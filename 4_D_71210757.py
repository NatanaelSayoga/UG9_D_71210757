n = int(input("suku yang ingin kita cari adalah suku ke: "))
a = float(input("masukkan nilai suku pertama deret geometri: "))
b = float(input("masukkan sembarang nilai dari 2 suku berurutan deret geometri, suku pertama: "))
c = float(input("suku kedua: "))
r = float(c/b)
un = float(a*r**(n-1))
sum = float((a*((r**n)-1))/(r-1))
print("jumlah suku ke-" + str(n) + " adalah " +str(un))
print("jumlah " +str(n)+ " suku pertama adalah " +str(sum))