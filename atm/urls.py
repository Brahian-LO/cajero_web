from django.urls import path
from .views import login_view, menu_view, logout_view, depositar_view, retirar_view, cambiar_pin_view

urlpatterns = [
    path('', login_view, name='login'),
    path('menu/', menu_view, name='menu'),
    path('logout/', logout_view, name='logout'),
    path('depositar/', depositar_view, name='depositar'),
    path('retirar/', retirar_view, name='retirar'),
    path('cambiar-pin/', cambiar_pin_view, name='cambiar_pin'),
]
