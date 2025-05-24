def zeros(m, n=None):
    if n is None:
        return [0.0] * m
    return [[0.0 for _ in range(n)] for _ in range(m)]

def eye(n):
    I = zeros(n, n)
    for i in range(n):
        I[i][i] = 1.0
    return I

def mat_copy(M):
    return [row[:] for row in M]

def mat_mul(A, B):
    m, p = len(A), len(A[0])
    p2, n = len(B), len(B[0])
    if p != p2:
        raise ValueError("Incompatible matrix dimensions for multiplication")
    result = zeros(m, n)
    for i in range(m):
        for j in range(n):
            result[i][j] = sum(A[i][k] * B[k][j] for k in range(p))
    return result

def mat_transpose(M):
    return [list(row) for row in zip(*M)]

def mat_sub(A, B):
    return [[A[i][j] - B[i][j] for j in range(len(A[0]))] for i in range(len(A))]

def outer_product(u, v):
    return [[u[i] * v[j] for j in range(len(v))] for i in range(len(u))]

def norm(v):
    return sum(x**2 for x in v) ** 0.5

def print_matrix(M):
    for row in M:
        print(" ".join([f"{val:.4f}" for val in row]))

EPSILON = 1e-7

def my_qr(A, economy=False):
    A = mat_copy(A)
    m = len(A)
    n = len(A[0])
    Q = eye(m)
    R = mat_copy(A)
    stnd_basis = eye(m)

    for j in range(n):
        x = [R[i][j] for i in range(m)]
        basis = [stnd_basis[i][j] for i in range(m)]
        for i in range(j):
            x[i] = 0.0

        xj = x[j]
        alpha = -1.0 * norm(x) if xj >= 0 else norm(x)

        u = [x[i] - alpha * basis[i] for i in range(m)]
        norm_u_squared = sum(val**2 for val in u)
        if norm_u_squared == 0:
            continue

        # Householder transformation
        H = eye(m)
        outer = outer_product(u, u)

        for i in range(m):
            for k in range(m):
                H[i][k] -= 2 * outer[i][k] / norm_u_squared

        Q = mat_mul(H, Q)
        R = mat_mul(H, R)

        # Numerical stability fix
        for i in range(m):
            for k in range(n):
                if abs(R[i][k]) < EPSILON:
                    R[i][k] = 0.0
            for k in range(m):
                if abs(Q[i][k]) < EPSILON:
                    Q[i][k] = 0.0

        # Check if R is upper triangular
        is_upper = all(R[i][j] == 0.0 for i in range(m) for j in range(i))
        if is_upper:
            break

    if economy and m > n:
        Q = mat_transpose(Q)
        Q = [row[:n] for row in Q]
        R = R[:n]
    else:
        Q = mat_transpose(Q)

    return Q, R
