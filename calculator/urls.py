from django.urls import path
from .views import WallCalculatorView, FloorCalculatorView, BathroomCalculatorView

urlpatterns = [
    path('', FloorCalculatorView.as_view(), name='floor-calculator'),
    path('calculator/wall', WallCalculatorView.as_view(), name='wall-calculator'),
    path('calculator/bathroom', BathroomCalculatorView.as_view(), name='bathroom-calculator'),
]
