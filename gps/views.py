from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseRedirect, HttpResponse
from django.forms import ModelForm
from django.core import serializers

from gps.models import GpsNode, GpsNodeMetrics

# Create your views here.

import logging
log = logging.getLogger('gps')

def index(request):
    """ Show a list of all registered GpsNodes, ordered by last_active """
    log.info("view.index(request = %r)", request)
    nodes = GpsNode.objects.all().order_by('-last_active')
    return render(request, 'gps/index.html', {'nodes' : nodes})

def showAll(request, id, *args, **kwargs):
    """ Show detailed information about a GpsNode with associated metrics """
    log.info("view.showAll(request = %r, node = %r)", request, id)
    node = get_object_or_404(GpsNode, pk=id)
    #data = serializers.serialize("python", node.objects.all())
    return render(request, 'gps/showAll.html', {'node' : node})


def create(request, node):
    """ Create a new GpsNode based on request details """
    log.info("view.create(request = %r, node = %r)", request, node)
    pass


def delete(request, node):
    """ Delete a GpsNode based on request details """
    log.info("view.delete(request = %r, node = %r)", request, node)
    pass



class MetricForm(ModelForm):
    class Meta:
        model = GpsNodeMetrics
        fields = ['latitude', 'longitude', 'accuracy', 'speed',
                  'altitude', 'nsecTimestamp', 'bearing', 
                  'vin', 'vinLastCached']
        exclude = ['nsecTimestamp']

def update(request, id=None, *args, **kwargs):
    """ Update a GpsNode with passed metrics """
    # if this is a POST request, we need to process the form data
    log.info("view.update(request = %r, info = %r)", request, id)
    if request.method == 'POST':
        form = MetricForm(request.POST)
        if form.is_valid():
            # need to process data 
            #return HttpResponseRedirect('') # TODO - fill in url
            return HttpResponse("This is under work")
        return HttpResponse("Invalid form submitted")
    else:
        form = MetricForm()
    return render(request, 'gps/update.html', {'form' : form, 'node' : id})
