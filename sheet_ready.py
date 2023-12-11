from openpyxl import load_workbook

wb = load_workbook("data/pivot_table.xlsx")
sheet = wb['Relatorio']

for i in range(2, 6):   
    ano = sheet["A%s" %i].value
    am = sheet["B%s" %i].value 
    bt =  sheet["C%s" %i].value