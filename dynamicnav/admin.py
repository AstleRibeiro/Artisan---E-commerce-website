from django.contrib import admin
from .models import AbstractPainting, WildlifePainting, PastelPainting, InkPainting

# Register your models here.
admin.site.register(AbstractPainting)
admin.site.register(WildlifePainting)
admin.site.register(PastelPainting)
admin.site.register(InkPainting)
