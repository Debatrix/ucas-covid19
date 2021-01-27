import os
import base64
s = os.environ.get('a')

t = base64.b64encode(s.encode())
print(s)
print(t)
