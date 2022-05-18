from django.conf.urls import url,include
from . import views 

urlpatterns = [
    #url('home',views.home,name='home'),
    url('index',views.indexFun, name = 'index')
]
