# # my_app.urls
# from django.urls import path
# from .views import first_view, second_view, pages
#
# urlpatterns = [
#     path('',first_view, name='first_page'),
#     path('second/',second_view, name='second_page'),
#     path('pages/<str:page>',pages, name='pages'),
# ]

from django.urls import path
from .views import Univer_sitet,  Toshkent_davlat_iqtisodiyot_universiteti
urlpatterns = [
    path('',Univer_sitet, name='Univer_sitet_page'),
    path('Toshkent_davlat_iqtisodiyot_universiteti/', Toshkent_davlat_iqtisodiyot_universiteti,
         name='Toshkent_davlat_iqtisodiyot_universiteti'),
    path('Toshkent_davlat_iqtisodiyot_universiteti/<str:page>',Toshkent_davlat_iqtisodiyot_universiteti, name='Toshkent_davlat_iqtisodiyot_universiteti'),
]