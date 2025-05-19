#1
from PIL import Image

with Image.open('Dcu.png') as dcuim:
    print("Dcu.png 파일은 " + dcuim.format + " 포맷 이미지입니다.")
with Image.open('sample.bmp') as sampleim:
    print("sample.bmp 파일은 " + sampleim.format + " 포맷 이미지 입니다.")
with Image.open('nuts.jpg') as numim:
    print("nuts.jpg 파일은 "+numim.format + " 포맷 이미지입니다.")
#2
from PIL import Image
import os

def getimage(path):
 with open(path, 'rb') as f:
 magic = f.read(2)

 with Image.open(path) as img:
 width, height = img.size
 channels = len(img.getbands())
 bits = 8 * channels
 raw_size = width * height * channels

 return {
 "Magic number" : magic,
 "File size" : os.path.getsize(path),
 "Width" : width,
 "Height" : height,
 "bits" : bits,
 "Raw size" : raw_size,
 }

file_path = "sample.bmp"
info = getimage(file_path)
for k,v in info.items():
 print(f"{k} : {v}")