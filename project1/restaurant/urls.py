from django.conf.urls import url
from . import views
from django.urls import include, path
urlpatterns = [
 url(r"^$",views.createrest,name="signup"),
 path(r"add/",views.addrest,name="add"),
 url(r"^addlocation$",views.addloc,name="addloc"),
 url(r"createloc",views.createloc,name="addloc"),
 path(r"viewloc/<rid>/",views.viewloc,name="viewloc"),
 path(r"editloc/<lid>/",views.editloc,name="editloc"),
 url(r"^editloc1$",views.editloc1,name="editloc1"),
 url(r"^search_loc$",views.searchloc,name="searchloc"),
 path(r"search/",views.search,name="search"),
]