"""
Aplikasi deteksi gempa terkini
MODULARISASI DENGAN FUNCTION
MODULARISASI DENGAN PACKAGES
"""
import recentearthquake

if __name__ == '__main__':
    print(f'Aplikasi utama menggunakan package yang memiliki deskripsi {recentearthquake.description}')
    result = recentearthquake.ekstraksi_data()
    recentearthquake.tampilkan_data(result)
