from django.http import HttpResponse


def first_view(request):
    html = """
    <h1>First page</h1>
    <h2>Asosiy bo'lim</h2>
    <a href="second/"> second page >> </a> <br>
    <a href="pages/kompyuterlar"> Computers page >> </a><br>
    <a href="pages/telefonlar"> Telephones page >> </a>
    
    """
    return HttpResponse(html)


def second_view(request):
    html = """
    <h1>Second page</h1>
    <h2>Ikkinchi bo'lim</h2>
     <a href="../"> << first page </a>
    """
    return HttpResponse(html)


def pages(request,page):
    if page == "kompyuterlar":
        html = f"""
        <h1>{page}</h1>
        <p>
        Kompyuter(inglizcha: computer — „hisoblayman“) — oldindan berilgan dastur boʻyicha ishlaydigan avtomatik qurilma. Elektron hisoblash mashinasi (EHM) bilan bir xildagi atama. Biroq, kompyuter hisoblash ishlarini bajarishdan tashqari uning funksiyasi ancha keng. EHMlarning rivojlanishida kompyuter ning bir necha avlodlarini koʻrsatish mumkin. Bu avlodlar element turlari, konstruktiv-texnologik xususiyatlari, mantiqiy tuzilishi, dastur taʼminoti, texnik tafsilotlari, texnikadan foydalanishning qulaylik darajasi bilan bir-biridan farq qiladi. Kompyuterning dastlabki avlodida (Ural-1, Minsk-2, BSEM-2) asosiy element elektron lampa boʻlgani uchun u juda katta joyni egallagan edi. Soʻngra bu lampa oʻrnida tranzistorlar ishlatilgan kompyuter (Razdan-2, M-220, Minsk-22 va boshqalar), integral mikrosxemalar ishlatilgan kompyuter (IBM-360, 1BM-370, (AQSh), YESEVM (Rossiya) va boshqalar, integratsiya darajasi katta boʻlgan integral sxemalar oʻrnatilgan shaxsiy kompyuterlar paydo boʻldi. Shaxsiy kompyuter (mikro va -mikro EHM) tushunchasi 20-asr 70-yillar oxiridan boshlab keng tarqala boshladi. Shaxsiy kompyuterning keyingi avlodlarida mikroelektron va biosxemalardan foydalanildi; ularning hajmi kitob kattaligidek hajmga kichraydi, massasi esa 3,5 kg gacha kamaydi. 1981-yil IBM shirkati shaxsiy kompyuterning yanada takomillashgan modellarini ishlab chikara boshladi. Keyinchalik boshka firmalar IBM bilan PC biriktirilgan kompyuterni, Apple shirkati esa Macintosh (talaffuzi: „Makintosh“) yoki oddiygina „maki“ deb ataladigan kompyuterni yaratishdi. 21-asr boshlarida dunyoda oʻnlab million shaxsiy kompyuterlar, 1 millionga yaqin EHM (shu jumladan, bir necha oʻn superEVM) boʻlgan. Kompyuterlar masalalarni yechishda foydalaniladigan komponentlar (tarkibiy qismlar) tarkibi va tavsifi jihatdan bir-biridan farq qiladi. Murakkab masalalarni yechishda kuchli qurilmalar urnatilgan kompyuterdan, qujjatlarni bosishda harf bosish qurilmasi boʻlgan kompyuterdan foydalaniladi. Istalgan kompyuter tizimlar bloki, monitor va klaviaturadan iborat boʻladi. Kerak boʻlganda boʻlardan tashqari boshqa qurilmalar ham ulanadi. Tizimlar bloki da kompyuterning ishlashi uchun zarur muhim qismlar (diskni yuritkich, vinchester — qattiq disk, mantiqiy amallarni bajaruvchi mikrosxemalar) boʻlib, unga qolgan qurilmalar ulanadi. Monitor (displey) matn va turli tasvir kurinishidagi axborotlarni ekranda aks ettiradi.
        </p>
         <a href="../"> << main page </a>
        """
    elif page == "telefonlar":
        html = f"""
        <h1>{page}</h1>
        <p>Telefon — tovush uzatish va qabul qilish uchun moʻljallangan telekommunikatsiyalar qurilmasidir. Odatda tovushning mexanik energiyasini elektrik signallar energiyasiga aylantirish, masofadan uzatish va uni qaytadan tovushga aylantirish prinsipi bilan ishlaydi.
        Telefon (tele... olis va fon un = olisun) — 1) elektr signallarini tovush signallariga aylantirib beradigan elektrakustik asbob. Elektromagnitli, elektrodinamik va pyezoelektr xillarga bulinadi. Elektromagnitli T. eng keng tarkalgan. Uning asosiy elementlari doimiy magnit, chulgʻamli qutblar va membranadan iborat. Abonent "telefon kilganida" T. signalining oʻzgaruvchan elektr toki taʼsirida membrana tebranib, tovush hosil qiladi. T. telefon apparati, turli radiotexnika a</p>
        <a href="../"> << main page </a>
        """
    else:
        html = f"""
        <h1>{page}</h1>
        """
    return HttpResponse(html)


from django.shortcuts import render
from django.http import HttpResponse


def Univer_sitet(request):
    html = """
    <h1>Universitet e</h1>
    <h2>Asosiy bo'lim</h2>
    <a href="Toshkent_davlat_iqtisodiyot_universiteti/"> National_University_of_Uzbekistan  >> </a><br>
    <a href="PDP/"> PDP>> </a>
    <a href="Jahon_tillari/"> World_languages  >> </a>
    """
    return HttpResponse(html)


def Toshkent_davlat_iqtisodiyot_universiteti(request, page=None):
    if page is None:
        html = f"""
            <a href="Bank_ishi_va_auditi/">  Bank_ishi_va_auditi >> </a><br>
            <a href="Moliyava_moliyaviy_texnologiyalar/"> Moliya_va_moliyaviy_texnologiyalar >> </a><br>
            <a href="Marketing/">Marketing>> </a>
            <a href="../"> << ortga </a>
            """

    elif page == "Bank_ishi_va_auditi":
        html = f"""
            <h1>{page}</h1>
            <p>
            <h1>matematika</h1><br>
            <h1> Ingliz tili</h1>

            </p>

            """
    elif page == "Moliya_va_moliyaviy_texnologiyalar":
        html = f"""
             <h1>{page}</h1>
            <p>
            <h1>matematika</h1><br>
            <h1> Ingliz tili</h1>

            </p>

            """
    else:
        html = f"""
             <h1>{page}</h1>
            <p>
            <h1>matematika</h1><br>
            <h1>Ingliz tili</h1>

            </p>

            """

    return HttpResponse(html)



