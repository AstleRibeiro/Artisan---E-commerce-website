from django.contrib import admin
from .models import AbstractPainting, AcrylicPainting, PastelPainting, InkPainting

# Register your models here.
admin.site.register(AbstractPainting)
admin.site.register(AcrylicPainting)
admin.site.register(PastelPainting)
admin.site.register(InkPainting)