from django.http import HttpResponseRedirect
from django.template import RequestContext
from django.core.urlresolvers import reverse
from django.shortcuts import render_to_response
from microblog.models import Microblog
from microblog.forms import MicroblogForm

def index(request):
    return render_to_response('microblog/templates/index.html',
                              {'messages':Microblog.timeline(),
                               'form':MicroblogForm()},
                              context_instance=RequestContext(request))

def save(request):
    Microblog.add_message(request.POST['message'])
    return HttpResponseRedirect(reverse('microblog:index'))