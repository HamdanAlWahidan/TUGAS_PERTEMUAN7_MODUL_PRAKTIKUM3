### NAMA: HAMDAN AL WAHIDAN
### KELAS: TI. 20. A. 1
### NIM: 312010114

_________________________________________________________________________________


Jadi pada pertemuan ini saya diberikan beberapa tugas oleh dosen saya yaitu diantaranya:

## TUGAS MODUL PRAKTIKUM 3
## LATIHAN 1

![Latihan 1](https://github.com/HamdanAlWahidan/TUGAS_PERTEMUAN7/blob/main/Pertemuan7/latihan2.png) <br>

Di tugas ke dua, saya diminta untuk mencari nilai acak yang bernominal dibawah 0,5. Maka saya memasukan syntax:
```
from random import seed
from random import gauss

seed = int(input("Masukan Nilai N: "))

for i in range(seed):
    value = gauss(0,5)
    print ("Data ke ", i, ":", value)
```

Jika sudah memasukan semua syntax diatas dan telah di run, maka kamu akan mendapatkan tampilan seperti gambar yang ada dibawah ini

![Foto Lat2](https://github.com/HamdanAlWahidan/TUGAS_PERTEMUAN7/blob/main/Lab3/Lab3.png) <br>

___________________________________________________________________________________________________

## LATIHAN 2

![Foto Lat2](https://github.com/HamdanAlWahidan/TUGAS_PERTEMUAN7_MODUL_PRAKTIKUM3/blob/main/Modul%20Praktikum3/latihan%202.png) <br>

Di latihan 2 ini saya di suruh membuat sebuah program dimana ketika kita menginput kan data, outputnya akan mengahasilkan outputan dengan nilai data tersebut merupakan nilai terbesar.

Disini saya menggunakan syntax seperti ini

```
N=int(input("Silahkan Masukan jumlah Bilangan ="))
if N>0:
    i=1
    x=int(input("Masukan Bilangan "+str(i)+"="))
    max=x;total=x
    for i in range(2,N+1):
        x=int (input("Masukan Bilangan "+str(i)+"="))
        total+=x
        if max<x:
            max=x

    print("Bilangan Terbesar =",max)

```

Jika sudah memasukan semua syntax diatas dan telah di run, maka kamu akan mendapatkan tampilan seperti gambar yang ada dibawah ini

![Foto Lat2](https://github.com/HamdanAlWahidan/TUGAS_PERTEMUAN7_MODUL_PRAKTIKUM3/blob/main/Modul%20Praktikum%203/Latihan2.png) <br>


## TUGAS PRAKTIKUM 3

![Foto Lat3](https://github.com/HamdanAlWahidan/TUGAS_PERTEMUAN7_MODUL_PRAKTIKUM3/blob/main/Modul%20Praktikum3/Tugas.png) <br>

Di tugas ini, saya di suruh membuat program INVESTASI.

untuk itu saya menulis syntax seperti ini:

```
print("Program menghitung laba dengan modal 100.000.000")

a = int(input("Masukkan Nilai Uang Yang Ingin Di Investasikan : "))
for x in range(1,9):
    if(x>=1 and x<=2):
        b = a*0
        print("Laba bulan ke-",x," : ",b)
    if(x>=3 and x<=4):
        c = a*0.1
        print("Laba bulan ke-",x," : ",c)
    if(x>5 and x<=7):
        d = a*0.5
        print("Laba bulan ke-",x," : ",d)
    if(x==8):
        e = a*0.5
        print("Laba bulan ke-",x," : ",e)
total=b+b+c+c+d+d+d+e
print("\Total : ",total)

```

Jika sudah memasukan semua syntax diatas dan telah di run, maka kamu akan mendapatkan tampilan seperti gambar yang ada dibawah ini

![Foto Lat2](https://github.com/HamdanAlWahidan/TUGAS_PERTEMUAN7_MODUL_PRAKTIKUM3/blob/main/Modul%20Praktikum%203/Tugas%20Praktikum%203.png) <br>

___________________________________________________________________________________________________
