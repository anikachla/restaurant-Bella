from asyncio.windows_events import NULL
from django.shortcuts import render,HttpResponse
from urllib3 import HTTPResponse
from .models import Dish
from .models import Category
from .models import OrderModel
from .models import Orderee

from django.views import View
from django.core.mail import send_mail
from django.shortcuts import redirect
from django.http import Http404
from datetime import datetime
from django.contrib import messages

# Create your views here.
from home.models import Contact
import random


def index(request):
    return render(request,'index.html')  
    # path to reach index.html

def admin(request):
    return render(request,'http://127.0.0.1:8000/admin')
    
def about(request):
    #return HttpResponse("My about page")
    return render(request,'about.html')

def contact(request):
    #return HttpResponse("My contact page")
    if request.method =='POST':
        name = request.POST.get('name')
        email =request.POST.get('email')
        phone= request.POST.get('phone')
        issue= request.POST.get('issue')
        
        contactobj = Contact(name=name, email=email, phone=phone, issue =issue)
        contactobj.save()   
      
        
    
    return render(request,'contact.html')

def item(request):
    # #return HttpResponse("My contact page")
    # if request.method =='POST':
    #     name = request.POST.get('name')
    #     email =request.POST.get('email')
    #     phone= request.POST.get('phone')
    #     issue= request.POST.get('issue')
        
    #     contactobj = Contact(name=name, email=email, phone=phone, issue =issue)
    #     contactobj.save()   
     
     return render(request, 'item.html')
    # return render(request,'item.html')

def menu(request):
    
    
    main1 = Dish()
    main1.id = 1
    main1.name= 'Masala Dosa'
    main1.img= 'menu1.jfif'
    main1.desc = 'Baked potatoes with chopped onions stuffed in Dosa. Served with Sambhar and Chutney'
    main1.price = 80 # main1.img = {% static 'images/menu1.jfif' %}
    main1.time = '15 mins to prepare'
    
    main1.save()
    
    main2 = Dish()
    main2.id = 2
    main2.name= 'Chole Bhature'
    main2.img= 'menu2.jfif'
    main2.desc ='A combination of chana masala fused spicy white chickpeas and bhatura/puri, a fried bread made from maida. ' 
    main2.price = 180
    main2.time = '10 mins to prepare'
    
    
    main3 = Dish()
    main3.id = 3
    main3.name= 'Daal Fry '
    main3.img= 'daal.jfif'
    main3.desc = 'soft-cooked dal (lentils) which is then sautéed in a masala made of onion, tomato, ginger, garlic, and spices in ghee '
    main3.price = 60
    main3.time = '15 mins to prepare'
    
    main4 = Dish()
    main4.id = 4
    main4.name= 'Shahi Kadhai Paneer'
    main4.img= 'menu3.jfif'
    main4.desc = 'The combination of paneer, onion and colourful bell peppers coated with spicy tomato sauce, aromatic spices and herbs, cooked with buttermilk curry.'
    main4.price = 180 
    main4.time = '20 mins to prepare'
    
    main5 = Dish()
    main5.id = 5
    main5.name= 'Roti and Rice'
    main5.img= 'menu5.jfif'
    main5.desc = 'Order two Rotis and a bowl of rice on the side for your Daal or vegetables. White Rice boiled,cooked with indian wheat bread.'
    main5.price = 70 
    main5.time = '8 mins to prepare'
    
    main6 = Dish()
    main6.id = 6
    main6.name= 'Pure Veg Thali'
    main6.img= 'menu4.jfif'
    main6.desc = 'The thali includes roti, rice, phakala , dalma (signature lentil and vegetables dish),  alu posto , baingan chatka , phulgobi kosha , tamato khatta .'
    main6.price = 110 # main1.img = {% static 'images/menu1.jfif' %}
    main6.time = '15 mins to prepare'
    
    main7 = Dish()
    main7.id = 7
    main7.name= 'Hakka Noodles'
    main7.img= 'menu6.jfif'
    main7.desc = ' Boiled noodles with soy sauce and fresh veggies such as cabbage,carrots, spring onions,garlic and beans. Order Manchurian by its side .'
    main7.price = 160 
    main7.time = ' mins to prepare'
    
    main8 = Dish()
    main8.id =8 
    main8.name= 'Manchurian balls'
    main8.img= 'menu9.jfif'
    main8.desc = 'Gravy filled Manchurian balls. Manchurian has chopped cabbage, carrots,onion,garlic filling coated in Maida and fried.'
    main8.price = 220 
    main8.time = '20 mins to prepare'
    
    main9 = Dish()
    main9.id = 9
    main9.name= 'Vegetable Biryani'
    main9.img= 'biryani.jfif'
    main9.desc = 'Fragrant Rice dum cooked with cumin,coriander,tamarind,cinnamon spices and caramelized onions,beans carrots with saffron infused milk'
    main9.price = 230
    main9.time = ' 12 mins to prepare'
    
    main10 = Dish()
    main10.id = 10
    main10.name= 'Alfredo Veggie Pizza'
    main10.img= 'menu8.jfif'
    main10.desc = 'White Alfredo sauce oven cooked pizza .The toppings include diced capsicums,tomatoes, black Olives, Jalepenos, and of coarse mozzarella cheese.'
    main10.price = 380 
    main10.time = '24 mins to prepare'
    
    main11 = Dish()
    main11.id = 11
    main11.name= 'White Sauce Pasta '
    main11.img= 'pasta.jfif'
    main11.desc = 'A silky smooth and aromatic  creamy sauce made from butter, milk and all purpose flour (maida),and munchy red green Bellpeppers, Black Olives . Oregano provided on the side .'
    main11.price = 280 # main1.img = {% static 'images/menu1.jfif' %}
    main11.time = '20 mins to prepare'
    
    main12= Dish()
    main12.id = 12
    main12.name= 'Veggie Tortilla Wrap'
    main12.img= 'wrap.jfif'
    main12.desc = ' A healthy yet fun combinantion  of  all veggies ,such as  capsicums,onions,kale,tomatoes,chillies and paprika covered in saucy Southwest sauce,rolled in Tortillas'
    main12.price = 210 # main1.img = {% static 'images/menu1.jfif' %}
    main12.time = '24 mins to prepare'
    
    
    MainCourse = Category()
    MainCourse.save()
    #Cannot assign "'MainCourse'": "Dish.category" must be a "Category" instance.
    
    main_course= [main1,main2,main3,main4,main5,main6,main7,main8,main9,main10,main11,main12]
    for s in main_course:
        s.category = MainCourse
    
    main2.save()
    main3.save()
    main4.save()
    main5.save()
    main6.save()
    main7.save()
    main8.save()
    main9.save()
    main10.save()
    main11.save()
    main12.save()

   
    
    return render(request,'menu2.html',{'main_course':main_course})

