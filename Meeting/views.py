from django.shortcuts import render
import requests
from django.http import JsonResponse


def generate_meeting_url(meeting_name):
    base_url = "https://meet.jit.si/"
    return base_url + meeting_name

def create_meeting(request):
    meeting_name = request.GET.get('meeting_name', 'default_meeting')
    meeting_url = generate_meeting_url(meeting_name)
    
    return JsonResponse({'meeting_url': meeting_url})

def meeting_view(request):
    return render(request, 'meeting.html')