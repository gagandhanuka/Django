
from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$',views.home2,name="home2"),
    url(r'insert$',views.insertemp,name="insert"),
    url(r'update$',views.updateemp,name="update"),
    url(r'delete$',views.deleteemp,name="delete"),
    url(r'show$',views.showemp,name="show"),
    url(r'search$',views.searchemp,name="search"),
    url(r'insert_emp$',views.insert_emp,name="insert_emp"),
    url(r'delete_emp$',views.delete_emp,name="delete_emp"),
    url(r'update_emp$',views.update_emp,name="update_emp"),
    url(r'savedata$',views.savedata,name="savedata"),
]