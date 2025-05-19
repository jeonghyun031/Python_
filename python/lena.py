#1
import struct
def read_bmp(filename):

    with open(filename, 'rb') as f:

        header = f.read(14)

        dib = f.read(40)

 

        magic_bytes = header[0:2]

        magic_number = magic_bytes[::-1].hex().upper()

 

        file_size = struct.unpack('<I', header[2:6])[0]

        file_size_hex = hex(file_size)[2:].upper()

 

        pixel_data_offset = struct.unpack('<I', header[10:14])[0]

 

        width = struct.unpack('<i', dib[4:8])[0]

        height = struct.unpack('<i', dib[8:12])[0]

        bits_per_pixel = struct.unpack('<H', dib[14:16])[0]

        image_size = struct.unpack('<I', dib[20:24])[0]

        h_res = struct.unpack('<i', dib[24:28])[0]

        v_res = struct.unpack('<i', dib[28:32])[0]

        used_colors = struct.unpack('<I', dib[32:36])[0]

        important_colors = struct.unpack('<I', dib[36:40])[0]

 

        print("Type             :", magic_number)

        print("Size             :", file_size_hex)

        print("OffBits          :", pixel_data_offset)

        print("Width            :", width)

        print("Height           :", height)

        print("BitCount         :", bits_per_pixel)

        print("SizeImage        :", image_size)

        print("XpelsPerMeter    :", h_res)

        print("YpelsPerMeter    :", v_res)

        print("ClrUsed          :", used_colors)

        print("ClrImportant     :", important_colors)

 

read_bmp("lena24b_512x512.bmp")

#2

import struct

def flip_bytearray(data, width, height):
    row_size = (width * 3 + 3) & ~3
flipped = bytearray()
    for row in range(height):
        start = row * row_size
        end = start + row_size
        flipped[0:0] = data[start:end]
    return flipped

with open("lena24b_512x512.bmp", "rb") as f:
    header_data = f.read(54)
    width = struct.unpack("<i", header_data[18:22])[0]
    height = struct.unpack("<i", header_data[22:26])[0]
    pixel_data = bytearray(f.read())

row_size = (width * 3 + 3) & ~3

row = 50
col = 50
offset = row * row_size + col * 3

if offset + 2 < len(pixel_data):
    pixel_data[offset] = 0
pixel_data[offset + 1] = 0
pixel_data[offset + 2] = 255

with open("output_dot.bmp", "wb") as f:
    f.write(header_data)
    f.write(pixel_data)

print("Saved modified image with a red dot to output_with_single_dot.bmp")
#3
import struct

def flip_bytearray(data, width, height):
    row_size = (width * 3 + 3) & ~3
flipped = bytearray()
    for row in range(height):
        start = row * row_size
        end = start + row_size
        flipped[0:0] = data[start:end]
    return flipped

with open("lena24b_512x512.bmp", "rb") as f:
    header_data = f.read(54)
    width = struct.unpack("<i", header_data[18:22])[0]
    height = struct.unpack("<i", header_data[22:26])[0]
    pixel_data = bytearray(f.read())

row_size = (width * 3 + 3) & ~3

for row in range(400, 450):
    for col in range(200, 300):
        offset = row * row_size + col * 3
if offset + 2 < len(pixel_data):
            pixel_data[offset] = 0
pixel_data[offset + 1] = 0
pixel_data[offset + 2] = 255

with open("output.bmp", "wb") as f:
    f.write(header_data)
    f.write(pixel_data)

print("Saved modified image to output.bmp")
#4
import struct

def flip_bytearray(data, width, height):
    row_size = (width * 3 + 3) & ~3
flipped = bytearray()
    for row in range(height):
        start = row * row_size
        end = start + row_size
        flipped[0:0] = data[start:end]
    return flipped

with open("lena24b_512x512.bmp", "rb") as f:
    header_data = f.read(54)
    width = struct.unpack("<i", header_data[18:22])[0]
    height = struct.unpack("<i", header_data[22:26])[0]
    pixel_data = bytearray(f.read())

row_size = (width * 3 + 3) & ~3

for col in range(300, 400):
    offset = 300 * row_size + col * 3
if offset + 2 < len(pixel_data):
        pixel_data[offset] = 0
pixel_data[offset + 1] = 255
pixel_data[offset + 2] = 255

for col in range(300, 400):
    offset = 399 * row_size + col * 3
if offset + 2 < len(pixel_data):
        pixel_data[offset] = 0
pixel_data[offset + 1] = 255
pixel_data[offset + 2] = 255

for row in range(300, 400):
    offset = row * row_size + 300 * 3
if offset + 2 < len(pixel_data):
        pixel_data[offset] = 0
pixel_data[offset + 1] = 255
pixel_data[offset + 2] = 255

for row in range(300, 400):
    offset = row * row_size + 399 * 3
if offset + 2 < len(pixel_data):
        pixel_data[offset] = 0
pixel_data[offset + 1] = 255
pixel_data[offset + 2] = 255

with open("output_empty_square.bmp", "wb") as f:
    f.write(header_data)
    f.write(pixel_data)

print("Saved modified image with an empty red square to output_empty_square.bmp")