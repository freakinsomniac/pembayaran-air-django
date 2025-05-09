from django import forms
from .models import Pelanggan

class PelangganForm(forms.ModelForm):
    class Meta:
        model = Pelanggan
        fields = ['no_pelanggan', 'nama', 'alamat', 'bulan', 'meter_awal', 'meter_akhir']
