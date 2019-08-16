from django.shortcuts import render, render_to_response
from django.http.response import HttpResponse
from django.template.loader import get_template
from django.template import Context
from poll.models import Chika
import random
# Create your views here.

def top(reqest):
	name_page = "top"
	template = get_template("poll.html")
	html = template.render({'name': name_page})
	return HttpResponse(html)

def poll(reqest):
	# name_page = "poll"
	# template = get_template("poll.html")
	# html = template.render({'name': name_page})
	# return HttpResponse(html)
	id_dev1 = random.randint(2717, 15130)
	id_dev2 = id_dev1
	while id_dev1==id_dev2:
		id_dev2 = random.randint(2717, 15130)
	dev1= Chika.objects.get(id=id_dev1)
	dev2= Chika.objects.get(id=id_dev2)
	return render_to_response('poll.html',{'dev1_link':dev1.vk_link,'dev1_photo':dev1.photo_link,'dev2_link':dev2.vk_link,'dev2_photo':dev2.photo_link})

