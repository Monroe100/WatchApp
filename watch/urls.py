from django.conf.urls import url,include
from . import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns=[
    url('^$',views.welcome,name = 'welcome'),
    url(r'^accounts/', include('registration.backends.simple.urls')),
]