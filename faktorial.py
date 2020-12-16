import os

def faktorial(angkaNya):
	hasil = 1
	for x in range(1, int(angkaNya)+1): hasil*=x
	return hasil

isi = input(" Masukkan Angka: ")
print(" Hasil Faktorial dari '{}' = '{}'".format(isi, faktorial(isi)))