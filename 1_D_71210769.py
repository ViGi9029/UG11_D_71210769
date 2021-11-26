a = input("Masukkan String: ")

def cekString(integer):
    try:
        float(integer)
        return True
    except ValueError :
        return False

if a.isnumeric() or cekString(a) :
    a = float(a)
    if((int(a)) % 2) == 0:
        print(int(a/2))
    else:
        print(int(int(a + 5) / 2))
else:
    print(a [::-1])