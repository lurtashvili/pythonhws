def text_to_list(file_name):
    List = []
    x = open(file_name)
    z = x.readlines()
    for i in z:
        List.append(i)  
    Set = set(List)
    y = sorted(list(Set))
    print(y)
text_to_list("txt1.txt")



def text_to_list_2(file_name):
    List = []
    with open(file_name) as f:
        for line in f:
            linee = line.strip()
            List.append(linee)
    return List
print(text_to_list_2("txt1.txt"))


