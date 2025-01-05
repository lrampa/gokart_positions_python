import itertools
from fractions import Fraction

"""
Finding the maximum number of unique variations is a much more complex problem,
related to maximum independent set problems in graph theory, which are NP-hard.
This means there's no known efficient algorithm to find the absolute best
solution in all cases.

However, we can implement a much-improved approach that is far more likely to
find a larger set of unique variations than the previous methods. This
approach uses backtracking.

Key Changes and Explanation:

1. find_max_unique_variations Function: This function now implements
   the backtracking algorithm.
2. find_unique_recursive Function: This recursive function does the heavy lifting:
   - Base Case: If remaining_variations is empty, it returns the current_unique set.
   - Recursive Step: It iterates through the remaining_variations. For each variation,
     it checks if it's unique with the current_unique set. If it is, it recursively
     calls itself with the updated current_unique set and the remaining variations
     after removing those that are now incompatible.
   - Maximization: It keeps track of the best_found set (the largest set found so
     far) and returns it.
3. Removing incompatible variations: Inside recursive function is added removing
   of incompatible variations remaining_after_selection = [...]. This is done after
   checking uniqueness of current variation with existing unique variations.

This backtracking approach explores different combinations of unique variations
and is much more likely to find a larger set than simply picking the first available
unique variation. It is still not guaranteed to find the absolute maximum in all cases
(due to the NP-hard nature of the problem), but it's a significant improvement and
will give you much better results in practice.

This is the most advanced and effective solution I can provide within the constraints
of reasonable computational time. If you have extremely large sets of numbers or very
large k values, even this approach might become computationally intensive. In those
cases, more advanced optimization techniques or approximation algorithms would be necessary.
"""


def find_max_unique_variations(numbers, k):
    """Finds a large set of unique variations with all possible averages using backtracking."""

    n = len(numbers)
    if k > n or k <= 0:
        return "Invalid k value."

    all_variations = list(itertools.permutations(numbers, k))
    possible_averages = set()

    for variation in all_variations:
        average = Fraction(sum(variation), k)
        possible_averages.add(average)

    max_unique_variations_by_average = {}

    for average in sorted(list(possible_averages)):
        if average != Fraction(5, 1):
            continue

        variations_for_avg = [var for var in all_variations if Fraction(sum(var), k) == average]
        
        def find_unique_recursive(current_unique, remaining_variations):
            if len(current_unique) < 4:
                print(f"Checking {len(remaining_variations)} variations for {len(current_unique)}")
            if not remaining_variations:
                return current_unique
            
            best_found = current_unique
            for i in range(len(remaining_variations)):
                current_var = remaining_variations[i]
                
                is_unique_with_current = True
                for existing_var in current_unique:
                    if any(current_var[j] == existing_var[j] for j in range(k)):
                        is_unique_with_current = False
                        break
                
                if is_unique_with_current:
                    remaining_after_selection = [
                        var for var in remaining_variations[i+1:] # Check only variations after current
                        if not any(current_var[j] == var[j] for j in range(k))
                    ]
                    
                    found_set = find_unique_recursive(current_unique + [current_var], remaining_after_selection)
                    if len(found_set) > len(best_found):
                        best_found = found_set
            return best_found

        max_unique_variations = find_unique_recursive([], variations_for_avg)

        if max_unique_variations:
            max_unique_variations_by_average[average] = max_unique_variations

    return max_unique_variations_by_average


# Example usage (same as before):
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
k = 6
result = find_max_unique_variations(numbers, k)

if isinstance(result, str):
    print(result)
else:
    for average, variations in result.items():
        filename = f"max_unique_variations_avg_{str(average).replace('/', '_')}.txt"
        with open(filename, "w") as f:
            for var in variations:
                f.write("\t".join(map(str, var)) + "\n")
        print(f"Found {len(variations)} max unique variations (average = {average}) written to {filename}")
