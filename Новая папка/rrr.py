red = input("введите два числа в формате hex:")
red_len=len(red)
if (red_len<=2):
    print("")
else:
    print("вы ввели больше двух чисел")
    red=input("ведите два числа: ")
r = int(red, 16)

green = input("введите два числа в формате hex:")
green_len=len(green)
if (green_len<=2):
    print("")
else:
    print("вы ввели больше двух чисел")
    green=input("ведите два числа: ")
g = int(green, 16)

blue = input("введите два числа в формате hex:")
blue_len=len(blue)
if (blue_len<=2):
    print("")
else:
    print("вы ввели больше двух чисел")
    blue=input("ведите два числа: ")
b = int(blue, 16)

print(r,g,b)

