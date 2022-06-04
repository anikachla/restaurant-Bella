from django.contrib import admin
from django.urls import path,include
from home import views

urlpatterns = [
    path("admin/", admin.site.urls),
    path("",views.index, name="home"),  # go to index() of views
    path("about",views.about, name="about"), # go to about() of views
    path("contact",views.contact,name="contact"),  #putcommas error otherwise
    path("menu",views.menu,name="menu")
     
]