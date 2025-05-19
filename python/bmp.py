#1
import struct

def flip_bytearray(data, width, height):
    row_size = (width * 3 + 3) & ~3
flipped = bytearray()

    for row in range(height):
        start = row * row_size
        end = start + row_size
        flipped.extend(data[start:end])
    return flipped

with open("lena24b_512x512.bmp", "rb") as f:
    header_data = f.read(54)
    img_width = struct.unpack("<i", header_data[18:22])[0]
    img_height = struct.unpack("<i", header_data[22:26])[0]
    pixel_data = bytearray(f.read())

pixels = []
row_size = (img_width * 3 + 3) & ~3

for row in range(img_height):
    start = row * row_size
    end = start + img_width * 3
pixels.append([pixel_data[start:end][i:i + 3] for i in range(0, len(pixel_data[start:end]), 3)])

sample_val = 32

for i in range(0, img_height, sample_val):
    for j in range(0, img_width, sample_val):
        r, g, b = 0, 0, 0
count = 0

for k in range(i, min(i + sample_val, img_height)):
            for l in range(j, min(j + sample_val, img_width)):
                pixel = pixels[k][l]
                r += pixel[0]
                g += pixel[1]
                b += pixel[2]
                count += 1

if count > 0:
            r = r // count
            g = g // count
            b = b // count

        for k in range(i, min(i + sample_val, img_height)):
            for l in range(j, min(j + sample_val, img_width)):
                pixels[k][l] = [r, g, b]

processed_pixel_data = bytearray()
for row in pixels:
    for pixel in row:
        processed_pixel_data.extend(pixel)

with open("output.bmp", "wb") as f:
    f.write(header_data)
    f.write(processed_pixel_data)
#2
from PIL import Image
def quantize_image(img, L):
    pixels = img.load()
    width, height = img.size
    quantization_step = 256 // L
    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y]
            r = (r // quantization_step) * quantization_step
            g = (g // quantization_step) * quantization_step
            b = (b // quantization_step) * quantization_step
            pixels[x, y] = (min(r, 255), min(g, 255), min(b, 255))
    return img
def main():
    img = Image.open("lena24b_512x512.bmp")
    L = int(input("L계수를 입력하세요 (양자화 구간 수): "))
    quantized_img = quantize_image(img, L)
    quantized_img.save(f"lena_quantized_L{L}.bmp", "BMP")
    print(f"이미지가 양자화되어 lena_quantized_L{L}.bmp로 저장되었습니다.")
if __name__ == "__main__":
    main()

#3
from PIL import Image

def main():
    img = Image.open("lena24b_512x512.bmp")
    brightness_percent = float(input("밝기 조절 값을 입력하세요 (+% 또는 -%): "))
    factor = 1 + brightness_percent / 100.0
pixels = img.load()
    width, height = img.size
    for y in range(height):
        for x in range(width):
            r, g, b = pixels[x, y]
            r = int(r * factor)
            g = int(g * factor)
            b = int(b * factor)
            pixels[x, y] = (min(r, 255), min(g, 255), min(b, 255))
    img.save(f"lena_brightness_{int(brightness_percent)}.bmp", "BMP")
if __name__ == "__main__": main()