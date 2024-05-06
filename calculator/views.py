from decimal import Decimal
from django.urls import reverse
from django.shortcuts import render, redirect
from django.views import View
from .models import FloorMaterial, HouseType, WallMaterial, BathroomItem

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
        floor_material = FloorMaterial.objects.all()
        wall_material = WallMaterial.objects.all()
        bathroom_item = BathroomItem.objects.all()
        bathroom_material = BathroomItem.objects.all()
        total_cost = request.session.pop('total_cost', None)
        return render(request, 'calculator/bathroom.html', {
            'type_of_house': type_of_house,
            'floor_material': floor_material,
            'wall_material': wall_material,
            'bathroom_item': bathroom_item,
            'bathroom_material': bathroom_material,
            'total_cost': total_cost,
        })
    
