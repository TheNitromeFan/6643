def norm(x):
    return sum(xi ** 2 for xi in x) ** 0.5


def residual(A, x, b):
    n = len(A)
    r = b[::]
    for i in range(n):
        for j in range(n):
            r[i] -= A[i][j] * x[j]
    return r


def gauss_seidel(A, b, max_iterations=10000, residual_ratio=1e-4):
    n = len(A)
    assert len(A[0]) == n
    assert len(b) == n
    x = [0 for _ in range(n)] # initial guess
    r0 = residual(A, x, b) # initial residual
    iterations = 0 # iteration counter
    while iterations < max_iterations:
        iterations += 1
        for i in range(n):
            s = b[i]
            for j in range(n):
                if j != i:
                    s -= A[i][j] * x[j]
            s /= A[i][i]
            x[i] = s
        r = residual(A, x, b)
        if norm(r) / norm(r0) < residual_ratio:
            break
    return x


if __name__ == '__main__':
    A = [[3, 0, 1], [0, 7, 2], [1, 2, 4]]
    b = [1, 9, -2]
    x = gauss_seidel(A, b)
    print(x)
