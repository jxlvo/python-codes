matriz1 = [[1,5,6], [2,6,8],[9,10,12]]
matriz2 = [[56,52,16],[12,46,58],[19,31,15]]
matriz_mult = []
matriz_had = []

print("Produto matricial: ","\n")
for i in range(len(matriz1)):
  matriz_mult.append([])

  for j in range(len(matriz1[0])):
      mult = [x*y for x, y in zip(matriz1[i], matriz2[j])]
      matriz_mult[i].append(sum(mult))

for i in range(len(matriz_mult)):
  print(matriz_mult[i])

print("\n", "Produto Hadamard: ", "\n")
for i in range(len(matriz1[0])):
  for j in range(len(matriz2[0])):
    x = [x*y for x, y in zip(matriz1[0], matriz2[0])]
matriz_had.append(x)

for i in range(len(matriz1[1])):
  for j in range(len(matriz2[1])):
    y = [x*y for x, y in zip(matriz1[1], matriz2[1])]
matriz_had.append(y)

for i in range(len(matriz1[2])):
  for j in range(len(matriz2[2])):
    z = [x*y for x, y in zip(matriz1[2], matriz2[2])]
matriz_had.append(z)

for i in range(len(matriz_had)):
  print(matriz_had[i])
