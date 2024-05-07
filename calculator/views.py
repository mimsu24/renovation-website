from decimal import Decimal
from django.urls import reverse
from django.shortcuts import render, redirect
from django.views import View
from .models import FloorMaterial, HouseType, WallMaterial, BathroomToilet, BathroomSink, BathroomShower, BathroomSpecialItem

class FloorCalculatorView(View):
    # Handle GET requests
    def get(self, request):
        # Fetch types of houses and materials to populate the form
        type_of_house = HouseType.objects.all()
        floor_material = FloorMaterial.objects.all()
        total_cost = request.session.pop('total_cost', None)
        return render(request, 'calculator/floor.html', {
            'type_of_house': type_of_house,
            'floor_material': floor_material,
            'total_cost': total_cost
        })

    # Handle POST requests
    def post(self, request):
        house_type_id = request.POST.get('house_type')
        square_meters = Decimal(request.POST.get('square_meters', '0'))  # Convert to Decimal here
        material_id = request.POST.get('floor_material')

        house_type = HouseType.objects.get(id=house_type_id)
        material = FloorMaterial.objects.get(id=material_id)


        # Ensure both operands are Decimal before multiplication
        total_cost = (material.price_per_square_meter * square_meters) + Decimal(house_type.add)
        request.session['total_cost'] = float(total_cost)
        return redirect(reverse('floor-calculator'))

class WallCalculatorView(View):
    # Handle GET requests
    def get(self, request):
        # Fetch types of houses and materials to populate the form
        type_of_house = HouseType.objects.all()
        wall_material = WallMaterial.objects.all()
        total_cost = request.session.pop('total_cost', None)
        return render(request, 'calculator/wall.html', {
            'type_of_house': type_of_house,
            'wall_material': wall_material,
            'total_cost' : total_cost,
        })
    
     # Handle POST requests
    def post(self, request):
        house_type_id = request.POST.get('house_type')
        square_meters = Decimal(request.POST.get('square_meters'))
        material_id = request.POST.get('wall_material')

        house_type = HouseType.objects.get(id=house_type_id)
        material = WallMaterial.objects.get(id=material_id)

        total_cost = (material.price_per_square_meter * square_meters) + Decimal(house_type.add)
        request.session['total_cost'] = float(total_cost)
        return redirect(reverse('wall-calculator'))
    
class BathroomCalculatorView(View):
    def get(self, request):
        type_of_house = HouseType.objects.all()
        wall_material = WallMaterial.objects.all()
        floor_material = FloorMaterial.objects.all()
        type_of_toilet = BathroomToilet.objects.all()
        type_of_shower = BathroomShower.objects.all()
        type_of_sink = BathroomSink.objects.all()
        type_of_item = BathroomSpecialItem.objects.all()
        total_cost = request.session.pop('total_cost', None)
        return render(request, 'calculator/Bathroom.html', {
            'type_of_house': type_of_house,
            'wall_material': wall_material,
            'floor_material': floor_material,
            'type_of_toilet': type_of_toilet,
            'type_of_shower': type_of_shower,
            'type_of_sink': type_of_sink,
            'type_of_item': type_of_item,
            'total_cost' : total_cost,
        })
    
    def post(self, request):
        house_type_id = request.POST.get('house_type')
        square_meters = Decimal(request.POST.get('square_meters', '0'))
        total_cost = Decimal('0')

        if house_type_id:
            house_type = HouseType.objects.get(id=house_type_id)
            total_cost += Decimal(house_type.add)  # Add costs associated with house type

        # Check each possible renovation choice, adding costs as needed
        wall_material_id = request.POST.get('wall_material')
        if wall_material_id:
            wall_material = WallMaterial.objects.get(id=wall_material_id)
            total_cost += wall_material.price_per_square_meter * square_meters

        floor_material_id = request.POST.get('floor_material')
        if floor_material_id:
            floor_material = FloorMaterial.objects.get(id=floor_material_id)
            total_cost += floor_material.price_per_square_meter * square_meters

        # Similar checks for other bathroom components
        type_of_toilet_id = request.POST.get('type_of_toilet')
        if type_of_toilet_id:
            type_of_toilet = BathroomToilet.objects.get(id=type_of_toilet_id)
            total_cost += Decimal(type_of_toilet.add)  # Assuming .add holds the cost

        type_of_shower_id = request.POST.get('type_of_shower')
        if type_of_shower_id:
            type_of_shower = BathroomShower.objects.get(id=type_of_shower_id)
            total_cost += Decimal(type_of_shower.add)

        type_of_sink_id = request.POST.get('type_of_sink')
        if type_of_sink_id:
            type_of_sink = BathroomSink.objects.get(id=type_of_sink_id)
            total_cost += Decimal(type_of_sink.add)

        type_of_item_id = request.POST.get('type_of_item')
        if type_of_item_id:
            type_of_item = BathroomSpecialItem.objects.get(id=type_of_item_id)
            total_cost += Decimal(type_of_item.add)

        request.session['total_cost'] = float(total_cost)  # Storing as float for session storage
        return redirect(reverse('bathroom-calculator'))
















"""
        house_type_id = request.POST.get('house_type')
        square_meters = Decimal(request.POST.get('square_meters'))
        wall_material_id = request.POST.get('wall_material')
        floor_material_id = request.POST.get('floor_material')
        type_of_toilet_id = request.POST.get('type_of_toilet')
        type_of_shower_id = request.POST.get('type_of_shower')
        type_of_sink_id = request.POST.get('type_of_sink')
        type_of_item_id = request.POST.get('type_of_item')


        get_house_type_id = HouseType.objects.get(id=house_type_id)
        get_wall_material_id = WallMaterial.objects.get(id=wall_material_id)
        get_floor_material_id = FloorMaterial.objects.get(id=floor_material_id)
        get_type_of_toilet_id = BathroomToilet.objects.get(id=type_of_toilet_id)
        get_type_of_shower_id = BathroomShower.objects.get(id=type_of_shower_id)
        get_type_of_sink_id = BathroomSink.objects.get(id=type_of_sink_id)
        get_type_of_item_id = BathroomSpecialItem.objects.get(id=type_of_item_id)

"""
