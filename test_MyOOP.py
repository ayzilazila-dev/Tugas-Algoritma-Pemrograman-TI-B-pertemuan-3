# UJI INHERITANCE

tv = ProdukElektronik("TV", "3.000.000", 2)
roti = ProdukMakanan("Roti", "15.000", "12-12-2026")

print(tv.info_produk())
print(roti.info_produk())


# UJI POLYMORPHISM

notif_email = Email()
notif_sms = SMS()

print(notif_email.kirim())
print(notif_sms.kirim())


# UJI ENCAPSULATION

mhs = Mahasiswa()

print(mhs.set_nilai(85))
print("Nilai mahasiswa:", mhs.get_nilai())

print(mhs.set_nilai(120))