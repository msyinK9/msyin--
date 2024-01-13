meme_dict = {
            "CRINGE": "Sesuatu yang sangat aneh atau memalukan",
            "LOL": "Tanggapan umum terhadap sesuatu yang lucu",
            "ROFL":  "tanggapan terhadap lelucon",
            "SHEESH": "sedikit ketidaksetujuan",
            "CREEPY":  "menakutkan, tidak menyenangkan",
            "AGGRO":  "untuk menjadi agresif/marah",
            }
word = input("Masukkan kata : ")
if word in meme_dict.keys():
    print(meme_dict[word])
else:
    print("Tidak ada")
