import sys
import base64

abc = "abcdefghijklmnopqrstuvwxyz"
cipher = sys.argv[1]

after_e5 = base64.decodebytes(cipher.encode()).decode()

after_e4 = "".join([abc[(abc.find(c)-13) % 26] for c in after_e5])

after_e3 = "".join([abc[(abc.find(c)-20) % 26] for c in after_e4])

v_key = 'cryptography'
for i in range(len(after_e3)-len(v_key)):
    v_key += v_key[i % len(v_key)]

after_e2 = "".join([abc[(abc.find(c)-abc.find(v)) % 26] for c, v in zip(after_e3, v_key)])

print(after_e2)

