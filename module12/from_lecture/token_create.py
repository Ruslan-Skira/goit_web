from jose import jwt

payload = {"sub": "1234567890", "name": "John Doe"}

encoded = jwt.encode(payload, "secret_key", algorithm='HS256')
print('encoded', encoded)

decoded = jwt.decode(encoded, "secret_key", algorithms=['HS256'])
print(f'{decoded=}')
