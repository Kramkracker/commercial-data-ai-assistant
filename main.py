
# Primeiro programa do projeto Commercial Data AI Assistant

vendas = [
    {"produto": "Produto A", "valor": 1500},
    {"produto": "Produto B", "valor": 2300},
    {"produto": "Produto C", "valor": 1800},
]

total = sum(venda["valor"] for venda in vendas)
media = total / len(vendas)

print("RELATÓRIO COMERCIAL")
print(f"Total de vendas: R$ {total:,.2f}")
print(f"Venda média: R$ {media:,.2f}")
