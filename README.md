# Project_UAS

Nama : Muhamad Rizki Wahyu Sapura 
NIM : 312410534
Kelas : TI.24.A.5
Mata Kuliah : Bahasa Pemograman

# Penjelasannya :
1. Kelas Kata
   ![alt text](![Cuplikan layar 2025-01-31 161246](https://github.com/user-attachments/assets/3f44959d-4538-4b1a-8c6a-1e9447b69649)
?raw=true)
   Kelas Data digunakan untuk menyimpan informasi tentang name (nama) dan age (usia). Konstruktor __init__ menginisialisasi dua atribut ini.
   
3. Kelas View
   ![alt text](![Cuplikan layar 2025-01-31 162054](https://github.com/user-attachments/assets/9be3da20-b2c1-4e45-b77b-1a8451a1f1e2)
?raw=true)
   Kelas View memiliki metode statis display_table yang digunakan untuk menampilkan data dalam bentuk tabel. Metode ini mencetak header dan kemudian mencetak data yang ada di data_list dalam format tabel.

4. Kelas Process
   ![alt text](![Cuplikan layar 2025-01-31 162300](https://github.com/user-attachments/assets/d2814cc1-84ab-4e52-983c-425396f7948b)
?raw=true)
   Kelas Process memiliki metode statis get_user_input yang berfungsi untuk mendapatkan input dari pengguna. Metode ini terus meminta input hingga pengguna memberikan nama yang tidak kosong dan usia yang merupakan bilangan bulat positif. Jika terjadi kesalahan, seperti nama kosong atau usia negatif, pesan kesalahan akan ditampilkan dan pengguna akan diminta untuk mencoba lagi.

5. Fungsi Main
   ![alt text](![image](https://github.com/user-attachments/assets/3c76eaf5-7287-4c72-9c42-765b8e1d2668)
?raw=true)
   Fungsi main adalah tempat utama di mana program dijalankan. Fungsi ini menginisialisasi data_list, kemudian terus meminta input pengguna menggunakan metode get_user_input dari kelas Process. Data yang diperoleh ditambahkan ke dalam data_list. Jika pengguna tidak ingin menambahkan data lagi, program berhenti meminta input dan menampilkan data dalam bentuk tabel menggunakan metode display_table dari kelas View.

6. Menjalankan Program
   ![alt text](![Cuplikan layar 2025-01-31 162602](https://github.com/user-attachments/assets/193bf382-7535-486b-b33c-515f07b5abb4)
?raw=true)
   Bagian ini memastikan bahwa fungsi main hanya akan dijalankan jika file ini dijalankan sebagai program utama, bukan diimpor sebagai modul di program lain.

Link Dokumentasi
