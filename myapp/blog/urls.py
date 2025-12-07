from django.urls import path
from . import views
urlpatterns = [
    path('render', views.home,name='home'),
    path('new_url', views.redirected_page,name='new'),
    path('old_url', views.url_redirect,name='old'),
    path('', views.render_page,name='render'),
    path('detail/<str:slug>', views.detail_page,name='detail'),
    path('contact', views.contact_page,name='contact'),
    path('about', views.about_page,name='about'),
    path('register', views.register_page,name='register'),
    path('login', views.login_page,name='login'),
    path('dashboard', views.dashboard_page,name='dashboard'),
    path('logout', views.logout_page,name='logout'),
]
