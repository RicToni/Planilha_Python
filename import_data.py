import pandas as pd

data = pd.read_excel('C:/Users/RT/Desktop/Ric/Estudos/Python-OBC-MiniCurso/Projeto-Planilha/data/VendaCarros.xlsx')
df = data[["Fabricante", "ValorVenda", "Ano"]]

pivot_table = df.pivot_table(
    index="Ano",
    columns="Fabricante",
    values="ValorVenda"
)

pivot_table.to_excel('data/pivot_table.xlsx', 'Relatorio')

print(pivot_table) 