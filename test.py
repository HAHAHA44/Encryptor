# -*- coding:utf-8 -*-
import des
data = "123ssx"
k = des.des(b"DESCRYPT", des.CBC, b"\0\0\0\0\0\0\0\0", pad=None, padmode=des.PAD_PKCS5)
d = k.encrypt(data)
print(str(d).replace('b','',1))
E = ("Encrypted: " + str(d).replace('b','',1))
D = ("Decrypted: " + str(k.decrypt(d)).replace('b','',1))
print (E)
print (D)
# assert (k.decrypt(d) == data)