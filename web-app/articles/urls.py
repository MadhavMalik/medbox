from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.article_list),
    url(r'contact', views.contact),
]
