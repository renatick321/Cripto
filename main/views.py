from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from Cripto.settings import BOT_TOKEN, ADMIN_ID
import requests


def main(request):
	return render(request, "main.html")


@login_required
def cabinet(request):
	return render(request, "cabinet.html")


def about(request):
	return render(request, "about_us.html")


def contact(request):
	if request.method == "POST":
		data = request.POST.dict()
		url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
		print(requests.post(url, {"chat_id": ADMIN_ID, 
			"text": f"Имя: {data['username']}\nПочта:{data['email']}\n{data['body']}"}))
	return render(request, "contact.html")