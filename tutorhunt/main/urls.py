
from django.conf.urls import url

from main import views

urlpatterns = [
    url(r'^$',views.bootstraphome,name='index'),
    url(r'^about$',views.aboutus,name='aboutus'),
    url(r'^contact$',views.contactus,name='contactus'),
    
    #url(r'home/$',views.home,name='home'),
]
