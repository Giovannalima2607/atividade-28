# Função para encontrar produtos com estoque zerado
def produtos_em_estoque_zerado(produtos, estoque):
    # Lista para armazenar produtos com estoque zerado
    produtos_zerados = []
    
    # Verifica cada produto e seu respectivo estoque
    for produto, quantidade in zip(produtos, estoque):
        if quantidade == 0:
            produtos_zerados.append(produto)
    
    # Retorna os produtos com estoque zerado
    return produtos_zerados

# Listas de exemplo
produtos = ['Arroz', 'Feijão', 'Macarrão', 'Açúcar', 'Sal']
estoque = [10, 0, 5, 0, 20]

# Chamando a função
produtos_zerados = produtos_em_estoque_zerado(produtos, estoque)

# Exibindo o resultado
if produtos_zerados:
    print("Produtos com estoque zerado:", ', '.join(produtos_zerados))
else:
    print("Nenhum produto com estoque zerado.")