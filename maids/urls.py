from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^faq$', views.faq, name='faq'),
    url(r'^services$', views.services, name='services'),
    url(r'^login$', views.login, name='login'),
]