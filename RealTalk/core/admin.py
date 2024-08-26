from django.contrib import admin
from .models import *


class FeatureAdmin(admin.ModelAdmin):
    list_display = ('name', 'id', 'developer',
                    'staging_enabled', 'production_enabled')


class LandingPageAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_enabled', 'access_code')



admin.site.register(Post)
admin.site.register(Tag)
admin.site.register(Comment)
admin.site.register(Reply)
admin.site.register(LikedPost)
admin.site.register(LikedComment)
admin.site.register(LikedReply)
admin.site.register(Feature, FeatureAdmin)
admin.site.register(LandingPage, LandingPageAdmin)
