import math

def luaskelilinglingkaran (r):
    if r < 0:
        print ("jari-jari lingkaran tidak boleh negatif")
        return
    
    luas = math.pi * r**2
    keliling = 2 * math.pi * r
    
    print("Luas : ", luas)
    print("Keliling : ", keliling)
    
r =  float(input("jari-jari : "))

luaskelilinglingkaran (r)
