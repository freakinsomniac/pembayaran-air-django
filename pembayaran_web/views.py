from django.shortcuts import render, redirect
from .models import Pelanggan
from .forms import PelangganForm

# View untuk menambah pelanggan
def tambah_pelanggan(request):
    if request.method == 'POST':
        form = PelangganForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('daftar_pelanggan')  # Redirect ke daftar pelanggan setelah simpan
    else:
        form = PelangganForm()
    return render(request, 'pembayaran_web/form.html', {'form': form})

# View untuk menampilkan daftar pelanggan
def daftar_pelanggan(request):
    data = Pelanggan.objects.all()  # Ambil semua data pelanggan dari database
    return render(request, 'pembayaran_web/list.html', {'pelanggan_list': data})

def input_pelanggan(request):
    if request.method == 'POST':
        form = PelangganForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            pemakaian = data['meter_akhir'] - data['meter_awal']
            total = 0
            sisa = pemakaian
            tarif_pakai = 0

            # 0-10 m3 pertama
            if sisa > 0:
                pakai = min(sisa, 10)
                total += pakai * 2500
                tarif_pakai = 2500  # Tarif yang dipakai jika hanya di level ini
                sisa -= pakai
            # 11-20 m3 berikutnya
            if sisa > 0:
                pakai = min(sisa, 10)
                total += pakai * 5000
                tarif_pakai = 5000  # Tarif yang dipakai jika sudah masuk level ini
                sisa -= pakai
            # 21-30 m3 berikutnya
            if sisa > 0:
                pakai = min(sisa, 10)
                total += pakai * 7000
                tarif_pakai = 7000  # Tarif yang dipakai jika sudah masuk level ini
                sisa -= pakai
            # >30 m3
            if sisa > 0:
                total += sisa * 10000
                tarif_pakai = 10000  # Tarif yang dipakai jika sudah masuk level ini

            data['selisih_meter'] = pemakaian
            data['tarif'] = tarif_pakai
            data['total_bayar'] = total
            return render(request, 'pembayaran_web/list.html', {'pelanggan': data})
    else:
        form = PelangganForm()
    return render(request, 'pembayaran_web/form.html', {'form': form})
