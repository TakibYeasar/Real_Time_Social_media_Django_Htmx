from django.contrib import admin
from django.urls import path, include
from .views import *
from django.views.generic.base import TemplateView
# Sitemaps
from django.contrib.sitemaps.views import sitemap
from core.sitemaps import *

sitemaps = {
    'static': StaticSitemap,
    'categories': CategorySitemap,
    'postpages': PostpageSitemap
}

app_name = 'authapi'

urlpatterns = [
    path('sitemap.xml/', sitemap, {'sitemaps': sitemaps},
         name='django.contrib.sitemaps.views.sitemap'),
    path('robots.txt/', TemplateView.as_view(template_name="robots.txt",
         content_type="text/plain")),
    path('accounts/', include('allauth.urls')),
    path('profile/', profile_view, name="profile"),
    path('<username>/', profile_view, name="userprofile"),
    path('profile/edit/', profile_edit_view, name="profile-edit"),
    path('profile/delete/', profile_delete_view, name="profile-delete"),
    path('profile/onboarding/', profile_edit_view, name="profile-onboarding"),
    path('profile/verify-email/', profile_verify_email,
         name="profile-verify-email"),
]
