from django.shortcuts import render
import json
from django.http import JsonResponse, HttpResponse
# Create your views here.
from .models import FoodMenu


def Create(request):
    if request.method == "POST":
        body = json.loads(request.body)
        foodname = body["foodname"]
        price = body["price"]
        available = body["available"]
        menu = FoodMenu.objects.create(
            foodname=foodname, price=price, available=available)
    else:
        return HttpResponse(json.dumps({"msg": "wrong routes"}))
    return HttpResponse(json.dumps({"msg": "Data Posted succesfully"}))


def Get(req):
    menu = FoodMenu.objects.all()
    arr = {"data": list(menu.values())}
    return JsonResponse(arr)


def Update(request, itemid):
    print(type(itemid))
    if request.method == "PATCH":
        menu = FoodMenu.objects.get(id=itemid)
        menu.available = "yes"
        menu.save()
    else:
        return JsonResponse({"msg": "eror"})
    return JsonResponse({"msg": "Update"})


def Delete(request, itemid):
    if request.method == "DELETE":
        menu = FoodMenu.objects.get(id=itemid)
        menu.delete()
    else:
        return JsonResponse({"msg": "eror"})
    return HttpResponse(json.dumps({"msg": "Deleted"}))