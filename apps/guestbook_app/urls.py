from django.conf.urls import url
from . import views

def test(request):
    print 701

urlpatterns = [
    url(r'^$', views.index),
    url(r'^process', views.process),
    url(r'^result', views.result),
]
