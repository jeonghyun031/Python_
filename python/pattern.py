#1-1
import os
import random

def gen_file(file_path,file_size=50*1024*1024, pattern=b'\xDE\xAD\xBE\xEF', insert_count=10):
  with open(file_path,"wb") as file:
    file.write(os.urandom(file_size))

    for __ in range(insert_count):
      position = random.randint(0,file_size)
      file.seek(position)
      file.write(pattern)

gen_file("large_data.bin",file_size=50*1024*1024,insert_count=10)
#1-2
def find_binary_pattern(file_path,pattern):
  position=[]
  offset=0

  with open(file_path,"rb") as file:
    while True:
      chunk = file.read(4096)
      if not chunk:
        break

      for i in range(len(chunk) - len(pattern) + 1):
          if chunk[i:i + len(pattern)] == pattern:
              position.append(offset + i)
             
      offset += len(chunk)

  return position
positions = find_binary_pattern("large_data.bin", b'\xDE\xAD\xBE\xEF')
print("패턴 찾기...")
print("총 {}회 발견됨.".format(len(positions)))
print("발견된 위치: {}".format(positions))
#2
import os

def generate_random_binary_file(file_path, size=1024):
    with open(file_path, "wb") as f:
        f.write(os.urandom(size))

def xor_encrypt(input_file, key, output_file):

    with open(input_file, "rb") as infile, open(output_file, "wb") as outfile:
        while True:
            chunk = infile.read(4096)
            if not chunk:
                break
            encrypted_chunk = bytes([b ^ key for b in chunk])
            outfile.write(encrypted_chunk)

generate_random_binary_file("secret_data.bin", 2048)

xor_encrypt("secret_data.bin", 0x7A, "encrypted_data.bin")
xor_encrypt("encrypted_data.bin", 0x7A, "decrypted_data.bin")

input_file = input("input file : ")
output_file = input("output file : ")
key = int(input("input XOR key(0~255) : "))

xor_encrypt(input_file, key, output_file)
#3
def split_binary_file(file_path, chunk_size=5*1024*1024):

    part_num = 1
    with open(file_path, "rb") as infile:
        while True:
            chunk = infile.read(chunk_size)
            if not chunk:
                break

            output_file_name = f"part_{part_num}.bin"  

            with open(output_file_name, "wb") as outfile:
                outfile.write(chunk)
           
            part_num += 1

if __name__ == "__main__":
    large_file_path = "large_data.bin"
    split_binary_file(large_file_path)