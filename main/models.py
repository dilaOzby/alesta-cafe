from django.db import models

class DavetTalebi(models.Model):
    ORGANIZASYON_CHOICES = [
        ('dogum_gunu', 'Doğum Günü'),
        ('evlilik_teklifi', 'Evlilik Teklifi'),
        ('grup_masasi', 'Grup Masası'),
        ('ozel_kutlama', 'Özel Kutlama'),
        ('diger', 'Diğer'),
    ]

    ALAN_CHOICES = [
        ('ic_alan', 'İç Alan'),
        ('acik_alan', 'Açık Alan'),
        ('fark_etmez', 'Fark Etmez'),
    ]

    ad_soyad = models.CharField(max_length=100, verbose_name="Ad Soyad")
    telefon = models.CharField(max_length=20, verbose_name="Telefon")
    organizasyon_turu = models.CharField(max_length=30, choices=ORGANIZASYON_CHOICES, verbose_name="Organizasyon Türü")
    tarih = models.DateField(verbose_name="Tarih")
    saat_araligi = models.CharField(max_length=50, blank=True, null=True, verbose_name="Saat Aralığı")
    kisi_sayisi = models.IntegerField(blank=True, null=True, verbose_name="Kişi Sayısı")
    alan_tercihi = models.CharField(max_length=20, choices=ALAN_CHOICES, blank=True, null=True, verbose_name="Alan Tercihi")
    notlar = models.TextField(blank=True, null=True, verbose_name="Notlar / Özel İstek")
    olusturulma_tarihi = models.DateTimeField(auto_now_add=True, verbose_name="Talep Tarihi")

    def __str__(self):
        return f"{self.ad_soyad} - {self.get_organizasyon_turu_display()} ({self.tarih})"

    class Meta:
        verbose_name = "Davet Talebi"
        verbose_name_plural = "Davet Talepleri"