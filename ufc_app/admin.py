from django.contrib import admin

from .models import Event, Fight, Fighter, FightResult, WeightClass


admin.site.register(WeightClass)
admin.site.register(Fighter)
admin.site.register(Event)
admin.site.register(Fight)
admin.site.register(FightResult)
