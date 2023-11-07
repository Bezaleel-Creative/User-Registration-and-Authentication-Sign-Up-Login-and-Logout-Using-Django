from django.shortcuts import render, redirect
from .models import Online_Appointment, Service_Category
from dashboard.models import *

# Create your views here.
def index(request):
    get_service = Service_Category.objects.all()
    ceo = Teamphoto.objects.filter(staff_possition=2).first()
    lab = Teamphoto.objects.filter(staff_possition=1).all()
    context = {
        'services' : get_service,
        'ceo' : ceo,
        'labs' : lab
    }
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        comment = request.POST.get('comment')
        service = request.POST.get('service')
        service_name = Service_Category.objects.get(service_name=service)
        appointment = Online_Appointment(name=name, email=email, phone=phone, comment=comment, service=service_name)
        appointment.save()
        return redirect('/')

    return render(request, 'myapp/index.html', context=context)
