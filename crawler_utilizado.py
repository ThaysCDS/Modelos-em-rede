import instaloader
import time

lib = instaloader.Instaloader()

lib.login("<usuario>", "<senha>")

arquivo = open("grafo.txt", "a")


# 1 --------------------------------------------------------------------

raiz_1 = instaloader.Profile.from_username(lib.context, "<seguidor1>")

arquivo1 = open("seguindo1.txt", "a")

raiz_seguindo_1 = []

# codigo filtrando os primeiros 600 seguidores que nao são verificados
c = 0
for seguidor1 in raiz_1.get_followees():
    if (seguidor1.is_verified):
        k = 0
    else:
        if (c < 700):
            raiz_seguindo_1.append(seguidor1.username)
            c += 1
        else:
            break

# transformando a lista dos nomes em uma lista numérica de 1 a len(lista)

raiz_seguindo_1_num = []

for i in range(1, len(raiz_seguindo_1) + 1):
    raiz_seguindo_1_num.append(i)

#gravando no arquivo os nós do meu primeiro perfil raiz
for n in raiz_seguindo_1_num:
    arquivo.write("0 {0} \n".format(n))
    index_nome_numero = raiz_seguindo_1_num.index(n)
    index_nome = raiz_seguindo_1[index_nome_numero]
    arquivo1.write("{0} {1} \n".format(n, index_nome))



# 2 --------------------------------------------------------------------

time.sleep(180)

raiz_2 = instaloader.Profile.from_username(lib.context, "<seguidor2>")

arquivo2 = open("seguindo2.txt", "a")

raiz_seguindo_2 = []

c = 0
for f in raiz_2.get_followees():
    if (f.is_verified):
        k = 0
    else:
        if (c < 300):
            raiz_seguindo_2.append(f.username)
            c += 1
        else:
            break

raiz_seguindo_2_num = []

# transformando a lista de nomes em número, sem atribuir mais de um número para o mesmo perfil
len2 = len(raiz_seguindo_1_num) + 1
for seguidor2 in raiz_seguindo_2:
    if seguidor2 in raiz_seguindo_1:
        index_nome = raiz_seguindo_1.index(seguidor2)
        index_nome_numero = raiz_seguindo_1_num[index_nome]
        raiz_seguindo_2_num.append(index_nome_numero)
    else:
        raiz_seguindo_2_num.append(len2)
        len2 += 1

posicaoNome2 = raiz_seguindo_1.index("<seguidor2>")
posicaoNumero2 = raiz_seguindo_1_num[posicaoNome2]

for n in raiz_seguindo_2_num:
    arquivo.write("{0} {1} \n".format(posicaoNumero2, n))
    index_nome_numero = raiz_seguindo_2_num.index(n)
    index_nome = raiz_seguindo_2[index_nome_numero]
    arquivo2.write("{0} {1} \n".format(n, index_nome))



# 3 --------------------------------------------------------------------

time.sleep(180)

raiz_3 = instaloader.Profile.from_username(lib.context, "<seguidor3>")

arquivo3 = open("seguindo3.txt", "a")

raiz_seguindo_3 = []

c = 0
for f in raiz_3.get_followees():
    if (f.is_verified):
        k = 0
    else:
        if (c < 100):
            raiz_seguindo_3.append(f.username)
            c += 1
        else:
            break

raiz_seguindo_3_num = []

len3 = max(raiz_seguindo_2_num) + 1
for seguidor3 in raiz_seguindo_3:
    if seguidor3 in raiz_seguindo_1:
        index_nome = raiz_seguindo_1.index(seguidor3)
        index_nome_numero = raiz_seguindo_1_num[index_nome]
        raiz_seguindo_3_num.append(index_nome_numero)
    elif seguidor3 in raiz_seguindo_2:
        index_nome = raiz_seguindo_2.index(seguidor3)
        index_nome_numero = raiz_seguindo_2_num[index_nome]
        raiz_seguindo_3_num.append(index_nome_numero)
    else:
        raiz_seguindo_3_num.append(len3)
        len3 += 1

posicaoNome3 = raiz_seguindo_1.index("<seguidor3>")
posicaoNumero3 = raiz_seguindo_1_num[posicaoNome3]

for n in raiz_seguindo_3_num:
    arquivo.write("{0} {1} \n".format(posicaoNumero3, n))
    index_nome_numero = raiz_seguindo_3_num.index(n)
    index_nome = raiz_seguindo_3[index_nome_numero]
    arquivo3.write("{0} {1} \n".format(n, index_nome))


