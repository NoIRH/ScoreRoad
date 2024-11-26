from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.http import HttpResponseRedirect, HttpResponseNotFound

from django.db import connection
from .models import AI_segment_mark, User_segment_mark,Segment

def index(request):
    return render(request, "index.html")

@login_required
def save_user_mark(request):
    if request.method == 'POST':
        mark = request.POST.get("mark")
        user = request.user
        #заглушка пока не появяться реальные точки 
        segment, created = Segment.objects.get_or_create(start_point ="1", end_point="22")
        user_mark = User_segment_mark(user = user,segment = segment, mark = mark)
        user_mark.save()
    return HttpResponseRedirect("/")