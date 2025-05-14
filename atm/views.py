from django.shortcuts import render, redirect
from .models import CajeroUser
from django.contrib import messages

def login_view(request):
    if request.method == "POST":
        pin = request.POST.get("pin")
        try:
            user = CajeroUser.objects.get(pin=pin)
            request.session['user_id'] = user.id
            return redirect('menu')
        except CajeroUser.DoesNotExist:
            messages.error(request, "PIN incorrecto.")
    return render(request, 'login.html')
