# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect, HttpResponse
from django import forms

# Create your views here.
def index(request):
	return render(request, 'survey_app/index.html')

def submit(request):
	print (request.method)
	if request.method == 'POST':
		print "*"*50
		request.session['name'] = request.POST['name']
		request.session['location'] = request.POST['location']
		request.session['language'] = request.POST['language']
		request.session['comments'] = request.POST['comments']
		print request.session['name']
		print request.session['location']
		print request.session['language']
		print request.session['comments']
		print "*"*50
	return redirect('/results')

def results(request):
	
	return render(request, 'survey_app/result.html')
