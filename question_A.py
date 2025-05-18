data = [12, 9, 30, "A", "M", 99, 82, "J", "N", "B"]

# Pisahkan huruf dan angka
huruf = [item for item in data if isinstance(item, str)]
angka = [item for item in data if isinstance(item, int)]

# Urutkan masing-masing
huruf.sort()
angka.sort()

# Gabungkan hasilnya
hasil = huruf + angka

# Tampilkan hasil
print(hasil)