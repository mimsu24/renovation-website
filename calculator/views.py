from django.views import View
from django.shortcuts import render, redirect
from decimal import Decimal, InvalidOperation
from django.urls import reverse
from .models import HouseType, FloorMaterial, WallMaterial, BathroomToilet, BathroomShower, BathroomSink, BathroomSpecialItem
import json

class DecimalEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Decimal):
            return str(obj)
        elif isinstance(obj, HouseType):
            return obj.type_of_house
        elif isinstance(obj, BathroomToilet):
            return obj.type_of_toilet
        elif isinstance(obj, BathroomShower):
            return obj.type_of_shower
        elif isinstance(obj, BathroomSink):
            return obj.type_of_sink
        elif isinstance(obj, BathroomSpecialItem):
            return obj.type_of_item
        return super(DecimalEncoder, self).default(obj)


class CalculatorView(View):
    def get(self, request):
        type_of_house = HouseType.objects.all()
        wall_material = WallMaterial.objects.all()
        floor_material = FloorMaterial.objects.all()
        type_of_toilet = BathroomToilet.objects.all()
        type_of_shower = BathroomShower.objects.all()
        type_of_sink = BathroomSink.objects.all()
        type_of_item = BathroomSpecialItem.objects.all()

        total_cost = request.session.pop('total_cost', None)
        total_floor_cost = request.session.pop('total_floor_cost', None)
        total_wall_cost = request.session.pop('total_wall_cost', None)

        floor_results = json.loads(request.session.pop('floor_results', '[]'))
        wall_results = json.loads(request.session.pop('wall_results', '[]'))
        house_result = json.loads(request.session.pop('house_result', '[]'))
        toilet_result = json.loads(request.session.pop('toilet_result', '[]'))
        shower_result = json.loads(request.session.pop('shower_result', '[]'))
        sink_result = json.loads(request.session.pop('sink_result', '[]'))
        item_result = json.loads(request.session.pop('item_result', '[]'))
       

        return render(request, 'calculator/index.html', {
            'type_of_house': type_of_house,
            'wall_material': wall_material,
            'floor_material': floor_material,
            'type_of_toilet': type_of_toilet,
            'type_of_shower': type_of_shower,
            'type_of_sink': type_of_sink,
            'type_of_item': type_of_item,
            'total_cost' : total_cost,
            'total_floor_cost' : total_floor_cost,
            'total_wall_cost' : total_wall_cost,
            'floor_results': floor_results,
            'wall_results': wall_results,
            'house_result': house_result,
            'toilet_result': toilet_result,
            'shower_result': shower_result,
            'sink_result': sink_result,
            'item_result': item_result,
        })

    def post(self, request):
        # Initialize total cost
        floor_results = []
        wall_results = []
        house_result = []
        toilet_result = []
        shower_result = []
        sink_result = []
        item_result = []
        sink_result = []
        total_cost = Decimal('0.0')
        total_floor_cost = Decimal('0.0')
        total_wall_cost = Decimal('0.0')

        house_type_id = request.POST.get('house_type')
        
        # Fetch the house type if provided and add its additional cost
        if house_type_id:
            house_type = HouseType.objects.get(id=house_type_id)
            total_cost += Decimal(house_type.add)
            house_result.append({
                 'type' : house_type,
                 'additional_cost' : str(house_type.add)
            })


        
        floor_square_meters_decimal = [Decimal(sqm) for sqm in request.POST.getlist('floor_square_meters[]') if sqm]
        floor_material_ids_decimal = [Decimal(material) for material in request.POST.getlist('floor_material_id[]') if material]
        

        # Then use these pre-converted values in your processing
        for mat_id, sqm_decimal in zip(floor_material_ids_decimal, floor_square_meters_decimal):
                material = FloorMaterial.objects.get(id=mat_id)
                sqm_decimal = sqm_decimal
                cost = material.price_per_square_meter * sqm_decimal
                total_floor_cost += cost
                total_cost += cost
                floor_results.append({
                    'type': 'Floor',
                    'material' : material.floor_material,
                    'square_meters' : sqm_decimal,
                    'cost' : cost
                })
                
                
        
        wall_square_meters_decimal = [Decimal(sqm) for sqm in request.POST.getlist('wall_square_meters[]') if sqm]
        wall_material_ids_decimal = [Decimal(material) for material in request.POST.getlist('wall_material_id[]') if material]
       

        # Then use these pre-converted values in your processing
        for mat_id, sqm_decimal in zip(wall_material_ids_decimal, wall_square_meters_decimal):
                material = WallMaterial.objects.get(id=mat_id)
                sqm_decimal = sqm_decimal
                cost = material.price_per_square_meter * sqm_decimal
                total_wall_cost += cost
                total_cost += cost
                wall_results.append({
                    'type': 'Wall',
                    'material' : material.wall_material,
                    'square_meters' : sqm_decimal,
                    'cost' : cost
                })
                

        # Fetch bathroom items and add their fixed cost (not based on square meters)
        type_of_toilet_id = request.POST.get('type_of_toilet', None)
        type_of_shower_id = request.POST.get('type_of_shower', None)
        type_of_sink_id = request.POST.get('type_of_sink', None)
        type_of_item_id = request.POST.get('type_of_item', None)
        if type_of_toilet_id:
            type_of_toilet = BathroomToilet.objects.get(id=type_of_toilet_id)
            total_cost += type_of_toilet.add  
            toilet_result.append({
                 'type' : type_of_toilet,
                 'additional_cost' : str(type_of_toilet.add)
            })

        if type_of_shower_id:
            type_of_shower = BathroomShower.objects.get(id=type_of_shower_id)
            total_cost += type_of_shower.add
            shower_result.append({
                 'type' : type_of_shower,
                 'additional_cost' : str(type_of_shower.add)
            })

        if type_of_sink_id:
            type_of_sink = BathroomSink.objects.get(id=type_of_sink_id)
            total_cost += type_of_sink.add
            sink_result.append({
                 'type' : type_of_sink,
                 'additional_cost' : str(type_of_sink.add)
            })

        if type_of_item_id:
            type_of_item = BathroomSpecialItem.objects.get(id=type_of_item_id)
            total_cost += type_of_item.add
            item_result.append({
                 'type' : type_of_item,
                 'additional_cost' : str(type_of_item.add)
            })

        request.session['floor_results'] = json.dumps(floor_results, cls=DecimalEncoder)
        request.session['wall_results'] = json.dumps(wall_results, cls=DecimalEncoder)
        request.session['house_result'] = json.dumps(house_result, cls=DecimalEncoder)
        request.session['toilet_result'] = json.dumps(toilet_result, cls=DecimalEncoder)
        request.session['shower_result'] = json.dumps(shower_result, cls=DecimalEncoder)
        request.session['sink_result'] = json.dumps(sink_result, cls=DecimalEncoder)
        request.session['item_result'] = json.dumps(item_result, cls=DecimalEncoder)

        request.session['total_cost'] = str(total_cost)
        request.session['total_floor_cost'] = str(total_floor_cost)
        request.session['total_wall_cost'] = str(total_wall_cost)


        
        print("Session total_cost:", request.session['floor_results'])
        print("Session total_cost:", request.session['wall_results'])


        # Redirect to display results
        return redirect(reverse('index') + '#calculator')
    


