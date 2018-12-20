from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import  static
from . import views

urlpatterns = [
    url('^$',views.home, name = 'home'),
    url(r'^profile/(\w+)',views.profile,name = 'profile'),
    url(r'^new/project$',views.new_project,name = 'new_project'),
    url(r'^search/',views.search,name='search'),
    url(r'^project/(\w+)',views.project,name='project'),
    url(r'^rate/(\d+)',views.rate,name='rate'),
    url(r'^api/profile/$', views.ProfApi.as_view()),
    url(r'^api/project/$', views.ProjApi.as_view()),
    url(r'^new/profile$',views.new_profile,name = 'new_profile'),
]
if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)
