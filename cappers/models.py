from django.db import models
from django.utils.text import slugify
from django.contrib.auth.models import User


class UpdateMixin(models.Model):
    """Mixin class for tracking when a model was updated."""

    class Meta:
        abstract = True

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Sport(models.Model):
    """A sport (like 'NFL') that cappers make picks for."""
    name = models.CharField(max_length=250)

    def __unicode__(self):
        return self.name


class Handicapper(User):
    """A Handicapper associated with the site."""
    specialty = models.ForeignKey(Sport, null=True, blank=True)
    bio = models.TextField()
    image = models.ImageField(upload_to='static', null=True, blank=True)

    def get_absolute_url(self):
        return '/cappers/' + slugify(self.username)

    def __unicode__(self):
        return self.username


class Pick(UpdateMixin):
    """A single pick made by a Capper"""

    name = models.CharField(max_length=250)
    pick_text = models.TextField()
    author = models.ForeignKey(Handicapper, related_name='product_post')
    teaser = models.TextField(default=True, null=True, blank=True)
    price = models.FloatField()
    for_sale_after = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)
    was_correct = models.BooleanField(default=False)
    sport = models.ForeignKey(Sport)

    class Meta:
        permissions = (
            ('view_pick', 'View a pick'),
        )

    def price_in_cents(self):
        return self.price * 100

    def __unicode__(self):
        return self.name

class Purchase(models.Model):
    """A purchase made by a user of the site."""
    user = models.ForeignKey(User)
    picks = models.ForeignKey(Pick)
    purchased_at = models.DateTimeField(auto_now_add=True)
    purchase_id = models.TextField()
    valid_until = models.DateTimeField()

    def __unicode__(self):
        return '{} by {}'.format(self.picks.name, self.user.email)