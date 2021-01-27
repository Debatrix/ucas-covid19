import os
import base64
s = os.environ.get('pwd')

t = base64.b64encode(s.encode())
print(t == b'UFxcYmJ8bjRcSTQ7X0hXRy90cid0VUgz')
