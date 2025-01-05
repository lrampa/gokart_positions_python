import itertools

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
k = 6  # Number of elements to choose

variations = list(itertools.permutations(numbers, k))

# Format the output for easy pasting into Excel
with open("variations.txt", "w") as f:
    for var in variations:
        f.write("\t".join(map(str, var)) + "\n")

print(f"{len(variations)} variations written to variations.txt")