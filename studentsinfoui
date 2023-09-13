opcao = ''
nomes = (input('Entre com os nomes dos alunos: ').upper()).split(';')
notas = input('Entre com as respectivas notas: ').split(';')
while opcao != '3':
    print('[1] ADICIONAR NOVO ALUNO/NOTA')
    print('[2] REMOVER ALUNO/NOTA')
    print('[3] REALIZAR OS CÁLCULOS')
    opcao = input('Inisra a opção desejada: ')
    print('')
    
    if opcao == '1':
        nnome = input('Entre com o nome do aluno: ').upper()
        nnota = input('Entre com a nota do aluno: ')
        nomes.append(nnome)
        notas.append(nnota)

    for p in range(0,len(notas)-1):
        pmin=p
        for q in range(p+1,len(notas)):
            if notas[q]>notas[pmin]:
                pmin=q
        tempx = notas[p]
        notas[p] = notas[pmin]
        notas[pmin] = tempx
        tempx = nomes[p]
        nomes[p] = nomes[pmin]
        nomes[pmin] = tempx

    if opcao == '2':
        rnome = input('Entre com o nome do aluno a ser removido: ').upper()
        for rn in range(0,len(nomes)-1):
            if nomes[rn] == rnome:
                nomes.remove(nomes[rn])
                notas.remove(notas[rn])
    
#notas para float          
for n in range(len(notas)):
    notas[n] = float(notas[n])

#ordem crescente e maior e menor nota
print('Maior e menor nota')
for i in range(0,len(notas)-1):
    menor = i
    for j in range(i+1,len(notas)):
        if notas[j] < notas[menor]:
            menor = j
    temp = notas[i]
    notas[i] = notas[menor]
    notas[menor]=temp
print('Maior nota: ',notas[-1])
print('Menor nota: ',notas[0])
print('')

#associar listas
for p in range(0,len(notas)-1):
    pmin=p
    for q in range(p+1,len(notas)):
        if notas[q]>notas[pmin]:
            pmin=q
    tempx = notas[p]
    notas[p] = notas[pmin]
    notas[pmin] = tempx
    tempx = nomes[p]
    nomes[p] = nomes[pmin]
    nomes[pmin] = tempx

#media aritimetica
print('Média aritimética')
soma = 0
for k in notas:
    soma += k
    media = soma/len(notas)
print('Média das notas: ',media)
print('')

#desvio padrao
print('Desvio padrão')
somatorio = 0
for l in range(0,len(notas)):
    distx = (media-notas[l])**2
    somatorio += distx
    x = somatorio/len(notas)
    dp = x**(1/2)
print('Desvio Padrão: ',dp)
print('')
        
#mediana
print('Mediana')
if len(notas)%2 == 0:
    mediana = (notas[(len(notas))//2] + (notas[(len(notas)//2)-1]))/2
else:
    mediana = notas[(len(notas))//2]
print('A mediana das notas: ',mediana)
print('')

#moda
print('Moda')
contador = 0
rep = 0
for m in range(len(notas)):
    contador = 0
    for o in range(len(notas)):
        if notas[m]==notas[o]:
            contador += 1
    if contador > rep:
        rep = contador
        moda = notas[m]        
print('A moda das notas é: ',moda,' que se repete ', rep, ' vezes')
print('')

#intervalo de notas
print('Notas dentro de um intervalo')
nummax = float(input('Insira o maior valor: '))
nummin = float(input('Insira o menor valor: '))
for mx in range(0,len(notas)):
        if notas[mx]>nummin and notas[mx]<nummax:
            print(notas[mx],nomes[mx])
print('')

#busca por letras
print('Busca por caracteres')
procura = input('Buscar: ').upper()
if procura == '':
    for o in range(len(nomes)):
        print(notas[o],nomes[o])        
else:
    for o in range(len(nomes)):
        proc = nomes[o].count(procura)
        if proc > 0:
            print(notas[o],nomes[o])
print('')

#frequencia em um intervalo
print('Frequencia das notas num intervalo')
nummax2 = float(input('Insira o maior valor: '))
nummin2 = float(input('Insira o menor valor: '))
for mx2 in range(0,len(notas)):
    if notas[mx2]>nummin2 and notas[mx2]<nummax2:
        print((notas[mx2]),':',notas.count(notas[mx2]))
print('')
print('Fim do Programa')
