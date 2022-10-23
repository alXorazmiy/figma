from re import T
from django.contrib import admin
from .models import Homiylar, Talabalar, Tolovlar

# Register your models here.

#admin.site.register(Homiylar)
admin.site.register(Talabalar)
admin.site.register(Tolovlar)

@admin.register(Homiylar)
class HomiylarAdmin(admin.ModelAdmin):
    list_display = ('fish', 'holat')
    search_fields = ('fish',)
    list_filter = ('fish',)