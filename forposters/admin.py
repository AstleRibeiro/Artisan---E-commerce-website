from django.contrib import admin
from .models import CampaignPosters, CorporatePosters, PoliticalPosters, ShowPosters

# Register your models here.
admin.site.register(CampaignPosters)
admin.site.register(CorporatePosters)
admin.site.register(PoliticalPosters)
admin.site.register(ShowPosters)
