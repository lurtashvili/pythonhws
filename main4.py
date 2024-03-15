
Dict = {"Name": "Lizi", "Courses": {"python": 85, "Javascript": 87}}
Dict2 = {101:{"Name": "Lizi", "Courses": {"python": 85, "Javascript": 87}}, 
         102:{"Name": "daviti", "Courses": {"python": 90, "Javascript": 77}}}
print(Dict)
print(Dict["Name"])
print(Dict.get("Courses", {}))
print(Dict["Courses"].get("python"))
print(Dict2[102])
Dict2[101].get("Courses")["python"]=95
print(Dict2[101])
