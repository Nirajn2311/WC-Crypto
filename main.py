import sys
import base64

abc = "abcdefghijklmnopqrstuvwxyz"
cipher = sys.argv[1]

after_e5 = base64.decodebytes(cipher.encode()).decode()

after_e4 = "".join([abc[(abc.find(c)+13) % 26] for c in after_e5])

after_e3 = "".join([abc[(abc.find(c)+(20-1)) % 26] for c in after_e5])

print(after_e3)
