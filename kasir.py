#import modul
import pandas as pd
from tabulate import tabulate

'''
Menginisialisasi kelas Transaction untuk menampung dictionary.
Mengecek apakan input dictionary sudah benar.
'''
class Transaction:
    def __init__(self):
        self.list_item = {}
        self.input = True

    '''
    Membuat method add item untuk :
    - Menyimpan name, quantity, dan price ke dictionary.
    - Menambahkan item lain ke dictionary
    '''
    def add_item(self, name, qty, price):
        dict_add = {name: [qty, price]}
        self.list_item.update(dict_add)
        print(f"Item yang dibeli adalah: {self.list_item}.")
    
    '''
    Membuat update nama dari item
    Memperbarui dan menampilkan dictionary terbaru
    '''
    def update_item_name(self, name, new_name):
        input_name = self.list_item[name]
        self.list_item.pop(name)
        self.list_item.update({new_name: input_name})
        #menampilkan data pesanan setelah terjadi perubahan
        print(self.list_item)
    
    '''
    Membuat update jumlah/quantity dari item
    Mengecek inputan customer benar atau salah(inputan quantity harus berupa integer)
    Memperbarui dan menampilkan dictionary terbaru
    '''
    def update_item_qty(self, name, new_qty):    
        if type(new_qty)!=int:
            print("Jumlah barang harus berupa angka!")
        else:
            self.list_item[name][0] = new_qty
            print(self.list_item)
    
    '''
    Membuat update price dari item
    Mengecek inputan customer benar atau salah(inputan price harus berupa integer)
    Memperbarui dan menampilkan dictionary terbaru
    '''
    def update_item_price(self, name, new_price):       
        if type(new_price)!=int:
            print("Harga barang harus berupa angka!")
        else:
            self.list_item[name][1] = new_price
            print(self.list_item)
    
    '''
    Membuat method delete item untuk menghapus item dari pesanan
    Mengecek apakah item ada di dalam pesanan
    '''
    def delete_item(self, name):
        try:
            self.list_item.pop(name)
            print(f"Menghapus pesanan {name}.")
            print(self.list_item)
        except KeyError:
            print(f"{name} tidak ada dalam daftar pesanan.")
        
    '''
    Membuat method reset transaction untuk menghapus semua item dari pesanan
    '''
    def reset_transaction(self):
        self.list_item = self.list_item.clear
        print("Semua item berhasil dihapus.")
    
    '''
    Membuat method print item untuk menampilkan tabel pesanan
    '''
    def print_item(self):
        try:
            table_item = pd.DataFrame(self.list_item).T
            headers = ["Nama Item", "Jumlah Item", "Harga/Item", "Total Harga"]
            print(tabulate(table_item, headers, tablefmt="github"))
        except:
            print("Belum ada pemesanan.")
            
    '''
    Menampilkan semua pesanan berupa tabel
    Menghitung total diskon dan total belanja
    '''     
    def total_price(self):
        self.print_item()
        total_belanja = 0
        for item in self.list_item:
            total_belanja += self.list_item[item][1] 

        if total_belanja>500_000:
            diskon = int(total_belanja*0.1)
            total_belanja = int(total_belanja-diskon)
            print(f"Selamat, Anda mendapatkan diskon 10% sebesar Rp {diskon}.")        
            print(f"Total belanja Anda adalah Rp {total_belanja}.")

        elif total_belanja>300_000:
            diskon = int(total_belanja*0.08)
            total_belanja = int(total_belanja-diskon)
            print(f"Selamat, Anda mendapatkan diskon 10% sebesar Rp {diskon}.")        
            print(f"Total belanja Anda adalah Rp {total_belanja}.")

        elif total_belanja>200_000:
            diskon = int(total_belanja*0.05)
            total_belanja = int(total_belanja-diskon)
            print(f"Selamat, Anda mendapatkan diskon 10% sebesar Rp {diskon}.")        
            print(f"Total belanja Anda adalah Rp {total_belanja}.")

        else:
            print(f"Total belanja Anda adalah Rp {total_belanja}.")
