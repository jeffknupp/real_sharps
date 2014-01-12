import itertools

from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.template import RequestContext
from django.contrib import messages
from django.views.generic import ListView, DetailView

from cappers.models import Purchase, Pick, Handicapper, Sport


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

def user_has_purchased(user, pick):
    """Return True if a user has purchased the give pick."""
    purchases = Purchase.objects.filter(user=user)
    for purchase in purchases:
        if pick in purchase.picks.picks.all():
            return True

    return False

@login_required
def pick_detail(request, pk=None, *args, **kwargs):
    """Show either the pick or a teaser with an opportunity to buy it."""
    pick = get_object_or_404(Pick, pk=pk)
    purchased = True
    if not pick.active:
        messages.error(request, pick.name + 'is not yet active')
        return index_view()
    elif not request.user.has_perm(pick):
        purchased = False
    return render_to_response(
        'cappers/pick_detail.html',
        {
            'pick': pick,
            'purchased': purchased,
        },
        context_instance=RequestContext(request))

class PickListView(ListView):
    model = Pick
    def get_queryset(self):
        return Pick.objects.filter(active=True)

class CapperListView(ListView):
    model = Pick
    context_object_name = 'picks'


    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(CapperListView, self).get_context_data(**kwargs)
        # Add in the publisher
        context['author'] = self.author
        context['capper_results'] = self.capper_results
        return context

    def get_queryset(self):
        self.author = Handicapper.objects.get(pk=self.kwargs['pk'])
        self.capper_stats=Pick.objects.filter(author=self.author)
        sports = Sport.objects.all()
        self.capper_results = {}
        for sport in sports:
            sport_picks = self.capper_stats.filter(sport=sport)
            correct = sport_picks.filter(was_correct=True)
            self.capper_results[sport.name] = (len(sport_picks), len(correct))
        return Pick.objects.filter(author=self.author)


def charge():
    pass
