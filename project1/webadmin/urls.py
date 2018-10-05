from django.conf.urls import url
from django.urls import include, path

from . import views
urlpatterns = [
    url(r'^$',views.login,name="login"),
    url(r'^test/$',views.test,name="test"),
    url(r'^check/$',views.check,name="check"),
    url(r"^adminhome$",views.adminhome,name="adminhome"),
    url(r"^show$",views.show_to_admin,name="show_to_admin"),
    url(r"^search$",views.search,name="search"),
    url(r"^searchbyname$",views.searchbyuser,name="searchbyname"),
    url(r"^search_rest$",views.search_rest,name="search_rest"),
    path(r"checked/<Rid>/",views.checkit,name="checked"),
    url(r"^search_restbyname$",views.search_restbyname,name="search_restbyname"),
     path(r"viewloc/<rid>/",views.viewloc,name="viewloc"),
]