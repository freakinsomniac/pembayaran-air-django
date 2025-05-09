from django.db import models

class Pelanggan(models.Model):
    no_pelanggan = models.CharField(max_length=10)
    nama = models.CharField(max_length=100)
    alamat = models.TextField()
    bulan = models.CharField(max_length=20)
    meter_awal = models.IntegerField()
    meter_akhir = models.IntegerField()

    def hitung_tagihan(self):
        pemakaian = self.meter_akhir - self.meter_awal
        tagihan = 0

        if pemakaian <= 10:
            tagihan = pemakaian * 2500
        elif pemakaian <= 20:
            tagihan = (10 * 2500) + ((pemakaian - 10) * 5000)
        elif pemakaian <= 30:
            tagihan = (10 * 2500) + (10 * 5000) + ((pemakaian - 20) * 7000)
        else:
            tagihan = (10 * 2500) + (10 * 5000) + (10 * 7000) + ((pemakaian - 30) * 10000)
        return tagihan