def starters(request):
    
    
    s1= Dish()
    s1.id = 11
    s1.name= 'SAMOSA '
    s1.img= 'starter4.jfif'
    s1.desc = 'The chatpata all time favourite snack, consisting of Potatoes,Peas, Onions served with Tamarind(Imli) Chutney '
    s1.price = 40
    s1.time = ' 7 mins to prepare'
    
    s2= Dish()
    s2.id = 12
    s2.name= 'KOTHIMBIR WADI'
    s2.img= 'starter5.jfif'
    s2.desc = ' Kothimbir Vadi is a Maharshtrian snack recipe made using cilantro (kothimbir) and gram flour (chickpea flour).  '
    s2.price = 70
    s2.time = '10 mins to prepare'
    
    s3= Dish()
    s3.id = 13
    s3.name= 'BUN MUSKA'
    s3.img= 'starter6.jfif'
    s3.desc = ' Wheat/Maida  Buns smeared with generous amounts of butter , served with jam '
    s3.price = 60
    s3.time = '5 mins to prepare'
    
    s4= Dish()
    s4.id = 14
    s4.name= 'PANEER KABAB'
    s4.img= 'starter1.jfif'
    s4.desc = ' The combination of grilled paneer, onion and colourful bell peppers coated with spicy tomato sauce, aromatic spices and herbs '
    s4.price = 180 
    s4.time = '20 mins to prepare'
    
    s5= Dish()
    s5.id = 15
    s5.name= 'VEGGIE SALAD'
    s5.desc = 'Seasonal Salad made from Lettuce, Kale, Cilantro, Herbs and Mayonise .Order this on the side for your Daal. White Rice boiled,cooked with indian wheat bread..jfif'
    s5.img = 'starter2.jfif'
    s5.price = 110
    s5.time = '8 mins to prepare'
    
    s6= Dish()
    s6.id = 16
    s6.name= 'MASALA PAPAD'
    s6.img= 'starter3.jfif'
    s6.desc = 'A native Maharshtrian snack made of fried Papad and tossed onions,tomatoes,cilantro,and Seviya . Goes well with Daal Roti '
    s6.price = 50
    s6.time = '15 mins to prepare'
    
    Starters =Category()
    Starters.save()
    
    starters = [s1,s2,s3,s4,s5,s6]
    for s in starters:
        s.category = Starters
    
    s1.save()
    s2.save()
    s3.save()
    s4.save()
    s5.save()
    s6.save()
    
    return render(request,'starters2.html',{'starters':starters})

