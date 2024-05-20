# Solicita ao usuário que digite o nome de uma cidade
nome_cidade = input("Digite o nome de uma cidade: ")

# Verifica se o nome da cidade começa com 'SANTO' e imprime o resultado
comeca_com_santo = nome_cidade.strip().upper().startswith("SANTO")
print(comeca_com_santo)


