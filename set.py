set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}

# Union |
union_set_comprehension = {x for x in set1} | {x for x in set2}

# Intersection &
intersection_set_comprehension = {x for x in set1} & {x for x in set2}

# Difference -
difference_set_comprehension = {x for x in set1} - {x for x in set2}

print("Union (set comprehension):", union_set_comprehension)
print("Intersection (set comprehension):", intersection_set_comprehension)
print("Difference (set comprehension):", difference_set_comprehension)
