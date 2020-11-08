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
