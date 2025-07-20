output = """Matrix A:
1+1j 2+2j 3+3j 4+4j 5+5j 6+6j 7+7j 8+8j 
2-1j 3+0j 4+1j 5+2j 6+3j 7+4j 8+5j 1+6j 
3+2j 4-1j 5+0j 6+1j 7+2j 8+3j 1+4j 2+5j 
4-3j 5+2j 6-1j 7+0j 8+1j 1+2j 2+3j 3+4j 
5+4j 6-3j 7+2j 8-1j 1+0j 2+1j 3+2j 4+3j 
6-5j 7+4j 8-3j 1+2j 2-1j 3+0j 4+1j 5+2j 
7+6j 8-5j 1+4j 2-3j 3+2j 4-1j 5+0j 6+1j 
8-7j 1+6j 2-5j 3+4j 4-3j 5+2j 6-1j 7+0j 
Matrix Q:
-0.0761387+0j -0.12009-0.0918868j 0.0127839-0.292873j 0.000633863-0.253151j 0.284118+0.109027j 0.224366-0.260928j 0.391211-0.077257j -0.0931901+0.665268j 
-0.0380693+0.114208j -0.153461+0.00949433j -0.0131262-0.28335j -0.0309598-0.23354j 0.269174+0.0867171j 0.189562-0.237824j 0.3359-0.0671059j 0.0298803-0.731584j 
-0.190347+0.0380693j -0.193119+0.109419j -0.251875-0.0943192j 0.0317304-0.280591j 0.231516-0.0247841j 0.118725-0.219096j -0.652896+0.465306j -0.0335683+0.0274654j 
-0.0380693+0.266485j -0.262681-0.116495j -0.115149-0.207228j -0.281825-0.0620649j 0.295284+0.151226j -0.266954+0.721206j 0.0119773+0.0396557j -0.0331565+0.0346955j 
-0.342624+0.0380693j -0.273125+0.263424j -0.185602-0.204034j -0.142127-0.207451j -0.741282+0.00954174j 0.147932+0.104725j 0.0950626-0.0656398j -0.0409683+0.019746j 
-0.0380693+0.418763j -0.371901-0.242669j -0.217255-0.131021j 0.395351+0.567098j -0.103232-0.000685151j -0.111679-0.208789j 0.0710166+0.101026j -0.0356661+0.0218538j 
-0.494902+0.0380693j -0.353132+0.41743j 0.48027+0.331018j 0.0137969+0.175552j 0.24658-0.0144145j -0.0594572-0.0259759j 0.0162795-0.120916j -0.055391+0.0160987j 
-0.0380693+0.57104j -0.0117156-0.425887j 0.129928+0.455527j -0.0389887-0.37912j -0.101878-0.177491j 0.205194-0.0187345j -0.0829605-0.169682j -0.0349247+0.00875291j 
Matrix R:
-13.1339-13.1339j -2.24609-2.77906j -8.87016-9.63155j -2.55065-4.14956j -5.67233-8.10877j -3.00748-6.89055j -3.54045-9.17471j -3.00748-11.002j 
9.97577e-16+2.75818e-16j -16.7949-2.04061j -3.8751-0.114264j -11.4872-1.38144j -5.0711-0.767297j -8.15932-1.99565j -6.72721-2.73549j -7.31592-4.32159j 
1.68028e-16-1.02827e-15j 0.000843562+4.77844e-05j -6.18486+6.6537j -3.745+2.94244j -4.64255+3.32709j -3.80963+0.534158j -4.20304-0.473852j -4.68434-2.4744j 
1.22738e-15+6.3933e-16j 0.000690285+9.67588e-05j 0.000182396-0.000388859j -5.22746+6.8849j -3.34932+4.63186j -4.03906+4.54508j -3.50208+3.07719j -3.98006+1.82975j 
-2.97668e-16-7.88261e-16j -0.000255535-0.000805128j -0.000156527-0.000212528j -0.000402411-1.14775e-05j 7.81428+2.53174j 5.31912+2.58886j 4.69638+3.03924j 3.0624+3.97412j 
-1.53678e-16-1.31237e-15j 0.000709397-0.0005683j 3.74365e-05-0.000274374j -0.00038568+0.00127517j -0.00044108-0.000481456j 2.46643+7.42087j 1.89384+5.44043j 0.679616+4.13095j 
-6.60325e-17-8.0605e-16j 0.000194098-0.0010091j 0.000401074+0.00183458j -0.000218332+0.000138184j -5.4781e-05-4.03695e-05j 4.11309e-05+0.000448733j 6.19291+4.13494j 3.79669+3.6783j 
-1.23387e-15+1.30805e-15j 0.00234328+0.000401802j -9.00905e-05-4.05067e-05j 0.00021657+0.00044778j 0.000231675-0.000368349j 0.00141324-0.000221163j 0.000260244-8.10441e-05j -0.47347-6.21203j 
"""