# 4 --------------------------------------------------------------------

time.sleep(180)

raiz_4 = instaloader.Profile.from_username(lib.context, "<seguidor4>")

arquivo4 = open("seguindo4.txt", "a")

raiz_seguindo_4 = []

c = 0
for f in raiz_4.get_followees():
    if (f.is_verified):
        k = 0
    else:
        if (c < 600):
            raiz_seguindo_4.append(f.username)
            c += 1
        else:
            break

raiz_seguindo_4_num = []

len4 = max(raiz_seguindo_3_num) + 1
for seguidor4 in raiz_seguindo_4:
    if seguidor4 in raiz_seguindo_1:
        index_nome = raiz_seguindo_1.index(seguidor4)
        index_nome_numero = raiz_seguindo_1_num[index_nome]
        raiz_seguindo_4_num.append(index_nome_numero)
    elif seguidor4 in raiz_seguindo_2:
        index_nome = raiz_seguindo_2.index(seguidor4)
        index_nome_numero = raiz_seguindo_2_num[index_nome]
        raiz_seguindo_4_num.append(index_nome_numero)
    elif seguidor4 in raiz_seguindo_3:
        index_nome = raiz_seguindo_3.index(seguidor4)
        index_nome_numero = raiz_seguindo_3_num[index_nome]
        raiz_seguindo_4_num.append(index_nome_numero)
    else:
        raiz_seguindo_4_num.append(len4)
        len4 += 1

posicaoNome4 = raiz_seguindo_1.index("<seguidor4>")
posicaoNumero4 = raiz_seguindo_1_num[posicaoNome4]

for n in raiz_seguindo_4_num:
    arquivo.write("{0} {1} \n".format(posicaoNumero4, n))
    index_nome_numero = raiz_seguindo_4_num.index(n)
    index_nome = raiz_seguindo_4[index_nome_numero]
    arquivo4.write("{0} {1} \n".format(n, index_nome))


# 5 --------------------------------------------------------------------

time.sleep(180)

raiz_5 = instaloader.Profile.from_username(lib.context, "<seguidor5>")

arquivo5 = open("seguindo5.txt", "a")

raiz_seguindo_5 = []

c = 0
for f in raiz_5.get_followees():
    if (f.is_verified):
        k = 0
    else:
        if (c < 400):
            raiz_seguindo_5.append(f.username)
            c += 1
        else:
            break

raiz_seguindo_5_num = []

len5 = max(raiz_seguindo_4_num) + 1
for seguidor5 in raiz_seguindo_5:
    if seguidor5 in raiz_seguindo_1:
        index_nome = raiz_seguindo_1.index(seguidor5)
        index_nome_numero = raiz_seguindo_1_num[index_nome]
        raiz_seguindo_5_num.append(index_nome_numero)
    elif seguidor5 in raiz_seguindo_2:
        index_nome = raiz_seguindo_2.index(seguidor5)
        index_nome_numero = raiz_seguindo_2_num[index_nome]
        raiz_seguindo_5_num.append(index_nome_numero)
    elif seguidor5 in raiz_seguindo_3:
        index_nome = raiz_seguindo_3.index(seguidor5)
        index_nome_numero = raiz_seguindo_3_num[index_nome]
        raiz_seguindo_5_num.append(index_nome_numero)
    elif seguidor5 in raiz_seguindo_4:
        index_nome = raiz_seguindo_4.index(seguidor5)
        index_nome_numero = raiz_seguindo_4_num[index_nome]
        raiz_seguindo_5_num.append(index_nome_numero)
    else:
        raiz_seguindo_5_num.append(len5)
        len5 += 1

posicaoNome5 = raiz_seguindo_1.index("<seguidor5>")
posicaoNumero5 = raiz_seguindo_1_num[posicaoNome5]

for n in raiz_seguindo_5_num:
    arquivo.write("{0} {1} \n".format(posicaoNumero5, n))
    index_nome_numero = raiz_seguindo_5_num.index(n)
    index_nome = raiz_seguindo_5[index_nome_numero]
    arquivo5.write("{0} {1} \n".format(n, index_nome))


arquivo.close()
arquivo1.close()
arquivo2.close()
arquivo3.close()
arquivo4.close()
arquivo5.close()
