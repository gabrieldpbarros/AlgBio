dna1 = "AATGCGTACG"
length = len(dna1)
middle = length//2

if(length % 2 == 0):
    for i in range(-2, 2):
        print(f"{dna1[middle + i]}", end='')

else:
    for i in range(-1, 3):
        print(f"{dna1[middle + i]}", end='')

print()