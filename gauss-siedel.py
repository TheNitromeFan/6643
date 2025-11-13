import random


def transpose(a):
    n = len(a)
    m = len(a[0])
    b = [[0.0 for _ in range(n)] for _ in range(m)]
    for i in range(m):
        for j in range(n):
            b[i][j] = a[j][i]
    return b


def inner_product(vector1, vector2):
    return sum(i * j for i, j in zip(vector1, vector2))


def norm(vector):
    return inner_product(vector, vector) ** 0.5


def gram_schmidt(vectors):
    n = len(vectors)
    m = len(vectors[0])
    normalized_vectors = []
    for i in range(n):
        u = vectors[i]
        answer = list(u)
        for j in range(i):
            v = normalized_vectors[j]
            c = inner_product(u, v) / inner_product(v, v)
            for k in range(m):
                answer[k] -= c * v[k]
        normalized_vectors.append(tuple(x / norm(answer) for x in answer))
    return normalized_vectors


def multiply_matrices(a, b):
    n = len(a)
    m = len(a[0])
    assert len(b) == m
    p = len(b[0])
    c = [[0.0 for _ in range(p)] for _ in range(n)]
    for i in range(n):
        for j in range(p):
            for k in range(m):
                c[i][j] += a[i][k] * b[k][j]
    return c


def quadratic_equation(a, b, c):
    d = (b ** 2 - 4 * a * c) ** 0.5
    return (-b + d) / (2 * a), (-b - d) / (2 * a)


def eigenvalues(a):
    trace = a[0][0] + a[1][1]
    determinant = a[0][0] * a[1][1] - a[0][1] * a[1][0]
    return quadratic_equation(1, -trace, determinant)


def main():
    min_max_eigenvalue = 1
    for _ in range(10 ** 6):
        m = []
        for _ in range(2):
            vector = []
            for _ in range(4):
                vector.append(50 * random.random() - 100)
            m.append(vector)
        m = gram_schmidt(m)
        max_eigenvalue = 0
        for i in range(4):
            for j in range(i + 1, 4):
                a = [[m[0][i], m[0][j]], [m[1][i], m[1][j]]]
                p = multiply_matrices(transpose(a), a)
                eigenvalue_max, eigenvalue_min = eigenvalues(p)
                max_eigenvalue = max(max_eigenvalue, eigenvalue_max)
        min_max_eigenvalue = min(min_max_eigenvalue, max_eigenvalue)
    print(min_max_eigenvalue)


def main2():
    min_max_eigenvalue = 109378
    save_m = None
    save_a = None
    save_p = None
    for _ in range(5 * 10 ** 4):
        m = []
        x = 0
        for _ in range(2):
            vector = []
            for _ in range(4):
                vector.append(50 * random.random() - 100)
            m.append(vector)
            x += sum(y ** 2 for y in vector)
        x **= 0.5
        scalar = 2 / x
        for vector in m:
            for i in range(4):
                vector[i] *= scalar
        max_eigenvalue = 0
        max_a = None
        max_p = None
        for i in range(4):
            for j in range(i + 1, 4):
                a = [[m[0][i], m[0][j]], [m[1][i], m[1][j]]]
                p = multiply_matrices(transpose(a), a)
                eigenvalue_max, eigenvalue_min = eigenvalues(p)
                if max_eigenvalue < eigenvalue_max:
                    max_eigenvalue = eigenvalue_max
                    max_a = a
                    max_p = p
        if min_max_eigenvalue > max_eigenvalue:
            min_max_eigenvalue = max_eigenvalue
            save_m = m
            save_a = max_a
            save_p = max_p
    min_max_singular_value = min_max_eigenvalue ** 0.5
    print(min_max_singular_value)
    print(save_m)
    print(save_a)
    print(save_p)


def main3():
    m = [[1/2, 0, 1/2**0.5, 1/2], [-1/2, 1/2**0.5, 0, 1/2]]
    max_eigenvalue = 0
    for i in range(4):
        for j in range(i + 1, 4):
            a = [[m[0][i], m[0][j]], [m[1][i], m[1][j]]]
            p = multiply_matrices(transpose(a), a)
            eigenvalue_max, eigenvalue_min = eigenvalues(p)
            print(i, j, eigenvalue_max, eigenvalue_min)
            max_eigenvalue = max(max_eigenvalue, eigenvalue_max)
    print(max_eigenvalue)


def test():
    m = [[(2 / 5) ** 0.5, (2 / 5) ** 0.5, (2 / 5) ** 0.5, 0], [0, 0, 0, (4 / 5) ** 0.5]]
    print(m)
    for i in range(4):
        for j in range(i + 1, 4):
            a = [[m[0][i], m[0][j]], [m[1][i], m[1][j]]]
            b = transpose(a)
            p = multiply_matrices(b, a)
            eigenvalue_max, eigenvalue_min = eigenvalues(p)
            singular_value_max, singular_value_min = eigenvalue_max ** 0.5, eigenvalue_min ** 0.5
            print(singular_value_max, singular_value_min)


if __name__ == '__main__':
    #main2()
    test()
