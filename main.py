import os
import base64
s = os.environ.get('pwd')

t = base64.b64encode(s.encode())
print('s?',s == r"P\\bb|n4\I4;_HWG/tr'tUH3")
print('base64?',t == b'UFxcYmJ8bjRcSTQ7X0hXRy90cid0VUgz')
