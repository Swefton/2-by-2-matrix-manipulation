# creating 1 by 5 matrix
cube = [['x', 'x', 'x', 'x', 'x'], ['x', 'x', 'x', 'x', 'x'], ['x', 'x', 'x', 'x', 'x'], ['x', 'x', 'x', 'x', 'x'], ['x', 'x', 'x', 'x', 'x']]
cube1 = []
cube2 = []
cube3 = []

#function to take user input and add it to an empty matrix
def cube_input(e_matrix):
    r1 = [input(), input(), input(), input(), input()]
    r2 = [input(), input(), input(), input(), input()]
    r3 = [input(), input(), input(), input(), input()]
    r4 = [input(), input(), input(), input(), input()]
    r5 = [input(), input(), input(), input(), input()]
    e_matrix[0] = r1
    e_matrix[1] = r2
    e_matrix[2] = r3
    e_matrix[3] = r4
    e_matrix[4] = r5

# all values are compared to the center piece, if content is same it's converted to 1 and if not 0
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

# rotates all values of the matrix counter-clockwise
def turn_left(next_permutation, current_state):
    for n in reversed(range(5)):
        next_permutation.append([row[n] for row in current_state])

# prints values of the matrix with line breaks for easier visualization
def present(cube_print):
    for r in cube_print:
        for c in r:
            print(c, end=" ")
        print()
