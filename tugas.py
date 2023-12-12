class DaftarNilaiMahasiswa:
    def __init__(self):
        self.daftar_nilai = []

    def tambah(self, nama, nilai):
        data_mahasiswa = {'nama': nama, 'nilai': nilai}
        self.daftar_nilai.append(data_mahasiswa)
        print(f"Data mahasiswa {nama} ditambahkan.")

    def tampilkan(self):
        print("Daftar Nilai Mahasiswa:")
        print("=" * 45)
        for data in self.daftar_nilai:
            print(f"Nama: {data['nama']}, Nilai: {data['nilai']}")

    def hapus(self, nama):
        for data in self.daftar_nilai:
            if data['nama'] == nama:
                self.daftar_nilai.remove(data)
                print(f"Data mahasiswa {nama} dihapus.")
                return
        print(f"Data mahasiswa {nama} tidak ditemukan.")

    def ubah(self, nama, nilai_baru):
        for data in self.daftar_nilai:
            if data['nama'] == nama:
                data['nilai'] = nilai_baru
                print(f"Data mahasiswa {nama} diubah menjadi nilai {nilai_baru}.")
                return
        print(f"Data mahasiswa {nama} tidak ditemukan.")

daftar_nilai_mahasiswa = DaftarNilaiMahasiswa()

# Menambah data mahasiswa
daftar_nilai_mahasiswa.tambah("John", 90)
daftar_nilai_mahasiswa.tambah("Alice", 85)
daftar_nilai_mahasiswa.tambah("Bob", 78)

# Menampilkan daftar nilai mahasiswa
daftar_nilai_mahasiswa.tampilkan()

# Menghapus data mahasiswa
daftar_nilai_mahasiswa.hapus("Alice")

# Menampilkan daftar nilai mahasiswa setelah penghapusan
daftar_nilai_mahasiswa.tampilkan()

# Mengubah nilai mahasiswa
daftar_nilai_mahasiswa.ubah("John", 95)

# Menampilkan daftar nilai mahasiswa setelah perubahan
daftar_nilai_mahasiswa.tampilkan()