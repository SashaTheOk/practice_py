'''
| | | | |
| | | | |
| | | | |
| | | | |
'''

SIZE_N = 5
SIZE_M = 5

world_map = ''

for j in range (SIZE_M):

    row = '|'

    for i in range(SIZE_N):

        row += ' |'

    world_map += f'{row}\n'

print(world_map)