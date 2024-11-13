import json
INDICE = 13
SOMA = 0
K = 0

while K < INDICE:
    K += 1
    SOMA += K
    
print(SOMA)


def fibonacci(n):
    if n < 0:
        return False
    a,b = 0, 1
    while a < n:
        a,b = b, a+b
        
    return a == n
        
num = int(input('=>'))

if fibonacci(num):
    print(f'o número {num} que digitou pertcence a sequencia')
else:
    print(f'o número {num} que digitou não pertcence a sequencia')
    
    
def faturamento(simple_json):
    with open(simple_json,'r') as file:
        dados = json.load(file)
    
    faturamento_diario = [item['faturamento'] for item in dados['faturamentos_diarios'] if item['faturamento'] > 0]
    
    if not faturamento_diario:
        return "não há faturamento"
    menor_faturamento = min(faturamento_diario)
    maior_faturamento = max(faturamento_diario)
    
    media_mensal = sum(faturamento_diario) / len(faturamento_diario)
    
    dam = sum(1 for valor in faturamento_diario if valor > media_mensal)
    
    return{
        "menor faturamento": menor_faturamento,
        "maior faturamento": maior_faturamento,
        "dias com faturamento acima da média": dam
    }
    
simple_json = "simple.json"

resultados = faturamento(simple_json)
for chave, valor  in resultados.items():
    print(f'{chave}: {valor}')
    
def faturamento_estado(simple_json):
    with open(simple_json,'r') as file:
        asd = json.load(file)
    
    faturamento_estados = asd['faturamento_estados']
    
    faturamento_total = sum(item['faturamento'] for item in faturamento_estados)
    
    percentuais = {}
    
    for item in  faturamento_estados:
        percentual = (item['faturamento'] / faturamento_total) * 100
        percentuais[item['estado']] = round(percentual, 2)
        
    return percentuais
    
percentuais = faturamento_estado(simple_json)
for estado, percentual in percentuais.items():
    print(f'{estado}: {percentual}%')

def inverter_string(s):
 
    string_invertida = ""
    
    for i in range(len(s)-1, -1, -1):
        string_invertida += s[i]
    
    return string_invertida

entrada = input("Digite uma string para inverter: ")
resultado = inverter_string(entrada)
print(f"A string invertida é: {resultado}")
