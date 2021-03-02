from django.shortcuts import render
from django.http import HttpResponse

from .models import Rickshaw

import json


def index(request):
    context = {}
    return render(request, "track/index.html", context)

def tracker(request):
    rickshaws = Rickshaw.objects.all()
    data = {}
    data["type"] = "FeatureCollection"
    data["features"] = []
    for r in rickshaws:
        temp = {}
        temp["type"] = "Feature"
        properties = {}
        metadata = []
        metadata.append("Driver Name: {}".format(r.name))
        metadata.append("License Plate: {}".format(r.license))
        metadata.append("Car Type: {}".format(r.type))
        properties["message"] = "\n".join(metadata)
        properties["iconSize"] = [18, 18]
        temp["properties"] = properties
        geometry = {}
        geometry["type"] = "Point"
        geometry["coordinates"] = [r.long, r.lat]
        temp["geometry"] = geometry
        data["features"].append(temp)
    context = {
        "data": json.dumps(data),
    }
    return render(request, "track/tracker.html", context)

def nearby(request):
    results = []
    lati=request.GET.get('latitude')
    longi=request.GET.get('longitude')
    rickshaws = Rickshaw.objects.all()
    for r in rickshaws:
        if r.is_nearby(lati, longi):
            results.append(r)
    context = {
        'rickshaws': results,
        'number': len(results)
    }
    return render(request, "track/nearby.html", context)
