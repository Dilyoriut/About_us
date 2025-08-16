from django.urls import path
from .views import *


urlpatterns = [
    path('', my_site, name="my_site"),
    path('tdiu/', first_site, name="first_site"),
    path('PDP/', second_site, name="second_site"),
    path('milliy/', third_site, name="third_site"),
    path('tdiu/biva/', tdiu_biva_site, name="biva"),
    path('tdiu/mvmt/', tdiu_mvmt_site, name="mvmt"),
    path('tdiu/M/', tdiu_M_site, name="M"),
    path('PDP/sdap/', PDP_sdap_site, name='sdap'),
    path('PDP/da/', PDP_da_site, name='da'),
    path('PDP/aisaa/', PDP_aisaa_site, name='aisaa'),
    path('milliy/tib/', milliy_tib_site, name="tib"),
    path('milliy/si/', milliy_si_site, name="si"),
    path('milliy/mat/', milliy_mat_site, name="mat"),

]
