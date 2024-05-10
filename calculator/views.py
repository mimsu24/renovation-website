from django.views import View
from django.shortcuts import render, redirect
from decimal import Decimal
from .models import HouseType, FloorMaterial, WallMaterial, BathroomToilet, BathroomShower, BathroomSink, BathroomSpecialItem

class CalculatorView(View):
    def get(self, request):
        context = {
            'type_of_house': HouseType.objects.all(),
            'floor_material': FloorMaterial.objects.all(),
            'wall_material': WallMaterial.objects.all(),
            'type_of_toilet': BathroomToilet.objects.all(),
            'type_of_shower': BathroomShower.objects.all(),
            'type_of_sink': BathroomSink.objects.all(),
            'type_of_item': BathroomSpecialItem.objects.all(),
            'total_cost': request.session.get('total_cost', None)
        }
        return render(request, 'calculator/index.html', context)

    def post(self, request):
        calculator_type = request.POST.get('calculator_type')
        house_type_id = request.POST.get('house_type')
        square_meters = Decimal(request.POST.get('square_meters', '0'))
        print(f"Calculator type: {calculator_type}, House ID: {house_type_id}, Square Meters: {square_meters}")

        try:
            house_type = HouseType.objects.get(id=house_type_id)
            print(f"House Type: {house_type.type_of_house}")
        except HouseType.DoesNotExist:
            print("House type not found")
            return redirect('index')  # or handle error

        if calculator_type == 'floor':
            material_id = request.POST.get('floor_material')
            material = FloorMaterial.objects.get(id=material_id)
            cost = material.price_per_square_meter * square_meters
            print(f"Floor Material: {material.floor_material}, Cost: {cost}")
        elif calculator_type == 'wall':
            material_id = request.POST.get('wall_material')
            material = WallMaterial.objects.get(id=material_id)
            cost = material.price_per_square_meter * square_meters
            print(f"Wall Material: {material.wall_material}, Cost: {cost}")
        elif calculator_type == 'bathroom':
            cost = 0
            # Additional logic for bathroom

        total_cost = cost + Decimal(house_type.add)
        print(f"Total Cost: {total_cost}")
        request.session['total_cost'] = float(total_cost)
        return redirect('index')