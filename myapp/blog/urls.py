from django.urls import path
from . import views
urlpatterns = [
    path('', views.home,name='home'),
    path('new_url', views.redirected_page,name='new'),
    path('old_url', views.url_redirect,name='old'),
    path('render', views.render_page,name='render'),
    path('detail/<str:slug>', views.detail_page,name='detail'),
]
