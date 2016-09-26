from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'add$', views.addQuote, name = 'addQuote'),
    url(r'favorite/add/(?P<quoteID>\d+)$', views.addFavorite, name = 'addFavorite'),
    url(r'favorite/remove/(?P<quoteID>\d+)$', views.removeFavorite, name = 'removeFavorite'),
    url(r'users/(?P<userID>\d+)$', views.userSummary, name = 'userSummary')
]
