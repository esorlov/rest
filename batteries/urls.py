from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.BatteryList.as_view()),
    url(r'^(?P<pk>[0-9]+)/$', views.BatteryDetail.as_view()),
    url(r'^state/$', views.BatteryStateList.as_view()),
    url(r'^state/(?P<pk>[0-9]+)/$', views.BatteryStateDetail.as_view()),
]