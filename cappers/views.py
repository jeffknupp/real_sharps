import itertools

from django.contrib.auth.decorators import login_required
from django.shortcuts import render_to_response, redirect
from django.template import RequestContext
from django.contrib import messages

from cappers.models import Product, Purchase, PickSetProduct, PickProduct


def index_view(request):
    """Homepage view."""
    return render_to_response(
        'cappers/index.html',
        {
            'pick_products': PickProduct.objects.filter(active=True),
            'pickset_products': PickSetProduct.objects.filter(active=True),
            'messages': messages.get_messages(request),
        },
        context_instance=RequestContext(request))


@login_required
def pick_product_detail(request, slug=None, *args, **kwargs):
    product = PickProduct.objects.get(slug=slug)
    if not Purchase.objects.filter(user=request.user, product=product).exists():
        messages.error(request, 'You have not purchased [' + product.name + ']')
        return redirect('home')
    else:
        return render_to_response(
            'cappers/product_detail.html',
            {'product': product},
            context_instance=RequestContext(request))


@login_required
def pickset_product_detail(request, slug=None, *args, **kwargs):
    product = PickSetProduct.objects.get(slug=slug)
    if not Purchase.objects.filter(user=request.user, product=product).exists():
        messages.error(request, 'You have not purchased [' + product.name + ']')
        return redirect('home')
    else:
        return render_to_response(
            'cappers/product_detail.html',
            {'product': product},
            context_instance=RequestContext(request))

def product_list(request, *args, **kwargs):
    products = itertools.chain(PickProduct.objects.filter(active=True), PickSetProduct.objects.filter(active=True))
    print products
    return render_to_response(
        'cappers/product_list.html',
        {'products': products},
        context_instance=RequestContext(request))

def charge():
    pass
