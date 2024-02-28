import json
import pandas as pd

usuarios = {}
file = open("secure-users.json", "r")
usuarios = json.load(file)

users_id = []
for item in usuarios:
      id = item["userId"]
      users_id.append(id)

passwords = []
for item in usuarios:
    password = item["password"]
    passwords.append(password)

df = pd.DataFrame({'ID': users_id, 'Contraseñas': passwords})
df.to_excel("usuarios.xlsx")



