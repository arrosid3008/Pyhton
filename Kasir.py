import random

def kasir_toko_baju():
    total_pembelian = 0
    struk_pembelian = []

    harga_per_item = {
        "Baju Koko" : 100000,
        "Kaos" : 50000,
        "Celana Jeans" : 200000,
        "Celana Pendek" : 50000,
        "Item random 1": random.randint(30000,300000),
    }

    while True:
        print("\nDaftar Item:")
        for item, harga in harga_per_item.items():
            print(f"{item}:Rp {harga}")

        item = input("Masukan nama item (Ketik 'selesai' untuk mengakhiri): ")
        if item.lower() =='selesai':
            break

        if item in harga_per_item:
            harga = harga_per_item[item]
        else:
            harga = random.randint(30000,300000)

        jumlah = int(input("Masukan Jumlah item yang di beli: "))
        total_item = harga * jumlah
        total_pembelian += total_item

        struk_pembelian.append((item, harga, jumlah, total_item))

        print("\n===== Struk Pembelian =====")
        print("Nama Toko: Semoga Jaya Fashion")
        print("No Telp: 02137681")
        print("\n{:<20} {:<10} {:<10} {:<10}".format("Item", "Harga", "Jumlah", "Total"))
        print("=" * 50)

        for item, harga, jumlah, total_item in struk_pembelian:
            print("\n{:<20} {:<10.2f} {:<10} {:<10.2f}".format(item, harga, jumlah, total_item))

        print("=" * 50)
        print("Total Pembelian: Rp {:.2f}".format(total_pembelian))