from django.shortcuts import render, render_to_response, redirect
from django.http.response import HttpResponse
from django.template.loader import get_template
from django.template import Context
from poll.models import Chika
import random
import json
# Create your views here.

def top(reqest):
	top100chik = Chika.objects.order_by('likes').reverse()[0:100]	
	return render_to_response('top.html',{'top100chik':top100chik})

def poll(reqest):
	id_dev1 = random.randint(2717, 15130)
	id_dev2 = id_dev1
	while id_dev1==id_dev2:
		id_dev2 = random.randint(2717, 15130)
	dev1= Chika.objects.get(id=id_dev1)
	dev2= Chika.objects.get(id=id_dev2)
	return render_to_response('poll.html',{'dev1_link':dev1.vk_link,'dev1_photo':dev1.photo_link,'dev2_link':dev2.vk_link,'dev2_photo':dev2.photo_link,'id1':id_dev1,'id2':id_dev2})

def addlike(reqest,id_devki):
	try:
		chika = Chika.objects.get(id=id_devki)
		chika.likes+=1
		chika.save()
	except:
		pass
	return redirect("/")

def get2devki(reqest):
	id_dev1 = random.randint(2717, 15130)
	id_dev2 = id_dev1
	while id_dev1==id_dev2:
		id_dev2 = random.randint(2717, 15130)
	dev1= Chika.objects.get(id=id_dev1)
	dev2= Chika.objects.get(id=id_dev2)

	data_to_dump = {
	   'link1': dev1.vk_link,
	   'link2': dev2.vk_link,
	   'photo1': dev1.photo_link,
	   'photo2': dev2.photo_link,
	   'id1' : id_dev1,
	   'id2':id_dev2,
	}

	data = json.dumps(data_to_dump)

	return HttpResponse(data, content_type='application/json')

def vote_devka(reqest,id_devki):
	try:
		chika = Chika.objects.get(id=id_devki)
		chika.likes+=1
		chika.save()
	except:
		pass

	id_dev1 = random.randint(2717, 15130)
	id_dev2 = id_dev1
	while id_dev1==id_dev2:
		id_dev2 = random.randint(2717, 15130)
	dev1= Chika.objects.get(id=id_dev1)
	dev2= Chika.objects.get(id=id_dev2)

	data_to_dump = {
	   'link1': dev1.vk_link,
	   'link2': dev2.vk_link,
	   'photo1': dev1.photo_link,
	   'photo2': dev2.photo_link,
	   'id1' : id_dev1,
	   'id2':id_dev2,
	}

	data = json.dumps(data_to_dump)

	return HttpResponse(data, content_type='application/json')