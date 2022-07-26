from django.contrib import admin
from django.urls import path,include
from home import views
#from .views import order_confirmation


urlpatterns = [
    path("admin/", admin.site.urls),
    path("",views.index, name="home"),  # go to index() of views
    path("index",views.index,name="home2"),
    path("about",views.about, name="about"), # go to about() of views
    path("contact",views.contact,name="contact"),  #putcommas error otherwise
    path("menu",views.menu,name="menu"),
    path("starters" ,views.starters,name="starters"),
    path("sweets", views.sweets, name="sweets"),
    path("item", views.item, name="item") ,
    #path("expression",views.expression, name="expression_value"),
    path('detail/<int:question_id>/', views.detail, name='detail'),
    #path('order_confirmation/<int:question_id>',order_confirmation.as_view(),name="order_confirmation"),
    #path('order', Order.as_view() , name="order"),
    
    path('order_confirmation/<int:question_id>/',views.order_confirmation, name='order-confirmation'),
    #path('order_confirmation1/',views.order_confirmation1, name='order-confirmation1')
    
     #path("order_confirmation", views.order_confirmation, name="order_confirmation") ,
    
]