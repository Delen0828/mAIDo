import os.path

from Crypto.Util.Padding import pad, unpad
from Crypto.Cipher import AES

key=b'\xc2\xb5a\x87\xb4\x90\xb9\xa7\xb5\x9a\xfc\xa1\x89&\xfa\xbd\xdc\x15\x16\x87\x97\xd8\xfc\x8e\xef\xd5\xd2\x98\xc0yQ7'
iv=b'\xfd\xa2\x1d8\xe9\xc3z3\x1fs\x91$\xc0\xb1\x9a\xc4'


def encrypt(filepath,key,iv):
    in_file = open(filepath, "rb")
    data = in_file.read()
    in_file.close()
    cipher1 = AES.new(key, AES.MODE_CBC, iv)
    ct = cipher1.encrypt(pad(data, 16))
    out_file = open(filepath, "wb")
    out_file.write(ct)
    out_file.close()

def decrypt(filepath,key,iv):
    cipher2 = AES.new(key, AES.MODE_CBC, iv)
    in_file = open(filepath, "rb")
    data = in_file.read()
    in_file.close()
    pt = unpad(cipher2.decrypt(data), 16)
    out_file = open(filepath, "wb")
    out_file.write(pt)

if __name__ == '__main__':
    decrypt(os.path.join(os.getcwd(),'data','task.csv'),key,iv)