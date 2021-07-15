with open("binary",'bw') as bin_file:
    bin_file.write(bytes(999))

with open("binary", 'br') as bin_file:
    for b in bin_file:
        print(bytes(b))