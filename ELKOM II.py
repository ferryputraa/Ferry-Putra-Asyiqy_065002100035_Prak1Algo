import math

a=input("Masukkan koordinat pertama : ")

p1 = a.split(",")

b=input("Masukkan koordinat kedua : ")

p2 = b.split(",")

jarak = math.sqrt( ((int(p1[0])-int(p2[0]))**2)+((int(p1[1])-int(p2[1]))**2) )

print("Jarak antara ", a,"dan", b, "adalah",jarak)
