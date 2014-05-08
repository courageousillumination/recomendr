from django.conf.urls import patterns, include, url
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth.views import login, logout_then_login

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^login/', login),
    url(r'^logout/', logout_then_login),
    url(r'^admin/', include(admin.site.urls)),
    #Pass everything else onto the app
    url(r'', include('recomendr.recomendr.urls')),
    
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
