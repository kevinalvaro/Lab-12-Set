#by Kevin Alvaro Adianto

print("""Pilihan:
1. Gabungan (union)
2. Dobel saja (Intersection)
3. Yang hanya ada di A (Difference)
4. hanya yang dobel (Symmetric Difference)
5. Exit""")

pilihan=int(input("Masukkan Pilihan: "))

while pilihan !=5:
    hasil=set()
    if pilihan == 1:
        A=input("Masukkan A: ").split()
        B=input("Masukkan B: ").split()
        A,B=set(A),set(B)
        hasil=A|B
        print("Hasilnya: ",sorted(hasil))

    elif pilihan == 2:
        A=input("Masukkan A: ").split()
        B=input("Masukkan B: ").split()
        A,B=set(A),set(B)
        hasil=A&B
        print("Hasilnya: ",sorted(hasil))

    elif pilihan == 3: 
        A=input("Masukkan A: ").split()
        B=input("Masukkan B: ").split()
        A,B=set(A),set(B)
        hasil=A-B
        print("Hasilnya: ",sorted(hasil))

    elif pilihan == 4: 
        A=input("Masukkan A: ").split()
        B=input("Masukkan B: ").split()
        A,B=set(A),set(B)
        hasil=A^B
        print("Hasilnya: ",sorted(hasil))
    else:
        print("mohon masukkan pilihan antara 1-5") 
    print("""Pilihan:
1. Gabungan (union)
2. Dobel saja (Intersection)
3. Yang hanya ada di A (Difference)
4. hanya yang dobel (Symmetric Difference)
5. Exit""")
    pilihan=int(input("Masukkan Pilihan: "))       