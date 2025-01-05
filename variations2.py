import itertools
from decimal import Decimal, getcontext
from fractions import Fraction

def find_unique_variations(numbers, k):
    """Finds unique variations with all possible averages."""

    n = len(numbers)
    if k > n or k <= 0:
        return "Invalid k value."

    all_variations = list(itertools.permutations(numbers, k))
    possible_averages = set()

    for variation in all_variations:
        average = Fraction(sum(variation), k) # Use Fraction for exact averages
        possible_averages.add(average)

    unique_variations_by_average = {}

    for average in sorted(list(possible_averages)): # Sort averages for consistent output
        unique_variations = []
        used_values = [set() for _ in range(k)]

        for variation in all_variations:
            if Fraction(sum(variation), k) == average:
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
            unique_variations_by_average[average] = unique_variations

    return unique_variations_by_average

# Example usage:
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
k = 6
result = find_unique_variations(numbers, k)

if isinstance(result, str):
    print(result)
else:
    for average, variations in result.items():
        filename = f"unique_variations_avg_{str(average).replace('/', '_')}.txt"
        with open(filename, "w") as f:
            for var in variations:
                f.write("\t".join(map(str, var)) + "\n")
        print(f"Found {len(variations)} unique variations (average = {average}) written to {filename}")

# Example with different numbers and k:
# numbers2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# k2 = 3
# result2 = find_unique_variations(numbers2, k2)

# if isinstance(result2, str):
#     print(result2)
# else:
#     for average, variations in result2.items():
#         filename = f"unique_variations_avg_{average}.txt"
#         with open(filename, "w") as f:
#             for var in variations:
#                 f.write("\t".join(map(str, var)) + "\n")
#         print(f"Found {len(variations)} unique variations (average = {average}) written to {filename}")
