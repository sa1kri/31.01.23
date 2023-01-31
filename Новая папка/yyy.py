r=int(input("ведите red (0-255): "))
g=int(input("ведите green (0-255): "))
b=int(input("ведите blue (0-255): "))
def rgb(r,g,b):

    if (r<256):
        print("")
    else:
        print("red.ведите число до 256")
        r=int(input("ведите red (0-255): "))
        
    if (r>=0):
        print("r=",r)
    else:
        print("red.ведите число больше 0")
        r=int(input("ведите red (0-255): "))    

    if (g<256):
        print("")
    else:
        print("green.ведите число до 256")
        g=int(input("ведите green (0-255): "))

    if (g>=0):
        print("g=",g)
    else:
        print("green.ведите число больше 0")
        g=int(input("ведите green (0-255): "))
        
    if (b<256):
        print("")
    else:
        print("blue.ведите число до 256")
        b=int(input("ведите blue (0-255): "))
        
    if (b>=0):
        print("b=",b)
    else:
        print("blue.ведите число больше 0")
        b=int(input("ведите blue (0-255): "))

    r = max(0, min(255, r))
    g = max(0, min(255, g))
    b = max(0, min(255, b))
    
    print("#{:02X}{:02X}{:02X}".format(r, g, b))

rgb(r,g,b)