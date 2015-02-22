from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.http import Http404, HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.template import RequestContext, loader

#import work_doer
from .tasks import doin_work, add, app

# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at the adder index.")

def show_options(request):
    return render(request, 'adder/show_options.html')

def not_ready(request, async_num):
    context = {'async_num': async_num}
    return render(request, 'adder/not_ready.html', context)

def results(request, result_num):
    response = "Adding nine to what you gave me is %s."
    return HttpResponse(response % result_num)

def checker(request, async_num):
    res2 = app.AsyncResult(async_num)
    if res2.ready():
        rep = res2.get()
        return HttpResponseRedirect(reverse('adder:results', args=(rep,)))
    else:
        return HttpResponseRedirect(reverse('adder:not_ready', args=(async_num,)))
 
def plus_nine(request):
    # Always return an HttpResponseRedirect after successfully dealing
    # with POST data. This prevents data from being posted twice if a
    # user hits the Back button.
    number = int(request.POST['choice'])
    #rep = work_doer.doin_work(number)

    results = doin_work.delay(number)
    #rep = results.get()
    #import pdb
    #pdb.set_trace()
    if results.ready():
        rep = results.get()
        return HttpResponseRedirect(reverse('adder:results', args=(rep,)))
    else:
        return HttpResponseRedirect(reverse('adder:not_ready', args=(results.id,)))
    
