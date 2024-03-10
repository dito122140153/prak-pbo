class Dagangan:
    total_barang = 0
    daftar_barang = []

    def __init__(self, nama, stok, harga):
        self.__nama = nama
        self.__stok = stok
        self.__harga = harga
        Dagangan.total_barang += 1
        Dagangan.daftar_barang.append((nama, stok, harga))

    def __del__(self):
        Dagangan.total_barang -= 1
        for i, item in enumerate(Dagangan.daftar_barang):
            if item[0] == self.__nama:
                del Dagangan.daftar_barang[i]
                print(f"{self.__nama} telah dihapus dari toko.")
                break

    @classmethod
    def lihat_barang(cls):
        print(f"Jumlah barang dagangan pada toko: {cls.total_barang}")
        for i, item in enumerate(cls.daftar_barang):
            print(f"{i+1}. {item[0]} - Harga: Rp {item[2]} (Stok: {item[1]})")

# Contoh penggunaan:
dagangan1 = Dagangan("Galon Aqua 19L", 32, 17000)
dagangan2 = Dagangan("Gas LPG 5 kg", 22, 88000)
dagangan3 = Dagangan("Beras Ramos 5 kg", 13, 68000)

Dagangan.lihat_barang()

del dagangan1
Dagangan.lihat_barang()
