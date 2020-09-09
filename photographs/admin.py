from django.contrib import admin
from .models import ArchitecturalPhoto, FashionPhoto, FineartPhoto, AerialPhoto, PortraitPhoto, SportsPhoto

# Register your models here.
admin.site.register(AerialPhoto)
admin.site.register(ArchitecturalPhoto)
admin.site.register(FashionPhoto)
admin.site.register(FineartPhoto)
admin.site.register(PortraitPhoto)
admin.site.register(SportsPhoto)
