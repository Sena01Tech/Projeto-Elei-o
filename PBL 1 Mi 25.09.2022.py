# Autor: Luiz Felipe Santana Sena
# Componente Curricular: Algoritmos I
# Concluído em: 25/09/2022
# Declaro que este código foi elaborado por mim de forma individual e não contém
# nenhum trecho de código de colega ou de outro autor, tais como provindos de livros e
# apostilas, e páginas ou documentos eletrônicos da internet. Qualquer trecho de código
# de outra autoria que não a minha está destacado com uma citação do autor e a fonte do
# código, e estou ciente que estes trechos não serão considerados para fins de avaliação.

area_total_Nordeste = 0
area_total_MA = 0
area_total_PI = 0
area_total_BA = 0
area_total_CE = 0
area_total_RN = 0
area_total_PB = 0
area_total_PE = 0
area_total_AL = 0
area_total_SE = 0

arvore_mais_quantidade = ("alo")
arvore_menos_quantidade = ("alo")
area_Cajueiro = 0
area_Mangueira = 0
area_Dendê = 0
area_Coqueiro = 0
area_BambuG = 0
area_Ipê = 0

vezes_MA = 0
vezes_PI = 0
vezes_BA = 0
vezes_CE = 0
vezes_RN = 0
vezes_PB = 0
vezes_PE = 0
vezes_AL = 0
vezes_SE = 0

vezes_contador = 0
vezes_Cajueiro = 0
vezes_Mangueira = 0
vezes_Dendê = 0
vezes_Coqueiro = 0
vezes_BambuG = 0
vezes_Ipê = 0

area_mais_extensa = 0
extenso_codigo = 0
extenso_cidade = 0
extenso_estado = 0
extenso_area = 0
extenso_tipo = ("nenhum")

estado_menos_florestado = ("nenhum")

