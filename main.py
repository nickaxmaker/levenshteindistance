firstWord = input("please enter the first word to compare: ")
firstWord = firstWord.lower()
secondWord = input("please enter the second word to compare: ")
secondWord = secondWord.lower()

firstWord = list(firstWord)
secondWord = list(secondWord)
firstWord.insert(0, '')
secondWord.insert(0, '')

calculationMatrix = []
n = len(firstWord)
m = len(secondWord)

for x in range(0, m):
    calculationMatrix.append([])
    for y in range(0, n):
        calculationMatrix[x].append(0)

for i in range(0, m):
    calculationMatrix[i][0] = i

for j in range(0, n):
    calculationMatrix[0][j] = j

for j in range(1, n):
    for i in range(1, m):
        if firstWord[j] == secondWord[i]:
            substitutionCost = 0
        else:
            substitutionCost = 1
        calculationMatrix[i][j] = min(calculationMatrix[i-1][j] + 1, calculationMatrix[i][j-1] + 1, calculationMatrix[i-1][j-1] + substitutionCost)

print(calculationMatrix)