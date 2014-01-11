from django.contrib import admin
from cappers.models import PickProduct, PickSetProduct, Pick, PickSet, PickClass, Handicapper, Sport

admin.site.register([Pick, PickSet, PickProduct, PickSetProduct, PickClass, Handicapper, Sport])
# Register your models here.
