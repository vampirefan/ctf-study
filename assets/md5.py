import hashlib

for i in range(32, 127):
    for j in range(32, 127):
        for k in range(32, 127):
            s = "TASC" + chr(i) + "O3RJMV" + chr(j) + "WDJKX" + chr(k) + "ZM"
            m = hashlib.md5()
            m.update(s.encode())  # Python 3 要先 encode 成 bytes
            des = m.hexdigest()
            if "e9032" in des and "da" in des and "911513" in des:
                print("Match found!")
                print("Input string:", s)
                print("MD5 hash:    ", des)
