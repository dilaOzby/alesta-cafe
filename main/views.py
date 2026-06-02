from django.shortcuts import render, redirect
from django.contrib import messages
from .models import DavetTalebi

def index(request):
    return render(request, 'index.html')

def menu(request):
    return render(request, 'menu.html')

def hakkimizda(request):
    return render(request, 'hakkimizda.html')

def davet(request):
    if request.method == 'POST':
        # HTML formundan gelen name değerlerine göre verileri çekiyoruz
        ad_soyad = request.POST.get('ad_soyad')
        telefon = request.POST.get('telefon')
        organizasyon_turu = request.POST.get('organizasyon_turu')
        tarih = request.POST.get('tarih')
        saat_araligi = request.POST.get('saat_araligi')
        kisi_sayisi = request.POST.get('kisi_sayisi')
        alan_tercihi = request.POST.get('alan_tercihi')
        notlar = request.POST.get('notlar')

        # Kişi sayısı boş bırakıldıysa veri tabanına null bassın diye kontrol
        if kisi_sayisi == '':
            kisi_sayisi = None

        # Veri tabanına yeni satır ekleme (SQL INSERT INTO)
        DavetTalebi.objects.create(
            ad_soyad=ad_soyad,
            telefon=telefon,
            organizasyon_turu=organizasyon_turu,
            tarih=tarih,
            saat_araligi=saat_araligi,
            kisi_sayisi=kisi_sayisi,
            alan_tercihi=alan_tercihi,
            notlar=notlar
        )

        # Kullanıcıya başarı bildirimi göndermek için (isteğe bağlı)
        messages.success(request, "Davet talebiniz başarıyla alındı!")
        
        # Formun başarılı gönderiminden sonra sayfayı kendi üzerine yönlendiriyoruz (Post-Redirect-Get pattern)
        return redirect('main:davet')

    return render(request, 'davet.html')

def iletisim(request):
    return render(request, 'iletisim.html')

def rezervasyon(request):
    return render(request, 'rezervasyon.html')