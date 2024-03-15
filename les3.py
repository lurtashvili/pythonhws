import openpyxl
workbook = openpyxl.Workbook()
y = workbook.active
List = [1,2,3,4,5,6,7,8,9,10]
y.append(List)
workbook.save("exceltest1.xlsx")