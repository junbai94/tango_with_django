from django.conf.urls import url
from . import views

urlpatterns = [
        url(r'^$', views.index, name='index'),
        url(r'^about/', views.about, name='about'),
        url(r'^category/(?P<category_slug>[\w\-]+)/$', views.category, name='category'),
        url(r'^add_category/$', views.add_category, name='add_category'),
        ]