from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User
from autoslug import AutoSlugField


class UpdateMixin(models.Model):
    """Mixin class for tracking when a model was updated."""
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Sport(models.Model):
    """A sport (like 'NFL') that cappers make picks for."""
    name = models.CharField(max_length=250)

    def __unicode__(self):
        return self.name


class Handicapper(User):
    """A Handicapper associated with the site."""
    specialty = models.ForeignKey(Sport, null=True)
    bio = models.TextField()

    def get_absolute_url(self):
        return '/cappers/' + slugify(self.username)

    def __unicode__(self):
        return self.username


class PickClass(models.Model):
    """A class of picks (e.g. "Bombs")"""
    name = models.CharField(max_length=250)
    description = models.TextField(blank=True, null=True)

    def __unicode__(self):
        return self.name


class Pick(UpdateMixin):
    """A single pick made by a Capper"""
    name = models.CharField(max_length=250)
    text = models.TextField()
    author = models.ForeignKey(Handicapper, related_name='product_post')
    pick_class = models.ForeignKey(PickClass, null=True)
    slug = AutoSlugField(populate_from='name')

    def __unicode__(self):
        return self.name


class PickSet(models.Model):
    """A named set of picks (e.g. 'AC's Bombs')"""
    picks = models.ManyToManyField(Pick)
    name = models.CharField(max_length=250)

    def __unicode__(self):
        return '{} pick set'.format(self.name)


class Product(models.Model):
    """An abstract product model."""
    price = models.FloatField()
    active = models.BooleanField(default=True)
    available_after = models.DateTimeField(auto_now_add=True)
    teaser = models.TextField(null=True)
    image = models.ImageField(upload_to='static', null=True, blank=True)

    def price_in_cents(self):
        return self.price * 100

    def __unicode__(self):
        return self.name


class PickProduct(Product):
    """A sell-able singe pick."""

    pick = models.ForeignKey(Pick)

    def get_absolute_url(self):
        return '/buy/picks/' + slugify(self.name)

    def __unicode__(self):
        return '{} at {}'.format(self.name, self.price)


class PickSetProduct(Product):
    """A sell-able collection of picks."""

    pick_set = models.ForeignKey(PickSet)

    def get_absolute_url(self):
        return '/buy/picksets/' + slugify(self.name)

    def __unicode__(self):
        return '{} at {}'.format(self.name, self.price)


class Purchase(models.Model):
    """A purchase made by a user of the site."""
    user = models.ForeignKey(User)
    product = models.ForeignKey(Product)
    purchased_at = models.DateTimeField(auto_now_add=True)
    purchase_id = models.TextField()
    valid_until = models.DateTimeField()

    def __unicode__(self):
        return '{} by {}'.format(self.product.name, self.user.email)