import os
import base64
s = os.environ.get('pwd')

t = base64.b64encode(s.encode())
print('s:',s)
print('t:',t)
