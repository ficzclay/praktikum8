# Praktikum 8


## Tugas Praktikum

Buat program sederhana dengan mengaplikasikan penggunaan class. Buatlah
class untuk menampilkan daftar nilai mahasiswa, dengan ketentuan:
- Method tambah() untuk menambah data
- Method tampilkan() untuk menampilkan data
- Method hapus(nama) untuk menghapus data berdasarkan nama
- Method ubah(nama) untuk mengubah data berdasarkan nama
- Buat diagram class, flowchart dan penjelasan programnya pada README.md.

### Penjelasan:
Program ini adalah sistem informasi mahasiswa yang mengelola daftar nilai mahasiswa. Berikut adalah penjelasan singkat dari metode-metode dan contoh penggunaan:

1. **tambah(self, nama, nilai)**: Menambahkan data mahasiswa ke dalam daftar nilai dengan bentuk dictionary.
2. **tampilkan(self)**: Menampilkan daftar nilai mahasiswa yang ada dalam daftar.
3. **hapus(self, nama)**: Menghapus data mahasiswa berdasarkan nama.
4. **ubah(self, nama, nilai_baru)**: Mengubah nilai mahasiswa dengan nama dan nilai baru.


Berikut Hasilnya:
![alt text](https://github.com/ficzclay/praktikum8/blob/master/picture/1.png?raw=true)
<br>
Diagram Class:<br>
![alt text](https://github.com/ficzclay/praktikum8/blob/master/picture/2.png?raw=true)
<br>
Flowchart:<br>
![alt text](https://github.com/ficzclay/praktikum8/blob/master/picture/3.png?raw=true)

## Langkah-langkah pengerjaan latihan

1. Konfigurasi terlebih dahulu username dan email pada global repository-nya

```
git config --global user.name “nama_user”
```

```
git config --global user.email “email_user”
```

2. Buat repository local

```
mkdir bahasa_pemrograman
```

```
cd bahasa_pemrograman
```

```
mkdir praktikum8
```

3. Jika sudah, jalankan command (command git init digunakan untuk menginisialisasi repositori git baru)

```
git init
```

## Menambahkan File Baru Pada Repository Lokal

1. Untuk membuat file baru bisa juga dengan text editor

disini akan menggunakan terminal

```
echo “# praktikum8 >> README.md
```

2. Untuk menambahkan file yang baru saja dibuat, gunakan command

```
git add .
```

3. Untuk menyimpan perubahan yang ada pada database repositori
   lokal, gunakan command

```
git commit -m "first commit"
```

## Membuat Repository Server

1. Server repository yang digunakan adalah github
2. Buat akun github terlebih dahulu
3. Klik tombol + new repository
4. Isi nama repository-nya,

```
contoh: praktikum8
```

5. lalu klik tombol Create repository

## Menambahkan Remote Repository

- Remote Repository merupakan server repositori yang akan digunakan untuk menyimpan segala perubahan yang dilakukan pada repositori lokal, dan bisa diakses oleh banyak pengguna
- Untuk menambahkan remote repository server, gunakan command

```
git remote add origin [url]
```

## Mengirim perubahan ke server (Push)

- Untuk mengirim perubahan pada repositori lokal ke server, gunakan command

```
git push -u origin master
```

## Clone Repository

- git clone digunakan untuk mengambil salinan dari repositori Git dari server ke repositori lokal
- gunakan command ini untuk melakukan kloning ke repositori lokal

```
git clone [url]
```
