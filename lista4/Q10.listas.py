#Eduardo Maia Freire
vetor1 = [1,3,5,7,9,11,13,15,17,19]
vetor2 = [2,4,6,8,10,12,14,16,18,20]
vetor3 = []
x = 0
v = len(vetor1)
for x in range (v):
    vetor3.append(vetor1[x])
    vetor3.append(vetor2[x])
    x = x + 1
print("Elementos do vetor 3 = ",vetor3)