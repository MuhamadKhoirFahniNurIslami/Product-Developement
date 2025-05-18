def hitung_huruf_urut(text: str):
    frekuensi = {}

    for char in text:
        if char.isalpha():
            frekuensi[char] = frekuensi.get(char, 0) + 1

    # Urutkan berdasarkan abjad (case-insensitive),
    # tapi tetap pisahkan huruf besar dan kecil
    hasil_urut = sorted(frekuensi.items(), key=lambda x: (x[0].lower(), x[0].isupper()))

    # Format output ke dalam list seperti ["d":1, "e":1, ...]
    output = [f'"{k}":{v}' for k, v in hasil_urut]
    return output

# Pemanggilan
input_user = input("Masukkan teks: ")
hasil = hitung_huruf_urut(input_user)
print(hasil)