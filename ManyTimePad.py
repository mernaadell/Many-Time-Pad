# Many-Time-Pad
finalsplitted = ""

if __name__ == "__main__":
    hexdec= "AEDE0273C4C0DA3477F919018A05DA71A2530F5A0020E4E0ACA80FF2DE"
    hexdec2 = "A8C80426C2DEC16D31F90D1497129475A45447561D74EEF1B8BF0FFCDC"
    hexdec3 = "A9D30426D3C7CB202EB8050E9717C734A5484A13126CE0FDABA212FBDF"
    hexdec4 = "B49B166FDAC58E2A25F90A159914D134B84E0F551677A7FFB6A512FBC1"
    hexdec5 = "B49B126ED7C5C26D20EA07149D40C771B2555D565373E8F4ADBC07E1D7"
    hexdec6 = "B3DE1763C489DC2822EB0B40970ED134A54942565370E6F6F9A003EAC1"
    # spiltting and printing
    def splitfunction (str) :
        counter = 0
        z = ""
        for i in range(0,len(str)):
            z = z + str[i]
            counter = counter + 1
            if counter == 2 :
                z = z + ' '
                counter = 0

        print z

        final = z.split()
        print final
    splitfunction(hexdec)
    splitfunction(hexdec2)
    splitfunction(hexdec3)
    splitfunction(hexdec4)
    splitfunction(hexdec5)
    splitfunction(hexdec6)
    def strxor(a, b):     # xor two strings (trims the longer input)
     return "".join([chr(ord(x) ^ ord(y)) for (x, y) in zip(a, b)])
   
    def xor(a,b):
      result = int(a, 16) ^ int(b, 16) # convert to integers and xor them together
      return '{:x}'.format(result)
    y=xor(hexdec,hexdec2)
    print(y)
    print("0x20")
  
    z=xor(y,"2020202020202020202020")# detect spaces
    print type(z)
    print("6160655061e1b59460014151d174e040607480c1d540a111417000e0".decode("hex")) #result
    y2=xor(hexdec2,hexdec3)
    print(y2)
    print("0x20")
  
    z2=xor(y2,"2020202020202020202020")# detect spaces
    print type(z2)
    y3=xor(hexdec3,hexdec4)
    print(y3)
    print("0x20")
    print("11b000011190a4d1f41081a00055341011c0d450f180e0c131d1d0703".decode("hex"))
    z3=xor(y3,"2020202020202020202020")# detect spaces
    print type(z3)
    y4=xor(hexdec4,hexdec5)
    print(y4)
    print("0x20")
    print("1d4812490902450a0b410f1b0e0316001d064546041b47021d0700001e".decode("hex"))
    z4=xor(y4,"2020202020202020202020")# detect spaces
    print type(z4)
    y5=xor(hexdec5,hexdec6)
    print(y5)
    print("0x20")
  
    z5=xor(y5,"2020202020202020202020")# detect spaces
    print type(z5)

   
