import itertools
from decimal import Decimal, getcontext

getcontext().prec = 3  # Set precision for decimal calculations

numbers = [2, 3, 4, 5, 6, 7, 8]
k = 3

min_possible_average = Decimal(sum(sorted(numbers[:k])) / k)
max_possible_average = Decimal(sum(sorted(numbers[-k:])) / k)

# Iterate by 0.25 to catch all possible averages
for i in range(int((max_possible_average - min_possible_average) * 4) + 1):
    target_average = min_possible_average + Decimal(i) / 4

    all_variations_for_avg = []
    for variation_tuple in itertools.permutations(numbers, k):
        variation = list(variation_tuple)
        if Decimal(sum(variation)) / k == target_average:
            all_variations_for_avg.append(variation)

    unique_variations = []
    used_values = [set() for _ in range(k)]

    for variation in all_variations_for_avg:
        is_unique = True
        for j in range(k):
            if variation[j] in used_values[j]:
                is_unique = False
                break
        if is_unique:
            unique_variations.append(variation)
            for j in range(k):
                used_values[j].add(variation[j])

    if unique_variations:
        filename = f"unique_variations_avg_{target_average}.txt"
        with open(filename, "w") as f:
            for var in unique_variations:
                f.write("\t".join(map(str, var)) + "\n")
        print(f"Found {len(unique_variations)} unique variations (average = {target_average}) written to {filename}")
    else:
        print(f"No unique variations found for average {target_average}")