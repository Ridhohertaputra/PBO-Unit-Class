class Mahasiswa:
    # Fungsi untuk menginisiasi class Mahasiswa
    def __init__(self, nama, npm, jurusan):
        self.nama = nama
        self.npm = npm
        self.jurusan = jurusan
    
    # Fungsi untuk menampilkan informasi dari Mahasiswa yang diinput
    def tampilkan_info(self):
        print("Nama: ", self.nama)
        print("NPM: ", self.npm)
        print("Jurusan: ", self.jurusan.NamaJurusan)

class Jurusan:
    # Fungsi untuk menginisiasi class Jurusan
    def __init__(self, nama_jurusan):
        self.NamaJurusan = nama_jurusan
        self.DaftarMahasiswa = []
    
    # Fungsi untuk menambah objek mahasiswa ke dalam class jurusan
    def tambah_mahasiswa(self, mahasiswa):
        self.DaftarMahasiswa.append(mahasiswa)
    
    # Fungsi untuk menampilkan daftar mahasiswa yang ada di dalam jurusan yang diinginkan
    def tampilkan_daftar_mahasiswa(self):
        print("-----------------------")
        print("Daftar Mahasiswa di Jurusan", self.NamaJurusan, ":")
        for mahasiswa in self.DaftarMahasiswa:
            print("Nama : ", mahasiswa.nama)
            print("NPM : ", mahasiswa.npm)
            print("-----------------------")

class Universitas:
    # Fungsi untuk menginisiasi class Universitas
    def __init__(self, nama_universitas):
        self.NamaUniversitas = nama_universitas
        self.DaftarJurusan = []
    
    # Fungsi untuk menambahkan jurusan ke dalam objek universitas
    def tambah_jurusan(self, jurusan):
        self.DaftarJurusan.append(jurusan)
    
    # Fungsi untuk menampilkan daftar jurusan yang ada di dalam Universitas
    def tampilkan_daftar_jurusan(self):
        print("Daftar Jurusan di Universitas", self.NamaUniversitas, ":")
        for jurusan in self.DaftarJurusan:
            print(jurusan.NamaJurusan)

# Buat objek Universitas dengan nama "XYZ University"
universitas = Universitas("XYZ University")

# Buat objek Jurusan dengan nama "Teknik Informatika" dan tambahkan ke dalam Universitas XYZ.
jurusan_TI = Jurusan("Teknik Informatika")
universitas.tambah_jurusan(jurusan_TI)

# Buat objek Jurusan dengan nama "Manajemen Bisnis" dan tambahkan ke dalam Universitas XYZ.
jurusan_mb = Jurusan("Manajemen Bisnis")
universitas.tambah_jurusan(jurusan_mb)

# Buat objek Jurusan dengan nama "Sastra Inggris" dan tambahkan ke dalam Universitas XYZ.
jurusan_sastra = Jurusan("Sastra Inggris")
universitas.tambah_jurusan(jurusan_sastra)

# Buat objek Jurusan dengan nama "Arkeologi" dan tambahkan ke dalam Universitas XYZ.
jurusan_arkeologi = Jurusan("Arkeologi")
universitas.tambah_jurusan(jurusan_arkeologi)

# Buat objek Jurusan dengan nama "Akuntansi" dan tambahkan ke dalam Universitas XYZ.
jurusan_akuntansi = Jurusan("Akuntansi")
universitas.tambah_jurusan(jurusan_akuntansi)

# Buat objek Mahasiswa dengan nama "Ridho Herta Putra", NPM "G1A022061", dan masukkan ke dalam Jurusan Teknik Informatika di XYZ University.
mahasiswa = Mahasiswa("Ridho Herta Putra", "G1A022061", jurusan_TI)
jurusan_TI.tambah_mahasiswa(mahasiswa)

# Tampilkan daftar jurusan yang ada di Universitas XYZ.
universitas.tampilkan_daftar_jurusan()

# Tampilkan daftar mahasiswa yang terdaftar dalam Jurusan Teknik Informatika di Universitas XYZ.
jurusan_TI.tampilkan_daftar_mahasiswa()
