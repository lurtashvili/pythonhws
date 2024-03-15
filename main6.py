import wikipediaapi
wiki = wikipediaapi.Wikipedia(language='en', user_agent='test (lizuna.urtashvili@gmail.com)')
z = input("shemoiyvane mosadzebni sityva")
page = wiki.page(z)
print(page.text)