import hashlib
import time

#t#est = str(time.time()).replace(".", "")

#for i in test:
#    print

#t = (x for x in test)
#print(tuple(t))

#test = str(test).encode("utf-8")
#print(test)
#print(type(test))

#bytes = bytes(test, encoding="raw_unicode_escape")

#print(bytes)
#print(type(bytes))

#m = hashlib.sha256().update(test)
#print(m)
#test = "abcd".encode()
#m = hashlib.sha256().update(test)
#print(m)

#print(m.digest())

#import hashlib
m = hashlib.sha256()
bytes_string = str(time.time()).encode("utf-8")
m.update(bytes_string)
#m.update(b"{}".format(test))
#print(m.hexdigest())
print(m.digest().hex())

