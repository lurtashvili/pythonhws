import csv
import os
directory = "C:/Users/liziu/Downloads/New folder (8)"
path = os.path.join(directory, 'txt.csv')
while True:
    info = input("""
                    1.chaweret informacia
                    2.waikitxet informacia
                    3.dasruleba""")
    if info == "3":
        print("dasrulebulia")
        break
    elif info == "2":
        with open(path) as f:
            z = csv.reader(f)
            for i in z:
                print(i)
            input("daawiret rames gasagrdzeleblad")
    elif info == "1":
        name = input("your name: ")
        age = input("your age: ")
        country = input("your country: ")
        list = [name, age, country]
        with open(path, "a") as file:
            x = csv.writer(file)
            x.writerow(list)
            print("your information has been saved succesfully")
            input("daawiret rames rom gaagrdzelot")

    