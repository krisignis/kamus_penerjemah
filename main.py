import time

meme_dict = {
            "CRINGE": "Sesuatu yang sangat aneh atau memalukan",
            "LOL": "Tanggapan umum terhadap sesuatu yang lucu",
            "ROFL": "tanggapan terhadap lelucon",
            "SHEESH": "sedikit ketidaksetujuan",
            "CREEPY": "menakutkan, tidak menyenangkan",
            "AGGRO":"untuk menjadi agresif/marah",
            }

print("Selamat datang di kamus gen z")
time.sleep(1)
for i in range(5):
    
    word = input("Ketik kata yang tidak Kamu mengerti (gunakan huruf kapital semua!): ").upper()
    
    if word in meme_dict.keys():
        print("Makna dari kata", word, "adalah", meme_dict[word])
        # Apa yang harus kita lakukan jika kata itu ditemukan?
    else:
        print("Kata tidak ada di kamus")
        # Apa yang harus kita lakukan jika kata itu tidak ditemukan?
