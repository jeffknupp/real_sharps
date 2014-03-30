from django.contrib import admin
from cappers.models import Pick, Handicapper, Sport
from guardian.admin import GuardedModelAdmin

class PickAdmin(GuardedModelAdmin):
    pass
class HandicapperAdmin(GuardedModelAdmin):
    pass
class SportAdmin(GuardedModelAdmin):
    pass

admin.site.register(Pick, PickAdmin)
admin.site.register(Handicapper, HandicapperAdmin)
admin.site.register(Sport, SportAdmin)
