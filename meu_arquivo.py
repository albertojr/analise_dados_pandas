import pandas as pd

#importar base de dados
tabela_vendas = pd.read_excel('Vendas.xlsx')

#faturamento por loja
faturamento = tabela_vendas[['ID Loja','Valor Final']].groupby('ID Loja').sum()
print("\n---------FATURAMENTO --------------")
print(faturamento)

#qnt produto por loja
qnt_produto_loja = tabela_vendas[['ID Loja','Quantidade']].groupby('ID Loja').sum()
print("\n---------QUANTIDADE DE PRODUTO POR LOJA --------------")
print(qnt_produto_loja)

#ticket medio por produto em cada loja
#to_frame -> transforma em uma tabela
ticket_medio = (faturamento['Valor Final'] / qnt_produto_loja['Quantidade']).to_frame()

#renomear coluna
ticket_medio = ticket_medio.rename(columns={0 : 'Ticket Médio'})

print("\n---------TICKET MÉDIO--------------")
print(ticket_medio)

#visualizar todas as colunas sem ocultar
# pd.set_option('display.max_columns',None)