def sweets(request):
    
    s1= Dish()
    s1.id = 17
    s1.name= 'Chocolate Ice Cream'
    s1.img= 'icecream1.jfif'
    s1.desc = 'Chocolate Creamy Ice Cream made from cocoa ,milk,sugar,butter and honey . All time favourite dessert to have .                                                                                 '
    s1.price = 170
    s1.time = '5 mins to prepare'
    
    s2= Dish()
    s2.id = 18
    s2.name= 'Strawberry Ice Cream '
    s2.img= 'icecream2.jfif'
    s2.desc = 'Strawberry slices added in Whipped Cream and Vanilla ice cream give you the ultimate Mahabaleshwar feels.'
    s2.price = 180
    s2.time = '5 mins to prepare'
    
    s3= Dish()
    s3.id = 19
    s3.name= 'ORANGE JUICE '
    s3.img= 'juice1.jfif'
    s3.desc = 'Freshly squeezed juice from Oranges rich in Vitamin C.Ice cubes and little sugar is added.'
    s3.price = 90
    s3.time = '7 mins to prepare'
    
    s4= Dish()
    s4.id = 20
    s4.name= 'GAAJAR ka HALWA'
    s4.img= 'halwa.jfif'
    s4.desc = 'A traditional North Indian dessert made by simmering fresh grated carrots with full fat milk,sugar and ghee,garnished with chopped nuts.'
    s4.price = 220
    s4.time = '10 mins to prepare'
    
    s5= Dish()
    s5.id = 21
    s5.name= 'COLD COFFEE'
    s5.img= 'coffee.jfif'
    s5.desc = ' Chilled coffee with whipped cream and sprinkled cocoa powder.  Creamy and Choclatey to keep you going through out your day.'
    s5.price = 70
    s5.time = '10 mins to prepare'
    
    s6= Dish()
    s6.id = 22
    s6.name= 'MIXED FRUIT JUICE'
    s6.img= 'juice2.jfif'
    s6.desc = 'The mixture of goody fruits such as Guavas, Oranges,Watermelons,Pineapples and Pomegranates.'
    s6.price = 50
    s6.time = '7 mins to prepare'
    
    Sweets = Category() # obj of class category sent as foreign key to this model
    Sweets.save()
    sweets = [s1,s2,s3,s4,s5,s6]
    
    
    for s in sweets:
        s.category = Sweets
        
    s1.save()
    s2.save()
    s3.save()
    s4.save()
    s5.save()
    s6.save()
   
    return render(request,'sweets2.html',{'sweets':sweets})


def detail(request, question_id):
    try:
        food = Dish.objects.get(pk=question_id)
       
    except Dish.DoesNotExist:
        raise Http404("Question does not exist")
    
    return render(request, 'output.html', {'food': food})


# def order_confirmation1(request, context):
#      # info form details object save
#      question_id= context["id"]
#      order=Orderer()
#      fname=request.POST.get('fname')
#      lname=request.POST.get('fname')
#      email=request.POST.get('email')
#      datetimep=request.POST.get('meeting-time')
     
#      order.item= Dish.objects.get(pk=question_id).name
#      order.serve_fn= fname
#      order.serve_ln =lname
#      order.email=email
#      order.serve_on= datetimep
#      order.save()
#      context={ 'id':question_id}
#      return render(request,'order_confirmation1.html',context)
     
     

