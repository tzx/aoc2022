numbers = [int(li) for li in open('input.txt')]

indices = [i for i in range(len(numbers))]
for old_idx in range(len(indices)):
    new_idx = indices.index(old_idx)
    indices.pop(new_idx)
    indices.insert((new_idx + numbers[old_idx]) % len(indices), old_idx)
z = indices.index(numbers.index(0))
cycle_hit = list(numbers[indices[(z + idx) % len(indices)]]
                 for idx in [1000, 2000, 3000])
print(sum(cycle_hit))

DEC_KEY = 811589153
numbers = [DEC_KEY * n for n in numbers]
indices = list(range(len(numbers)))
for old_idx in indices * 10:
    new_idx = indices.index(old_idx)
    indices.pop(new_idx)
    indices.insert((new_idx + numbers[old_idx]) % len(indices), old_idx)
z = indices.index(numbers.index(0))
cycle_hit = list(numbers[indices[(z + idx) % len(indices)]]
                 for idx in [1000, 2000, 3000])
print(sum(cycle_hit))
