meme_dict = {
            "CRINGE": "Garip ya da utandırıcı bir şey",
            "LOL": "Komik bir şeye verilen cevap",
            }

for i in range(5):
  print(5 - i, "hakkınız kaldı")
  word = input("Anlamadığınız bir kelime yazın (hepsini büyük harflerle yazın!)")
  if word in meme_dict.keys():
    print("Anlamı:", meme_dict[word])
  else:
    print("Aradığınız kelime bulunmamaktadır.")
