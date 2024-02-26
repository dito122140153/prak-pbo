import math

def luaskelilinglingkaran (r):
    if r < 0:
        print ("jari-jari lingkaran tidak boleh negatif")
        return
    
    luas = math.pi * r**2
    keliling = 2 * math.pi * r
    
    print("Luas : ", round(luas, 2))
    print("Keliling : ", round(keliling, 2))
    
r =  float(input("jari-jari : "))

luaskelilinglingkaran (r)
