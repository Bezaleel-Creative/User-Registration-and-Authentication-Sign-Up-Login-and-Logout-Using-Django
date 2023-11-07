from django.shortcuts import render, redirect
from .models import Teamphoto, Position
from django.contrib import messages
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='userapp:login')
def index(request):
    return render(request, 'dashboard/index.html')


@login_required(login_url='userapp:login')
def form(request):
    return render(request, 'dashboard/form.html')


@login_required(login_url='userapp:login')
def team(request):
    getposition = Position.objects.all()
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        email = request.POST.get('email')
        post = request.POST.get('post')
        image = request.FILES.get('upload')

        if image:
            posts = Position.objects.get(position=post)
            member = Teamphoto(name=name, email=email, photo=image, staff_possition=posts)
            member.save()
            messages.success(request, "Member Added Successfully")
            return redirect('dashboard:team')

        else:
            messages.error(request, "Please upload an Image")
            return redirect('dashboard:team')

    
    getmember = Teamphoto.objects.all()
    context = {
        'members' : getmember,
        'positions' : getposition
    }
    return render(request, 'dashboard/team.html', context)


@login_required(login_url='userapp:login')
def team_edit(request, id):
    get_team = Teamphoto.objects.get(id=id)
    if request.method == 'POST':
        get_team.name = request.POST.get('name')
        get_team.email = request.POST.get('email')

        if 'upload' in request.FILES:
            get_team.photo = request.FILES.get('upload')
        get_team.save()
        messages.success(request, "Member Updated Successfully")
        return redirect('dashboard:team')        

    context = {
        'team' : get_team
    }
    return render(request, 'dashboard/team_edit.html', context)


@login_required(login_url='userapp:login')
def team_delete(request, id):
    team_delete = Teamphoto.objects.get(id=id)
    team_delete.delete()
    return redirect('dashboard:team') 


@login_required(login_url='userapp:login')
def products(request):
    return render(request, 'dashboard/products.html')