def order_confirmation(request,question_id ):
    # bill details save orderconfirm
     #if request.method =="GET":
        
        try:
            food = Dish.objects.get(pk=question_id)
        
        except Dish.DoesNotExist:
            raise Http404("Question does not exist")
        now = datetime.now()
        
        order= OrderModel()
        order.created_on = now
        order.item= food.name
        order.item_id = food.id
        order.price  = food.price
        order.item_uniq= random.randint(100,999999)
        order.save()
        context={ 'id':food.id}
   
    
        # if request.method == 'POST':
        #     try:
        #         food = Dish.objects.get(pk=question_id)
        #         order.item= Dish.objects.get(pk=question_id).name
            
        #     except Dish.DoesNotExist:
        #         raise Http404("Question id given does not exist")
        #     food = Dish.objects.get(pk=question_id)
        # order=OrderModel.objects.get(price={{food.price}})
                
        orderee= Orderee()
        fname=request.POST.get('fname',False)
        lname=request.POST.get('fname',False)
        email=request.POST.get('email',False)
        datetimep=request.POST.get('meeting-time',False)
        print(fname)
        print(lname)
        print(email)
            
        #     order.item= Dish.objects.get(pk=question_id).name
        orderee.serve_fn= fname
        orderee.serve_ln =lname
        orderee.email=email
        orderee.serve_on= datetimep
        orderee.bill_uniq = order.item_uniq
        orderee.save()
        context={ 'id':question_id}
        
    
            # Going back to previous URL
            
    #return redirect(request.META['HTTP_REFERER'])
    #return HttpResponse("Order has been recorded ")
        return render(request,'order_confirmation.html',context)
    #return HttpResponse('')
    
    
 
# class order_confirmation(View):
    
#       def post(self,request ,question_id,*args, **kwargs):
#           food = Dish.objects.get(pk=question_id)
#           a= request.POST['quantity']
#           b= request.POST['t']
#           now = datetime.now()
#           order= OrderModel()
#           order.created_on = now
#           order.item= food.name
#           order.item_id = food.id
#           order.price  = food.price
#           order.save()
    
          
#           print(a)
#           print(b)
#           context={
#               'quantity' :a ,
#                'id' : b
#           }
#           return render(request,'order_confirmation.html',context)
          
          
#     def get(self,request,*args,**kwargs):
#         #get every item from each category
#         starters =  Dish.objects.filter(category__name__contains ='Starters')
#         maincourse =  Dish.objects.filter(category__name__contains='MainCourse')
#         sweets =  Dish.objects.filter(category__name__contains='Sweets')
#         print(starters)
#         #pass into context
#         context = {
#             'starters'   : starters ,
#              'maincourse': maincourse ,
#              'sweets'    : sweets ,
#         }
        
#         return render(request, 'order.html',context)
    
    
    
#     def post(self, request, *args, **kwargs):
#         order_items= {
#             'items':[]
#         }
#         items= request.POST.getlist('items[]')
        
#         for item in items:
#             menu_item = Dish.objects.get(pk = int(item))
#             item_data= {
                
#                 'id' :menu_item.pk,
#                 'name' : menu_item.name,
#                 'price' :menu_item.price,
#                 'desc' :menu_item.desc,
#                 'time': menu_item.time
                
#             }
            
#             order_items['items'].append(item_data)
            
#             price=0 
#             item_ids =[]
#             for item in order_items['items']:
#                 price += item['price']
#                 item_ids.append(item['id'])
                
#             order= OrderModel.objects.create(price=price)
#             order.items.add(* item_ids)
            
#             body = ('Thank you for your order! Your food is being made and will be delivered soon!\n'
#                 f'Your total: {price}\n'
#                 'Thank you again for your order!')

#             send_mail(
#             'Thank You For Your Order!',
#              body,
#             'anikachawla02@gmail.com',
#             [send_mail],
#             fail_silently=False )

            
#             context = {
#                  'items': order_items['items'] ,
#                  'price': price
                 
#             }
            
#             #return redirect('order-confirmation', pk=order.pk)
            
#             #
#             return render(request,'order_confirmation.html',context)
        
# # def order_confirmation(View):
# #     return render('order-confirmation')
  
    




