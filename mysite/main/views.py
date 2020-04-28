#Importing django assets
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import CarType, Manufacturer, CarModel
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from .forms import NewUserForm
# Create your views here.


def single_slug(request, single_slug):
    #Calling all objects in CarType and setting them equal to categories
    categories = [c.car_slug for c in CarType.objects.all()]
    #If object is in single slug filter all objects in Manufacturer and organize by alphabetical order
    if single_slug in categories:
        matching_car = Manufacturer.objects.filter(car_category__car_slug=single_slug).order_by("car_manufacturer")

        series_urls = {}
    #If object is in Manufacturer filter all objects in CarModel and organize by alphabetical order
        for m in matching_car.all():
            part_one = CarModel.objects.filter(car_manufacturer__car_manufacturer=m.car_manufacturer).earliest("model_published")
            series_urls[m] = part_one.model_slug
            
        return render(request, "main/category.html", {"part_ones": series_urls})

    #Redirect user to slug requested if the slug requested is equal to a slug in the database
    cars = [c.model_slug for c in CarModel.objects.all()]
    if single_slug in cars:
        this_car = CarModel.objects.get(model_slug = single_slug)
        cars_from_manufacturer = CarModel.objects.filter(car_manufacturer__car_manufacturer=this_car.car_manufacturer).order_by("model_title")

        this_car_idx = list(cars_from_manufacturer).index(this_car)

        return render(request, "main/model.html", {"car":this_car, "sidebar": cars_from_manufacturer, "this_car_idx": this_car_idx})

    #If webpage requested does not exist show information saying so
    return HttpResponse(f"{single_slug} does not correspond to anything.")

def homepage(request):
    return render(request=request,template_name="main/categories.html",context={"categories": CarType.objects.all})

#If user enters different password or invalid information return error message
#If user enters valid data when registering for an account redirect user to homepage and display toast saying account created and user logged in
def register(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"New Account Created: {username}")
            login(request, user)
            messages.info(request, f"You are now logged in as {username}")
            return redirect("main:homepage")
        else:
            for msg in form.error_messages:
                messages.error(request, f"{msg}:{form.error_messages[msg]}")

    form = NewUserForm
    return render(request, "main/register.html", context={"form":form})

#Showing toast messages when user logs out
def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("main:homepage")

#If user types username and password correctly redirect user to homepage and show toast saying they are logged ing
#If user types incorrect username or password show toast saying wrong username or password
def login_request(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f"You are now logged in as {username}")
                return redirect("main:homepage")
            else:
                messages.error(request, "Invalid username or password")
        else:
            messages.error(request, "Invalid username or password")
    
    form = AuthenticationForm()
    return render(request, "main/login.html", {"form":form})
    
