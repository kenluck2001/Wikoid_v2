from django.template import RequestContext, Context,  loader, Template
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
import json
import requests as  req
from search import Search
from Wikoid.forms import SearchForm
from django.utils import simplejson

def results(search_text):
    links = []
    page_title='Search Result'
    search_text = search_text
    search_text = search_text.capitalize()
    WIKIPEDIA_BASE='https://en.wikipedia.org'
    seed = WIKIPEDIA_BASE + str('/wiki/') + str(search_text) # as seed
    search = Search(seed)
    graph = search.create_graph()
    for source, dest in graph:
        newDict = {"source": source, "target": dest }
        links.append(newDict)
    return links
    #return HttpResponse(json.dumps(links), content_type = "application/json")



def indexView(request, template_name="index.html"): 
    '''
        This is used to create the index page. This is the welcome screen for searching.
    '''
    '''
		This displays the comment form.
    '''
    page_title='Search Form'
    if request.method == 'GET':
        getdata = request.GET.copy()
        form = SearchForm(getdata)
        if form.is_valid():
            searchtext = getdata.get('searchbox','')
            #url='results/{0}/'.format(searchtext)
            #jsonObject = results(request, searchtext)
            #showPage(request, jsonObject)

            return HttpResponseRedirect(reverse('Show Page', args=(searchtext,)))
            #return HttpResponseRedirect(url)  
               
    else:
		form = SearchForm()

    return render_to_response(template_name, locals(), context_instance=RequestContext(request))


def showPage(request, searchtext, template_name="results.html"):
    '''
        This is used to get pictures of item.
    '''
    page_title='Wiki'
    items = results(searchtext)
    items = json.dumps(items)
    return render_to_response(template_name, locals(), context_instance=RequestContext(request))








