N, M = list(map(int, input().split()))

# N persons
persons = {}

for _ in range(N):
    person = input()
    persons[person] = True

# M well known persons
well_known_persons = []

for _ in range(M):
    well_known_person = input()
    well_known_persons.append(well_known_person)

# Find the common persons
common_persons = []

for person in well_known_persons:
    if person in persons:
        common_persons.append(person)

# Print the common persons
print(len(common_persons))

for person in sorted(common_persons):
    print(person)
