import hashlib
import json

#Lectura JSON
usuarios = {}
file = open("users.json", "r")
usuarios = json.load(file)

for item in usuarios:
    password = item["password"]
    hash_password = hashlib.sha1(password.encode()).hexdigest()
    item["password"] = hash_password

file_hash = open("secure-users.json", "w")
json.dump(usuarios, file_hash, indent=4)





