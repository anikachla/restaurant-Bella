from django.contrib import admin

# Register your models here.
from.models import Contact
from.models import Dish
from.models import Category
from.models import OrderModel
from.models import Orderee

admin.site.register(Contact)
admin.site.register(Dish)
admin.site.register(Category)
admin.site.register(OrderModel)
admin.site.register(Orderee)