x = 0
while x == 0:
    codigo = int(input("digite o codigo em numeros para este refloresamento, obs:ele não pode ter sido usado antes"))
    cidade = input("digite a cidade que vai ser reflorestada")
    estado = int(input("digite o numero correspondente ao estado que vai ser reflorestado, 1 para pernabuco, 2 para maranhão, 3 para piaui, 4 para bahia, 5 para ceará, 6 para rio grande do norte, 7 para paraiba, 8 para alagoas, 9 para sergipe"))
    largura = int(input("digite a largura em Metros da aréa que vai ser reflorestada"))
    comprimento = int(input("digite o comprimento em Metros da area que vai ser reflorestada"))
    arvore_usada = int(input("digite o numero correspondente a arvore que vai ser reflorestada, só uma arvore pode ser reflorestada por vez, 1 para cajueiro, 2 para mangueira, 3 para dendê, 4 para coqueiro, 5 para bambu grande, 6 para ipê"))
    area_florestada = (largura)*(comprimento)
    #area florestada mais extensa 
    if area_florestada > area_mais_extensa:
        area_mais_extensa = area_florestada
        extenso_codigo = codigo
        extenso_cidade = cidade
        extenso_estado = estado
        extenso_area = area_mais_extensa
        if arvore_usada == 1:
            extenso_tipo = ("cajueiro")
        elif arvore_usada == 2:
            extenso_tipo = ("mangueira")
        elif arvore_usada == 3:
            extenso_tipo = ("dendê")
        elif arvore_usada == 4:
            extenso_tipo = ("coqueiro")
        elif arvore_usada == 5:
            extenso_tipo = ("bambu grande")
        elif arvore_usada == 6:
            extenso_tipo = ("ipê")

    #Nordeste
    area_total_Nordeste += area_florestada
    #Por estado
    if estado == 1:
        area_total_PE += area_florestada
        vezes_PE += 1
    elif estado == 2:
        area_total_MA += area_florestada
        vezes_MA += 1
    elif estado == 3:
        area_total_PI += area_florestada
        vezes_PI += 1
    elif estado == 4:
        area_total_BA += area_florestada
        vezes_BA += 1
    elif estado == 5:
        area_total_CE += area_florestada
        vezes_CE += 1
    elif estado == 6:
        area_total_RN += area_florestada
        vezes_RN += 1
    elif estado == 7:
        area_total_PB += area_florestada
        vezes_PB += 1
    elif estado == 8:
        area_total_AL += area_florestada
        vezes_AL += 1
    elif estado == 9:
        area_total_SE += area_florestada
        vezes_SE += 1
    #Por tipo de Arvore
    if arvore_usada == 1:
        area_Cajueiro += area_florestada
    elif estado == 2:
        area_Mangueira += area_florestada
    elif estado == 3:
        area_Dendê += area_florestada
    elif estado == 4:
        area_Coqueiro += area_florestada
    elif estado == 5:
        area_BambuG += area_florestada
    elif estado == 6:
        area_Ipê += area_florestada
    #Por vezes mesma arvore
    if arvore_usada == 1:
        vezes_Cajueiro += 1
    elif estado == 2:
        vezes_Mangueira += 1
    elif estado == 3:
        vezes_Dendê += 1
    elif estado == 4:
        vezes_Coqueiro += 1
    elif estado == 5:
        vezes_BambuG += 1
    elif estado == 6:
        vezes_Ipê += 1
    #mais plantado quant
    vezes_contador = vezes_Cajueiro
    arvore_mais_quantidade = ("cajueiro")
    if vezes_Mangueira > vezes_contador:
        vezes_contador = vezes_Mangueira
        arvore_mais_quantidade = ("mangueira")
    if vezes_Dendê > vezes_contador:
        vezes_contador = vezes_Dendê
        arvore_mais_quantidade = ("dendê")
    if vezes_Coqueiro > vezes_contador:
        vezes_contador = vezes_Coqueiro
        arvore_mais_quantidade = ("coqueiro")
    if vezes_BambuG > vezes_contador:
        vezes_contador = vezes_BambuG
        arvore_mais_quantidade = ("Bambu Grande")
    if vezes_Ipê > vezes_contador:
        vezes_contador = vezes_Ipê
        arvore_mais_quantidade = ("Ipê")
    #menos plantado quant
    vezes_contador = vezes_Cajueiro
    arvore_menos_quantidade = ("cajueiro")
    if vezes_Mangueira < vezes_contador:
        vezes_contador = vezes_Mangueira
        arvore_menos_quantidade = ("mangueira")
    if vezes_Dendê < vezes_contador:
        vezes_contador = vezes_Dendê
        arvore_menos_quantidade = ("dendê")
    if vezes_Coqueiro < vezes_contador:
        vezes_contador = vezes_Coqueiro
        arvore_menos_quantidade = ("coqueiro")
    if vezes_BambuG < vezes_contador:
        vezes_contador = vezes_BambuG
        arvore_menos_quantidade = ("Bambu Grande")
    if vezes_Ipê < vezes_contador:
        vezes_contador = vezes_Ipê
        arvore_menos_quantidade = ("Ipê")

    if area_total_MA < area_total_Nordeste:
        estado_menos_florestado = ("Maranhão")
    if area_total_PI < area_total_MA:
        estado_menos_florestado = ("Piaui")
    if area_total_BA < area_total_PI:
        estado_menos_florestado = ("Bahia")
    if area_total_CE < area_total_BA:
        estado_menos_florestado = ("Ceará")
    if area_total_RN < area_total_CE:
        estado_menos_florestado = ("Rio Grande do Norte")
    if area_total_PB < area_total_RN:
        estado_menos_florestado = ("Paraiba")
    if area_total_PE < area_total_PB:
        estado_menos_florestado = ("Pernambuco")
    if area_total_AL < area_total_PE:
        estado_menos_florestado = ("Alagoas")
    if area_total_SE < area_total_AL:
        estado_menos_florestado = ("Sergipe")

    x = float(input("digite 0 se deseja fazer um novo cadastramento, digite 1 se deseja ver o relatório e depois fazer novo recadastramento, ou digite 2 se deseja apenas ver o relatório"))
    if x == 1 :
        #Área total geral reflorestada da Região Nordeste;
        print ("a área total reflorestada do nordeste foi: ", area_total_Nordeste)
        #Área total reflorestada por estado;
        print ("A área total reflorestada do Maranhão foi:", area_total_MA)
        print ("A área total reflorestada do Piaui foi:", area_total_PI)
        print ("A área total reflorestada da Bahia foi:", area_total_BA)
        print ("A área total reflorestada do Ceará foi:", area_total_CE)
        print ("A área total reflorestada do Rio Grande do Norte foi:", area_total_RN)
        print ("A área total reflorestada da Paraiba foi:", area_total_PB)
        print ("A área total reflorestada de Pernanbuco foi:", area_total_PE)
        print ("A área total reflorestada de Alagoas foi:", area_total_AL)
        print ("A área total reflorestada do Sergipe foi:", area_total_SE)
        #Área total reflorestada por cada tipo de árvore;
        print ("A área total reflorestada com Cajueiro foi:", area_Cajueiro)
        print ("A área total reflorestada com Mangueira foi:", area_Mangueira)
        print ("A área total reflorestada com Dendê foi:", area_Dendê)
        print ("A área total reflorestada com Coqueiro foi:", area_Coqueiro)
        print ("A área total reflorestada com Bambu Grande foi:", area_BambuG)
        print ("A área total reflorestada com Ipê foi:", area_Ipê)
        #O tipo de árvore mais usado no reflorestamento e o menos usado (considerando apenas o uso e não a dimensão das áreas reflorestadas);
        print ("O tipo de arvores mais vezes reflorestado foi", arvore_mais_quantidade)
        print ("O tipo de arvores menos vezes reflorestado foi", arvore_menos_quantidade)
        #As informações (código, cidade, estado, área,tipo de árvore) da maior extensão de área reflorestada;
        print ("O codigo da aréa redlorestada mais extensa é ", extenso_codigo)
        print ("A cidade da aréa reflorestada mais extensa é ", extenso_cidade) 
        print ("O Estado da aréa reflorestada mais extensa é ", extenso_estado) 
        print ("O codigo da aréa reflorestada mais extensa é ", extenso_area) 
        print ("O tipo de arvores da aréa mais extensa é ", extenso_tipo) 
        #A quantidade de áreas reflorestadas por estado;
        print ("A quantidade de vezes que o Maranhão foi reflorestado é", vezes_MA) 
        print ("A quantidade de vezes que o Piaui foi reflorestado é", vezes_PI) 
        print ("A quantidade de vezes que o Bahia foi reflorestado é", vezes_BA) 
        print ("A quantidade de vezes que o Ceara foi reflorestado é", vezes_CE) 
        print ("A quantidade de vezes que o Rio Grande do Norte foi reflorestado é", vezes_RN) 
        print ("A quantidade de vezes que o Paraiba foi reflorestado é", vezes_PB) 
        print ("A quantidade de vezes que o Pernanbuco foi reflorestado é", vezes_PE) 
        print ("A quantidade de vezes que Alagoas foi reflorestado é", vezes_AL) 
        print ("A quantidade de vezes que o Sergipe foi reflorestado é", vezes_SE) 
        #O estado menos reflorestado,
        print ("O estado menos reflorestado foi", estado_menos_florestado)
        x = 0
