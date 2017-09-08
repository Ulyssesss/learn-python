import base64

print(base64.b64encode('中文'.encode('utf-8')))
print(base64.b64decode(b'5Lit5paH').decode('utf-8'))

