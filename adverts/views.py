from django.shortcuts import render
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import user_passes_test
from .models import Advert
from .forms import AdvertForm


# Create your views here.


def is_admin(user):
    return user.is_superuser


@user_passes_test(is_admin)
def create_advert(request):
    if request.method == 'POST':
        form = AdvertForm(request.POST, request.FILES)
        if form.is_valid():
            advert = form.save(commit = False)
            advert.created_by = request.user
            advert.save()
            return redirect('advert_list')
    else:
        form = AdvertForm()
    
    return render(request, 'adverts/create_advert.html', {'form': form})


def advert_list(request):
    adverts = Advert.objects.all().order_by('-created_at')
    return render(request, 'adverts/advert_list.html', {'adverts': adverts}) 


def home(request):
    return render(request, 'adverts/home.html')