#Área total geral reflorestada da Região Nordeste;
print ("a área total reflorestada do nordeste foi: ", area_total_Nordeste)
#Área total reflorestada por estado;
print ("A área total reflorestada do Maranhão foi:", area_total_MA)
print ("A área total reflorestada do Piaui foi:", area_total_PI)
print ("A área total reflorestada da Bahia foi:", area_total_BA)
print ("A área total reflorestada do Ceará foi:", area_total_CE)
print ("A área total reflorestada do Rio Grande do Norte foi:", area_total_RN)
print ("A área total reflorestada da Paraiba foi:", area_total_PB)
print ("A área total reflorestada de Pernanbuco foi:", area_total_PE)
print ("A área total reflorestada de Alagoas foi:", area_total_AL)
print ("A área total reflorestada do Sergipe foi:", area_total_SE)
#Área total reflorestada por cada tipo de árvore;
print ("A área total reflorestada com Cajueiro foi:", area_Cajueiro)
print ("A área total reflorestada com Mangueira foi:", area_Mangueira)
print ("A área total reflorestada com Dendê foi:", area_Dendê)
print ("A área total reflorestada com Coqueiro foi:", area_Coqueiro)
print ("A área total reflorestada com Bambu Grande foi:", area_BambuG)
print ("A área total reflorestada com Ipê foi:", area_Ipê)
#O tipo de árvore mais usado no reflorestamento e o menos usado (considerando apenas o uso e não a dimensão das áreas reflorestadas);
print ("O tipo de arvores mais vezes reflorestado foi", arvore_mais_quantidade)
print ("O tipo de arvores menos vezes reflorestado foi", arvore_menos_quantidade)
#As informações (código, cidade, estado, área,tipo de árvore) da maior extensão de área reflorestada;
print ("O codigo da aréa redlorestada mais extensa é ", extenso_codigo)
print ("A cidade da aréa reflorestada mais extensa é ", extenso_cidade) 
print ("O Estado da aréa reflorestada mais extensa é ", extenso_estado) 
print ("O codigo da aréa reflorestada mais extensa é ", extenso_area) 
print ("O tipo de arvores da aréa mais extensa é ", extenso_tipo) 
#A quantidade de áreas reflorestadas por estado;
print ("A quantidade de vezes que o Maranhão foi reflorestado é", vezes_MA) 
print ("A quantidade de vezes que o Piaui foi reflorestado é", vezes_PI) 
print ("A quantidade de vezes que o Bahia foi reflorestado é", vezes_BA) 
print ("A quantidade de vezes que o Ceara foi reflorestado é", vezes_CE) 
print ("A quantidade de vezes que o Rio Grande do Norte foi reflorestado é", vezes_RN) 
print ("A quantidade de vezes que o Paraiba foi reflorestado é", vezes_PB) 
print ("A quantidade de vezes que o Pernanbuco foi reflorestado é", vezes_PE) 
print ("A quantidade de vezes que Alagoas foi reflorestado é", vezes_AL) 
print ("A quantidade de vezes que o Sergipe foi reflorestado é", vezes_SE) 
#O estado menos reflorestado,
print ("O estado menos reflorestado foi", estado_menos_florestado)


