"""
Aplikasi deteksi gempa terkini
MODULARISASI DENGAN FUNCTION
"""


def ekstraksi_data():
    """
    Tanggal: 12 Maret 2023
    Waktu: 20:26:25 WIB
    Magnitudo: 2.5
    Kedalaman: 8 km
    Lokasi: LS=2.5 BT=140.68
    Pusat Gempa: Pusat gempa berada di darat 6 km baratlaut Kota Jayapura
    Dirasakan: Dirasakan (Skala MMI): II Kota Jayapura
    :return:
    """
    hasil = dict()
    hasil['tanggal'] = '12 Maret 2023'
    hasil['waktu'] = '20:26:25 WIB'
    hasil['magnitudo'] = 2.5
    hasil['kedalaman'] = 8
    hasil['lokasi'] = {'ls': 2.5, 'bt': 140.68}
    hasil['pusat_gempa'] = 'Pusat gempa berada di darat 6 km baratlaut Kota Jayapura'
    hasil['dirasakan'] = 'Dirasakan (Skala MMI): II Kota Jayapura'
    return hasil


def tampilkan_data(result):
    print('Gempa terakhir berdasarkan BMKG')
    print(f"Tanggal {result['tanggal']}")
    print(f"Waktu {result['waktu']}")
    print(f"Magnitudo {result['magnitudo']}")
    print(f"Kedalaman {result['kedalaman']} km")
    print(f"Lokasi: LS={result['lokasi']['ls']}, BT={result['lokasi']['bt']}")
    print(f"Pusat Gempa {result['pusat_gempa']}")
    print(f"Dirasakan {result['dirasakan']}")


if __name__ == '__main__':
    print('Aplikasi utama')
    result = ekstraksi_data()
    tampilkan_data(result)
