from django.http import HttpResponse, HttpResponseRedirect
from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.core.urlresolvers import reverse
from eventbrite import Eventbrite
import requests
import json

from .models import Question, Category, Results

# Create your views here.
def index(request):
    p = Question.objects.get(pk='1')    
    return HttpResponseRedirect(reverse('pollEvents:details', args=(p.id,)))

def details(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    q = Question.objects.get(pk='1')
    category_list = q.category_set.all()
    for category in category_list:
        category.votes = 0
        category.save()
    
    return render(request, 'pollEvents/detail.html', {'question': question})

def vote(request, question_id):
    p = get_object_or_404(Question, pk=question_id)
    
    category_list = request.POST.getlist('category')
    for category in category_list:
        selected = Category.objects.get(pk=category)
        selected.votes+= 1
        selected.save()
        
    return HttpResponseRedirect(reverse('pollEvents:results', args=(p.id,)))


def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    #Load results for selected categories
    #Get the question
    q = Question.objects.get(pk='1')
    #get the list of categories
    category_list = q.category_set.all()
    #iterate over every category
    for category in category_list:
        #check if the category has 1 vote (it has been picked)
        if category.votes == 1:
                #create the parameters for the API call to find number of pages
                tmpload = ['token','4AV7SBC4EFRAY3P3TENN','categories',category.cID]
                t = "https://www.eventbriteapi.com/v3/events/search/"
                t = t + "?" + tmpload[2] + "=" + str(tmpload[3]) + "&" + tmpload[0] + "=" + tmpload[1]
                #request api
                tmp = requests.get(t)
                #Get the number of pages
                tmp_json = tmp.json()
                numofpages = tmp_json["pagination"]["page_count"]
                #iterate over every page in the API results
                for x in range(1,numofpages):
                    #Make API request
                    payload = ['token','4AV7SBC4EFRAY3P3TENN','pages',x,'categories',category.cID]
                    tt="https://www.eventbriteapi.com/v3/events/search/"
		    
                    tt = tt + "?" + payload[0] + "=" + payload[1] + "&" + payload[2] + "=" + str(payload[3]) + "&" + payload[4] + "=" + str(payload[5]) 
                    r = requests.get(tt)
                    #store api information as an object
                    json_object = r.json()
                    #iterate over every  event
                    for number in range(len(json_object)):
                        #Save individual events to the Results table
                        p=Results(category=json_object["events"][number]["category"],name=json_object["events"][number]["name"]["text"],eID=json_object["events"][number]["id"],city=json_object["events"][number]["venue"]["address"]["city"],country=json_object["events"][number]["venue"]["address"]["country"],link=json_object["events"][number]["url"])
                        p.save()
                   
    return render(request, 'pollEvents/results.html', {'question': question,'results':Results.objects.order_by('categories')})
