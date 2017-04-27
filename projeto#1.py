print("Bem vindo ao Quiz de Conhecimentos Gerais!!!")
p=0
q1=input("Primeira pergunta onde se localiza o arco do triunfo: A.Alemanha   B.França   C.China ")
if q1=="a" or q1=="A":
    p=p+3
else:
    if q1=="b" or q1=="B":
        p=p+5
    else:
        if q1=="c" or q1=="C":
            p=0
q2=input("Onde estão localizadas as usinas nucleares do Brasil: A.Angra dos reis   B.Baía da Guanabara   C.Rio Paraguai ")
if q2=="A" or q2=="a":
    p=p+5
else:
    if q2=="B" or q2=="b":
        p=p+3
    else:
        if q2=="c" or q2=="C":
            p=p+0
q3=input("Qual das unidades é usada para medir calor: A.Celsius/Joule   B.Celsius/Caloria   C.Byte/Joule ")
if q3=="c" or q3=="C":
    p=p+0
else:
    if q3=="a" or q3=="A":
        p=p+5
    else:
        if q3=="B" or q3=="b":
            p=p+3
q4=input("A lei da inercia foi criada por: A.Galileu   B.Steve Jobs   C.Newton ")
if q4=="a" or q4=="A":
    p=p+3
else:
    if q4=="b" or q4=="B":
        p=p+0
    else:
        if q4=="c" or q4=="C":
            p=p+5
q5=input("Quanto é x+2+3=11? A.5   B.6   C.0 ")
if q5=="A" or q5=="a":
    p=p+5
else:
    if q5=="B" or q5=="b":
        p=p+3
    else:
        if q5=="C" or q5=="c":
            p=p+0
q6=input("7²+7¹=7³:A.Correto   B.Incorreto ")
if q6=="A" or q6=="a":
    p=p+0
else:
    if q6=="B" or q6=="b":
        p=p+5
q7=input("Na tabela periodica o Fosforo tem qual sigla: A.Fo   B.Zn   C.P ")
if q7=="A" or q7=="a":
    p=p+3
else:
    if q7=="B" or q7=="b":
        p=p+0
    else:
        if q7=="c" or q7=="C":
            p=p+5
q8=input("Qual substancia não é um acido: A.Laranja  B.Hcl  C.Oxigenio ")
if q8=="C" or q8=="c":
    p=p+5
else:
    p=p+0
q9=input("A sequência da conversão de um sinal analógico para digital é: A.Codificação,amostragem,quantização   B.Hackiar,programar,codificar   C.Amostragem, quantização, codificação. " )
if q9=="c" or q9=="C":
    p=p+5
else:
    if q9=="A" or q9=="a":
        p=p+3
    else:
        if q9=="b" or q9=="B":
            p=p+0
q10=input("Qual o Sistema Numérico que o computador adota? A.Binario   B.Octadecimal   C.Inteiro ")
if q10=="A" or q10=="a":
    p=p+5
else:
    if q10=="b" or q10=="B":
        p=p+3
    else:
        if q10=="c" or q10=="C":
            p=p+0
if p==50:
    print("Parabéns!!! Você acertou T U D O")
else:
    if p>40:
        print("Você quase acertou tudo")
    else:
        if p>20:
            print("Seu desempenho não foi bom")
        else:
            if p>10:
                print("Você errou quase tudo")
            else:
                if p==0:
                    print("Você errou TUDO")
print("Pontuação final",p)