# If the flag - is set, read from stdin
import os
import sys

USE_COMPLEX = True

if len(sys.argv) > 1 and sys.argv[1] == "-":
    print("Reading from stdin...")
    output = ""
    output = sys.stdin.read()
    while not output.strip():
        output = sys.stdin.read()

matrices_A = []
matrices_Q = []
matrices_R = []

lines = output.strip().splitlines()

i = 0

def print_matrix(matrix):
    for row in matrix:
        if USE_COMPLEX:
            print(" ".join(f"{val.real:.3f}+{val.imag:.3f}j" if val.imag >= 0 else f"{val.real:.3f}{val.imag:.3f}j" for val in row))
        else:
            print(" ".join(f"{val:.6f}" for val in row))

def parse_matrix(lines, start_index):
    matrix = []
    while start_index < len(lines) and lines[start_index].startswith("Matrix"):
        start_index += 1
    while start_index < len(lines) and lines[start_index].strip():
        if lines[start_index].startswith("Matrix"):
            break
        if USE_COMPLEX:
            row = list(map(complex, lines[start_index].split()))
        else:
            row = list(map(float, lines[start_index].split()))
        matrix.append(row)
        start_index += 1
    return matrix, start_index

while i < len(lines):
    if lines[i].startswith("Matrix A:"):
        matrix_A, i = parse_matrix(lines, i)
        matrices_A.append(matrix_A)
    elif lines[i].startswith("Matrix Q:"):
        matrix_Q, i = parse_matrix(lines, i)
        matrices_Q.append(matrix_Q)
    elif lines[i].startswith("Matrix R:"):
        matrix_R, i = parse_matrix(lines, i)
        matrices_R.append(matrix_R)
    else:
        i += 1

print("Found matrices:")
print(f"Number of A matrices: {len(matrices_A)}")
print(f"Number of Q matrices: {len(matrices_Q)}")
print(f"Number of R matrices: {len(matrices_R)}")

assert len(matrices_A) == len(matrices_Q) == len(matrices_R), "Mismatch in number of matrices A, Q, and R"

import sys
sys.path.append("..")
sys.path.append("test")

from qrd import mat_mul

# The output only has 4 decimal places, so we use a small epsilon for comparison
EPSILON = 1e-3

def compare_matrices(A, B):
    assert len(A) == len(B) and len(A[0]) == len(B[0]), "Matrix size mismatch"

    D = [[A[i][j] - B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

    for i in range(len(D)):
        for j in range(len(D[0])):
            if abs(D[i][j]) < EPSILON:
                D[i][j] = 0.0

    for i in range(len(D)):
        for j in range(len(D[0])):
            if abs(D[i][j]) >= EPSILON:
                print_matrix(A)
                print()
                print_matrix(B)
                print()
                print_matrix(D)
                raise AssertionError(f"Invalid matrix value at ({i}, {j}): {D[i][j]} != 0")


for idx, (A, Q, R) in enumerate(zip(matrices_A, matrices_Q, matrices_R)):
    print("Checking matrices A, Q, R at index", idx)

    reconstructed_A = mat_mul(Q, R)

    compare_matrices(A, reconstructed_A)

print("All matrices decompositions are valid.")
