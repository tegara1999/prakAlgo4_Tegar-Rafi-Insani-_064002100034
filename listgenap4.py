
print  ("@@@@@    @     @@@@  @ ")
print  ("@   @  @   @   @     @ ")
print  ("@@@@@  @ @ @   @@@@  @ ")
print  ("@ @    @   @   @     @ ")
print  ("@   @  @   @   @     @ ")

kok=0
while kok==0:
    k=input('masukan list angka (integer): ')
    # nilai di dalam K yang diberi spasi # 3 5 9
    genap=[]
    ganjil=[]
    for k in k.split():
        if int(k)%2==1:
            
            genap.append(int(k))
            print('list angka tidak memiliki angka genap')
            break

        if int(k)%2==0:
                print('list angka memiliki angka genap')
                break
        else:
            print('tidak terdapat bilangan genap')