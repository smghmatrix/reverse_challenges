li = [0x71,0x0a,0x05,0x45,0x01,0x2b,0x5f,0x56,0x00,0x57,0x0d,0x73,0x55,0x07,0x45,0x51,0x2c,0x5f,0x01,0x03,0x51,0x05,0x75,0x0d,0x03,0x10,0x52,0x7b,0x5e,0x50,0x09,0x54,0x55,0x27,0x5a,0x50,0x13,0x07,0x7f,0x58,0x50,0x54,0x02,0x51,0x25,0x08,0x50,0x45,0x52,0x79,0x5a,0x07,0x55,0x0b,0x07,0x24,0x5d,0x04,0x41,0x5d,0x7d,0x5b,0x56,0x54]
text = "FlareOn2024FlareOn2024FlareOn2024FlareOn2024FlareOn2024FlareOn2024"
result = []
result_string = ""
for i in range(len(li)):
    #print(li[i])
    #print(ord(text[i]))
    result.append(li[i] ^ ord(text[i]))
    result_string+= chr(li[i] ^ ord(text[i]))

s = ""
for i in result:
    s+=str(hex(ord(chr(i)))) + " " 

print(result_string)
