# 1. EXTRAÇÃO (Extract)
# Nossa lista de utilizadores com saldo positivo
clientes = [
    {
        "name": "Jean Engenheiro",
        "account": {"number": "10001-1", "agency": "0001", "balance": 5200.00, "limit": 2000.00},
        "card": {"number": "**** **** **** 9999", "limit": 5000.0},
        "news": []
    },
    {
        "name": "Aline Tech",
        "account": {"number": "10002-2", "agency": "0001", "balance": 850.00, "limit": 1000.00},
        "card": {"number": "**** **** **** 8888", "limit": 2000.0},
        "news": []
    },
    {
        "name": "Bruno Python",
        "account": {"number": "10003-3", "agency": "0001", "balance": 120.00, "limit": 500.00},
        "card": {"number": "**** **** **** 7777", "limit": 500.0},
        "news": []
    },
    {
        "name": "Carla Dados",
        "account": {"number": "10004-4", "agency": "0001", "balance": 15000.00, "limit": 10000.00},
        "card": {"number": "**** **** **** 6666", "limit": 15000.0},
        "news": []
    },
    {
        "name": "Diego Dev",
        "account": {"number": "10005-5", "agency": "0001", "balance": 2500.00, "limit": 300.00},
        "card": {"number": "**** **** **** 5555", "limit": 1000.0},
        "news": []
    }
]

print("✅ Passo 1 (Extract): Dados extraídos com sucesso!")

# 2. TRANSFORMAÇÃO (Transform)
# Gerando conselhos baseados no saldo de cada um
for cliente in clientes:
    saldo = cliente['account']['balance']
    nome = cliente['name']
    
    if saldo > 10000:
        conselho = f"Olá {nome}, com R$ {saldo} já pode pensar em investimentos globais!"
    elif saldo > 1000:
        conselho = f"Parabéns {nome}! Que tal reforçar a sua reserva de emergência com esses R$ {saldo}?"
    else:
        conselho = f"Oi {nome}, o seu saldo de R$ {saldo} é um ótimo começo para os seus sonhos."
    
    # Adicionando o conselho na caixinha 'news' do cliente
    cliente['news'].append({"message": conselho})

print("✅ Passo 2 (Transform): Mensagens criadas!")

# 3. CARREGAMENTO (Load)
# Exibindo o resultado final na tela
print("\n--- RELATÓRIO FINAL ---")
for cliente in clientes:
    nome = cliente['name']
    # Pegando a mensagem que acabamos de criar lá em cima
    mensagem = cliente['news'][0]['message'] 
    print(f"Cliente: {nome} | Mensagem: {mensagem}")

print("\n🚀 Desafio concluído!")
