from django.urls import URLPattern, path
from . import views

urlpatterns= [ 
    path('',views.index,name='index'),
    path('department',views.department,name='department'),
    path('doctor',views.doctor,name='doctor'),
    path('booking',views.booking,name='booking'),
    path('about',views.about,name='about'),
    path('contact',views.contact,name='contact'),

]