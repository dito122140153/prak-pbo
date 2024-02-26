def penjumlahanganjil(bawah,atas):
  if bawah < 0 or atas < 0 :
    print("Batas bawah dan atas yang dimasukan tidak boleh dibawah Nol")

  jumlahganjil = 0
  for i in range (bawah, atas):
    if i % 2 != 0:
      print(i)
      jumlahganjil+=1
      return jumlahganjil

bawah = int(input("batas bawah : "))
atas = int(input("batas atas : "))

jumlahganjil = penjumlahanganjil(bawah, atas)
print("Total : ",jumlahganjil)
