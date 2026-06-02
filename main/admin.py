from django.contrib import admin
from .models import DavetTalebi

@admin.register(DavetTalebi)
class DavetTalebiAdmin(admin.ModelAdmin):
    # Admin panelinde hangi sütunların görüneceğini seçiyoruz
    list_display = ('ad_soyad', 'telefon', 'organizasyon_turu', 'tarih', 'kisi_sayisi', 'olusturulma_tarihi')
    
    # Sağ tarafa filtreleme kutusu ekliyoruz
    list_filter = ('organizasyon_turu', 'tarih', 'alan_tercihi')
    
    # Arama çubuğu ekliyoruz (İsimle veya telefonla arama yapmak için)
    search_fields = ('ad_soyad', 'telefon', 'notlar')