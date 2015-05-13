from django.shortcuts import render, HttpResponse
from models import Mission
from forms import MissionForm
import json


def index(request):
    return render(request, 'realityquest/index.html')


def add_mission(request):
    if request.method == "POST":
        mission_form = MissionForm(data=request.POST)
        if mission_form.is_valid():
            mission_form.save()
            status = 'post'
    else:
        mission_form = MissionForm()
        status = 'get'

    return render(request, 'realityquest/add-mission.html', {'form': mission_form, 'status': status})


def all_missions(request):
    all_missions_list = Mission.objects.all()
    response_data = {"missions": []}
    for mission in all_missions_list:
        response_data['missions'].append({
            "Id": mission.id,
            "Lat": mission.lat,
            "Lng": mission.lng,
            "title": mission.title
        })
    return HttpResponse(json.dumps(response_data), content_type="application/json")
