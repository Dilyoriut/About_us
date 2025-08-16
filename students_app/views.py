from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.



def my_site(request):
    http = """"
    <h1 style="text-align: center; color: green;">Asosiy saxifa</h1>
    <h2 style="text-align: center; color: yellow ">Unversitetlar ro'yxati</h2>
    <a href="tdiu/Toshkent_davlat_iqtisodiyot_universiteti"> National_University_of_Uzbekistan page>> </a><br>
    <a href="PDP/PDP"> PDP>> </a> <br>
    <a href="milliy/O’zbekiston milliy universiteti"> O’zbekiston milliy universiteti>> </a>

    """
    return HttpResponse(http)


def first_site(request):
    http = """
    <h1 style="text-align: center; color: green;">Toshkent_davlat_iqtisodiyot_universiteti</h1>
    <a href="biva/">Bank_ishi_va_auditi>> </a><br>
    <a href="mvmt/">Moliya_va_moliyaviy_texnologiyalar>> </a><br>
    <a href="M/">Marketing>> </a><br>
    <a href="../"> << ortga </a>

    """
    return HttpResponse(http)

def tdiu_biva_site(request):
    http = """
     <h2 style="text-align: center; ">Bank ishi va auditi</h2>
     <p style="font-size: 20px;">Yo'nalishiga kirish blok fanlari</p>

     <li style="color: rgb(79, 2, 2); font-size: 20px;">Matematika</li>
     <li style="color: rgb(79, 2, 2); font-size: 20px;">Ing lis tili</li> <br>
     <a href="../"> << ortga </a>


     """

    return HttpResponse(http)


def tdiu_mvmt_site(requsest):
    http = """
     <h2 style="text-align: center; ">Moliya va moliyaviy texnologiyalar</h2>
     <p style="font-size: 20px;">Yo'nalishiga kirish blok fanlari</p>

     <li style="color: rgb(79, 2, 2); font-size: 20px;">Matematika</li>
     <li style="color: rgb(79, 2, 2); font-size: 20px;">Ing lis tili</li> <br>
     <a href="../"> << ortga </a>


    """
    return HttpResponse(http)


def tdiu_M_site(requsest):
    http = """
     <h2 style="text-align: center; ">Marketingr</h2>
     <p style="font-size: 20px;">Yo'nalishiga kirish blok fanlari</p>
     <ol>
        <li style="color: rgb(79, 2, 2); font-size: 20px;">Matematika</li>
        <li style="color: rgb(79, 2, 2); font-size: 20px;">Ing lis tili</li> <br>
     </ol>
     <a href="../"> << ortga </a>


    """
    return HttpResponse(http)


def second_site(request):
    http = """
    <h1 style="text-align: center; color: green;">PDP</h1>
    <a href="sdap/">Software Development and Programming>> </a><br>
    <a href="da/"> Data Analytics>> </a><br>
    <a href="aisaa/">Artificial Intelligence Solutions and Applications>> </a><br>
    <a href="../"> << ortga </a>

    """
    return HttpResponse(http)


def PDP_sdap_site(request):
    http = """
     <h2 style="text-align: center; ">Software Development and Programming</h2>
     <p style="font-size: 20px;">Yo'nalishiga kirish blok fanlari</p>

     <li style="color: rgb(79, 2, 2); font-size: 20px;">Matematika</li>
     <li style="color: rgb(79, 2, 2); font-size: 20px;">Ing lis tili</li> <br>
     <a href="../"> << ortga </a>


     """

    return HttpResponse(http)


def PDP_da_site(requsest):
    http = """
     <h2 style="text-align: center; "> Data Analyticsr</h2>
     <p style="font-size: 20px;">Yo'nalishiga kirish blok fanlari</p>

     <li style="color: rgb(79, 2, 2); font-size: 20px;">Matematika</li>
     <li style="color: rgb(79, 2, 2); font-size: 20px;">Ing lis tili</li> <br>
     <a href="../"> << ortga </a>


    """
    return HttpResponse(http)


def PDP_aisaa_site(requsest):
    http = """
     <h2 style="text-align: center; "Artificial Intelligence Solutions and Applications</h2>
     <p style="font-size: 20px;">Yo'nalishiga kirish blok fanlari</p>
     <ol>
        <li style="color: rgb(79, 2, 2); font-size: 20px;">Matematika</li>
        <li style="color: rgb(79, 2, 2); font-size: 20px;">Ing lis tili</li> <br>
     </ol>
     <a href="../"> << ortga </a>


    """
    return HttpResponse(http)


def third_site(request):
    http = """
    <h1 style="text-align: center; color: blue;">O’zbekiston milliy universiteti</h1>
    <h2 style="text-align: center; ">Bakalavriatura:</h2>
    <ul style="list-style-type: none;">
        <li><a style="text-decoration: none; font-size: 20px;" href="tib/">Tibbiyot fizikasi</a></li><hr>
        <li><a style="text-decoration: none; font-size: 20px;" href="si/">Sun’iy intellekt</a></li><hr>
        <li><a style="text-decoration: none; font-size: 20px;" href="mat/">Matematika</a></li><hr><br>
        <a href="../"> << ortga </a>
    </ul>
    """
    return HttpResponse(http)

def milliy_tib_site(request):
    http = """
    <h1 style="text-align: center; color: blue;">O’zbekiston milliy universiteti</h1>
    <h2 style="text-align: center; ">Tibbiyot fizikasi</h2>
    <p style="font-size: 20px;">Yo'nalishiga kirish blok fanlari</p>
    <ol>
        <li style="color: rgb(79, 2, 2); font-size: 20px;">Matematika</li>
        <li style="color: rgb(79, 2, 2); font-size: 20px;">Biologiya</li>
    </ol>
    <a href="../"> << ortga </a>
    """
    return HttpResponse(http)


def milliy_si_site(request):
    http = """
    <h1 style="text-align: center; color: blue;">O’zbekiston milliy universiteti</h1>
    <h2 style="text-align: center; ">Sun’iy intellekt</h2>
    <p style="font-size: 20px;">Yo'nalishiga kirish blok fanlari</p>
    <ol>
        <li style="color: rgb(79, 2, 2); font-size: 20px;">Matematika</li>
        <li style="color: rgb(79, 2, 2); font-size: 20px;">Fizika</li>
    </ol>
     <a href="../"> << ortga </a>
    """
    return HttpResponse(http)


def milliy_mat_site(request):
    http = """
    <h1 style="text-align: center; color: blue;">O’zbekiston milliy universiteti</h1>
    <h2 style="text-align: center; ">Matematika</h2>
    <p style="font-size: 20px;">Yo'nalishiga kirish blok fanlari</p>
    <ol>
        <li style="color: rgb(79, 2, 2); font-size: 20px;">Matematika</li>
        <li style="color: rgb(79, 2, 2); font-size: 20px;">Fizika</li>
    </ol>
    <a href="../"> << ortga </a>
    """
    return HttpResponse(http)