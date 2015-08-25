from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin

# Django REST framework
from rest_framework import routers
from voting import views

# (Django rest framework) Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'choices', views.ChoiceViewSet) # choices is the url prefix (i.e. /choices/) # must include as views. ... as I import VIEWS, not VOTING

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    # RapidSMS core URLs
    url(r'^accounts/', include('rapidsms.urls.login_logout')),
    url(r'^$', 'rapidsms.views.dashboard', name='rapidsms-dashboard'),
    # RapidSMS contrib app URLs
    url(r'^httptester/', include('rapidsms.contrib.httptester.urls')),
    url(r'^messagelog/', include('rapidsms.contrib.messagelog.urls')),
    url(r'^messaging/', include('rapidsms.contrib.messaging.urls')),
    url(r'^registration/', include('rapidsms.contrib.registration.urls')),

    # Third party URLs
    url(r'^selectable/', include('selectable.urls')),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
