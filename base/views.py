from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
rooms = [
    {"id": 1, "name": "Let's learn Django"},
    {"id": 2, "name": "Fundamentals of Java"},
    {"id": 3, "name": "Why NodeJs leading in startup market"}
]
user_info = {"name": "aman saurabh", "city": "greater noida", "age": 17, "joining_date": datetime.now(), "rooms" : rooms}

# Create your views here.
def home(request):
    return render(request, 'home.html', {"user": user_info});

def room(request, pk):
    #Following both implementations are correct
    #requested_room = [r for r in rooms if r['id'] == int(pk)];
    requested_room = list(filter(lambda a: a['id'] == int(pk), rooms))
    # Following is also correct but we want to handle it on template. So commented out it.
    # if(len(requested_room) == 1) :
    #     return render(request, 'room.html', { "room": requested_room[0] } );
    # else :
    #     return HttpResponse("Room not found");
    return render(request, 'room.html', { "room": requested_room[0] if len(requested_room) == 1 else None} );
    