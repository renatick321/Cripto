from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from Cripto.settings import BOT_TOKEN, ADMIN_ID
import requests


def main(request):
	return render(request, "index.html")


@login_required
def cabinet(request):
	return render(request, "cabinet.html")


def about(request):
	return render(request, "about.html")


def contact(request):
	print("121")
	if request.method == "POST":
		print(222)
		data = request.POST.dict()
		url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
		print(requests.post(url, {"chat_id": 705853549, 
			"text": f"Имя: {data['username']}\nПочта: {data['email']}\n{data['body']}"}))
	return render(request, "contact.html")