from django.http import HttpResponseRedirect, HttpResponse, HttpResponseForbidden, Http404
from django.shortcuts import render_to_response, get_object_or_404, get_list_or_404
from django.template import RequestContext
from django.views.generic import TemplateView, FormView
from django.conf import settings
from django.core.mail import send_mail
from main.forms import MessageForm
from main.models import Message

def index(request):
    visits = Message.objects.all()

    data = {
        'visits': visits
    }

    return render_to_response("index.html", data, context_instance=RequestContext(request))

def agregar(request):
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = MessageForm()

    data = {
        'form': form,
        }

    return render_to_response("add.html", data, context_instance=RequestContext(request))

def editar(request, id):
    message = Message.objects.get(pk=id)
    if request.method == 'POST':
        form = MessageForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = MessageForm(instance=message)

    data = {
      'form': form,
      }

    return render_to_response("add.html", data, context_instance=RequestContext(request))
