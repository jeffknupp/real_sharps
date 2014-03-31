from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.template import RequestContext
from django.contrib import messages
from django.views.generic import ListView, DetailView

from djstripe.decorators import subscription_payment_required

from cappers.models import Pick, Handicapper, Sport

def index_view(request):
    """Homepage view."""
    return render_to_response(
        'cappers/index.html',
        {
            'picks': Pick.objects.filter(active=True),
            'cappers': Handicapper.objects.all(),
            'messages': messages.get_messages(request),
        },
        context_instance=RequestContext(request))

@login_required
@subscription_payment_required
def pick_detail(request, pk=None, *args, **kwargs):
    """Show either the pick or a teaser with an opportunity to buy it."""
    pick = get_object_or_404(Pick, pk=pk)
    if not pick.active:
        messages.error(request, pick.name + 'is not yet active')
        return index_view()
    return render_to_response(
        'cappers/pick_detail.html',
        {
            'pick': pick,
        },
        context_instance=RequestContext(request))

def sport_list_view(request, pk=None, *args, **kwargs):
    context = {}
    context['picks'] = Pick.objects.filter(sport__pk=pk)
    context['is_capper'] = False
    sport = get_object_or_404(Sport, pk=pk)
    context['pick_category'] = sport.name
    return render_to_response(
            'cappers/pick_list.html',
            context,
            context_instance=RequestContext(request))

def pick_list_view(request, pk=None, *args, **kwargs):
    context = {}
    context['is_capper'] = False
    context['pick_category'] = 'All Picks'
    context['picks'] = Pick.objects.filter(active=True)
    return render_to_response(
            'cappers/pick_list.html',
            context,
            context_instance=RequestContext(request))
    
def capper_list_view(request, pk=None, *args, **kwargs):
    context = {}
    context['is_capper'] = True
    context['author'] = Handicapper.objects.get(pk=pk)
    capper_stats = Pick.objects.filter(author=context['author'])
    sports = Sport.objects.all()
    capper_results = {}
    for sport in sports:
        sport_picks = capper_stats.filter(sport=sport)
        correct = sport_picks.filter(was_correct=True)
        capper_results[sport.name] = (len(sport_picks), len(correct))
    context['picks'] = Pick.objects.filter(author=context['author'])
    context['capper_results'] = capper_results
    return render_to_response(
            'cappers/pick_list.html',
            context,
            context_instance=RequestContext(request))

def charge():
    pass
