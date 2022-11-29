cube = [['x', 'w', 'w', 'w', 'x'], ['g', 'o', 'o', 'o', 'b'], ['g', 'o', 'o', 'o', 'b'], ['g', 'o', 'o', 'o', 'b'],
        ['x', 'y', 'y', 'y', 'x']]
cube1 = []
cube2 = []
cube3 = []


def cube_input():
    r1 = ['x', input(), input(), input(), 'x']
    r2 = [input(), input(), input(), input(), input()]
    r3 = [input(), input(), input(), input(), input()]
    r4 = [input(), input(), input(), input(), input()]
    r5 = ['x', input(), input(), input(), 'x']
    cube[0] = r1
    cube[1] = r2
    cube[2] = r3
    cube[3] = r4
    cube[4] = r5


def convert_mono():
    core = str(cube[2][2])
    for co in range(5):
        for ro in range(5):
            if cube[co][ro] == core:
                cube[co][ro] = '1'
            elif cube[co][ro] == 'x':
                cube[co][ro] == str('x')
            else:
                cube[co][ro] = '0'


def turn_left(next_permutation, current_state):
    for n in reversed(range(5)):
        next_permutation.append([row[n] for row in current_state])


def present(cube_print):
    for r in cube_print:
        for c in r:
            print(c, end=" ")
        print()
