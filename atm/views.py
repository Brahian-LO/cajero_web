from django.shortcuts import render, redirect
from .models import CajeroUser
from django.contrib import messages

def login_view(request):
    if request.method == 'POST':
        pin = request.POST.get('pin')
        try:
            user = CajeroUser.objects.get(pin=pin)
            request.session['user_id'] = user.id
            return redirect('menu')
        except CajeroUser.DoesNotExist:
            messages.error(request, '❌ PIN incorrecto.')
    return render(request, 'atm/login.html')


def menu_view(request):
    user_id = request.session.get('user_id')
    if not user_id:
        return redirect('login')

    user = CajeroUser.objects.get(id=user_id)
    return render(request, 'atm/menu.html', {'user': user})

def logout_view(request):
    request.session.flush()
    return redirect('login')

def depositar_view(request):
    user = CajeroUser.objects.get(id=request.session['user_id'])
    if request.method == "POST":
        monto = float(request.POST.get("monto", 0))
        if monto > 0:
            user.saldo += monto
            user.save()
            messages.success(request, f"✅ Se depositaron ${monto:.2f} correctamente.")
            return redirect('menu')
        else:
            messages.error(request, "⚠️ El monto debe ser mayor a 0.")
    return render(request, 'atm/depositar.html')

def retirar_view(request):
    user = CajeroUser.objects.get(id=request.session['user_id'])
    if request.method == "POST":
        monto = float(request.POST.get("monto", 0))
        if monto <= 0:
            messages.error(request, "⚠️ El monto debe ser mayor a 0.")
        elif monto > user.saldo:
            messages.error(request, "❌ Fondos insuficientes.")
        else:
            user.saldo -= monto
            user.save()
            messages.success(request, f"✅ Se retiraron ${monto:.2f} correctamente.")
            return redirect('menu')
    return render(request, 'atm/retirar.html')

def cambiar_pin_view(request):
    user = CajeroUser.objects.get(id=request.session['user_id'])
    if request.method == "POST":
        nuevo_pin = request.POST.get("nuevo_pin")
        if str(user.pin) == nuevo_pin:
            messages.error(request, "⚠️ El PIN debe ser distinto al anterior.")
        else:
            user.pin = int(nuevo_pin)
            user.save()
            messages.success(request, "✅ El PIN fue cambiado exitosamente.")
            return redirect('menu')
    return render(request, 'atm/cambiar_pin.html')