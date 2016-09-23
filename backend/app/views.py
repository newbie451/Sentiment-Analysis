from django.shortcuts import render, render_to_response
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from django.template import RequestContext
from app.models import Word
from django.template import Context
from django.template.loader import get_template
import predict
import os,time
import subprocess as sub
import json
# Create your views here.

def  home(request):
	return render(request,'sign.html')

@csrf_exempt
def keyword(request):
	return render(request,'keyword.html',content_type="")

@csrf_exempt
def text(request):
	return render(request,'textword.html',content_type="")

@csrf_exempt
def keyres(request):
	if request.method == "POST":
		m  = request.POST.get('key')
	temp = get_template('keyres.html')
	tweet=[]
	sentiment=[]
	count1=0
	count2=0
	var=['java -classpath' , '"lib/*:."' , 'SimpleStream2']
	var.append(m)
	command =  " ".join(var)
	print (command)
	p = os.popen(command,"r")
	count=0
	while count<13:
		line = p.readline()
		print (line)
		if count>2:
			if count%2==0:
				if "Positive" in line:
					count1+=1
					sentiment.append(line)
				elif "Negative" in line:
					count2+=1
					sentiment.append(line)
				else:
					sentiment.append("No keyword found")
			elif count%2==1:
				tweet.append(line)
		count+=1
	json_tweet = json.dumps(tweet)
	json_sentiment = json.dumps(sentiment)
	cont = RequestContext(request,{'tweets_array':json_tweet,'sent_array':json_sentiment,'count1':count1,'count2':count2})
	return HttpResponse(temp.render(cont))


@csrf_exempt
def normalres(request):
	temp = get_template('normalres.html')
	tweet=[]
	sentiment=[]
	count1=0
	count2=0
	var=['java -classpath' , '"lib/*:."' , 'SimpleStream']
	command =  " ".join(var)
	p = os.popen(command,"r")
	count=0
	while count<13:
		line = p.readline()
		print (line)
		if count>2:
			if count%2==0:
				if "Positive" in line:
					count1+=1
					sentiment.append(line)
				elif "Negative" in line:
					count2+=1
					sentiment.append(line)
				else:
					sentiment.append("No keyword found")
			elif count%2==1:
				tweet.append(line)
		count+=1
	json_tweet = json.dumps(tweet)
	json_sentiment = json.dumps(sentiment)
	cont = RequestContext(request,{'tweets_array':json_tweet,'sent_array':json_sentiment,'count1':count1,'count2':count2})
	return HttpResponse(temp.render(cont))

@csrf_exempt
def textres(request):
	if request.method == "POST":
		x  = request.POST.get('content')
	temp = get_template('textres.html')
	new_x = str(x)
	val = predict.main(new_x)
	cont = RequestContext(request,{'string':x,'sentiment':val})
	return HttpResponse(temp.render(cont))
