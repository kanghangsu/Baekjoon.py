# input N, M
# N = number of dict_pokemons
# M = number of queries
# input N lines of dict_pokemon names
# input M lines of queries
# if query is a dict_pokemon name, print its index
# if query is a dict_pokemon index, print its name

import sys

input = sys.stdin.readline
print = sys.stdout.write

N, M = list(map(int, input().split()))

dict_pokemon_index_name = {}
dict_pokemon_name_index = {}

for i in range(1, N + 1):
    name = input().rstrip()
    dict_pokemon_index_name[i] = name
    dict_pokemon_name_index[name] = i

for i in range(M):
    query = input().rstrip()
    if query.isdigit():
        print(dict_pokemon_index_name[int(query)] + "\n")
    else:
        print(str(dict_pokemon_name_index[query]) + "\n")
