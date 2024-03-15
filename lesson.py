import bcrypt

paroli = "password1234"

z = paroli.encode("utf-8")

print(z)
paroli2 = bcrypt.gensalt()
paroli = bcrypt.hashpw(z, paroli2)
print(paroli)
entered_password = "password12345"
entered_password = entered_password.encode("utf-8")
check = bcrypt.checkpw(entered_password, paroli)
print(check)