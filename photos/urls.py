"""
HOME ULS CONFIGURATIONS
"""

from django.conf.urls import url

from photos.views import HomeView, ServiceView

urlpatterns = [
    url(r'^$', HomeView.as_view(), name='index'),
    url(r'^services$', ServiceView.as_view(), name='services'),
]
