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
        return render(request, 'calculator/bathroom.html', {
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
        square_meters = request.POST.get('square_meters')

        # Convert square meters to Decimal only if provided
        square_meters = Decimal(square_meters) if square_meters else 0

        # Initialize total cost
        total_cost = 0

        # Fetch the house type if provided and add its additional cost
        if house_type_id:
            house_type = HouseType.objects.get(id=house_type_id)
            total_cost += Decimal(house_type.add)

        # Fetch wall and floor materials if provided and calculate cost based on square meters
        wall_material_id = request.POST.get('wall_material', None)
        floor_material_id = request.POST.get('floor_material', None)
        if wall_material_id and floor_material_id:
            wall_material = WallMaterial.objects.get(id=wall_material_id)
            floor_material = FloorMaterial.objects.get(id=floor_material_id)
            total_cost += wall_material.price_per_square_meter + floor_material.price_per_square_meter * square_meters
        elif floor_material_id:
            floor_material = FloorMaterial.objects.get(id=floor_material_id)
            total_cost += floor_material.price_per_square_meter * square_meters
        elif wall_material_id: 
            wall_material = WallMaterial.objects.get(id=wall_material_id)
            total_cost += wall_material.price_per_square_meter * square_meters

        # Fetch bathroom items and add their fixed cost (not based on square meters)
        type_of_toilet_id = request.POST.get('type_of_toilet', None)
        type_of_shower_id = request.POST.get('type_of_shower', None)
        type_of_sink_id = request.POST.get('type_of_sink', None)
        if type_of_toilet_id:
            type_of_toilet = BathroomToilet.objects.get(id=type_of_toilet_id)
            total_cost += type_of_toilet.add  # Assuming a fixed_price field exists

        if type_of_shower_id:
            type_of_shower = BathroomShower.objects.get(id=type_of_shower_id)
            total_cost += type_of_shower.add

        if type_of_sink_id:
            type_of_sink = BathroomSink.objects.get(id=type_of_sink_id)
            total_cost += type_of_sink.add

        # Store the calculated total cost in session
        request.session['total_cost'] = float(total_cost)

        # Redirect to display results
        return redirect(reverse('bathroom-calculator'))
















