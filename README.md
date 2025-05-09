# 💧 Aplikasi Pembayaran Air – Django Project

Selamat datang di proyek Django pertama saya 
Ini adalah aplikasi web sederhana berbasis **Django + Bootstrap**, dirancang untuk mencatat dan menghitung tagihan pemakaian air pelanggan berdasarkan meteran awal dan akhir.

---

## 📋 Fitur Utama

✅ Input data pelanggan (No. Pelanggan, Nama, Alamat)  
✅ Input data tagihan air (bulan, meter awal, meter akhir)  
✅ Hitung otomatis total tagihan berdasarkan tarif pemakaian  
✅ Tampilan antarmuka responsif menggunakan Bootstrap  
✅ Manajemen data melalui Django Admin  
✅ Simpan data ke database SQLite secara otomatis  

---

## 🧮 Tarif Pemakaian Air

| Pemakaian (m³)         | Tarif (Rp/m³) |
|------------------------|---------------|
| 0 – 10 m³              | 2.500         |
| 11 – 20 m³             | 5.000         |
| 21 – 30 m³             | 7.000         |
| > 30 m³                | 10.000        |

**Total Pemakaian = meter_akhir - meter_awal**

---
