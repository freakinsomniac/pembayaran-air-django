from django.shortcuts import render, redirect
from django.shortcuts import render
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
    return render(request, 'pembayaran_web/list.html', {'data': data})
