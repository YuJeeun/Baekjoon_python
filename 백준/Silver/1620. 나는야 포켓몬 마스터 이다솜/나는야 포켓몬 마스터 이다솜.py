n, m = map(int, input().split())

pokemon_ddict = {}
for i in range(1, n+1):
    pokemon = input()
    pokemon_ddict[pokemon] = str(i)
    pokemon_ddict[str(i)] = pokemon

question = [input() for _ in range(m)]

for i in range(m):
    print(pokemon_ddict[question[i]])