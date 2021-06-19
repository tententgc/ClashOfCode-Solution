import math
import sys
def hex_to_rgb(hex_string):
    r_hex = hex_string[1:3]
    g_hex = hex_string[3:5]
    b_hex = hex_string[5:7]
    return int(r_hex,16), int(g_hex,16), int(b_hex,16)


a = input()
z= hex_to_rgb(a)

for i in z:
    print(i)




# c = input()


# print(int(c[1:3], 16))
# print(int(c[3:5], 16))
# print(int(c[5:], 16))
