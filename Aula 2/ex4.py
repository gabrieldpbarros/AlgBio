dna1 = "AGCTGA"
size = len(dna1) 
for i in range(0, size, 5):
    print(f"{dna1[i]}", end=' ')
print()