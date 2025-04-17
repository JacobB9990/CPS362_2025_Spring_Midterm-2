import numpy as np


# Create a symmetric matrix
def make_matrix():
    return np.array([[2.0, 1.0, 0.0], [1.0, 2.0, 1.0], [0.0, 1.0, 2.0]])


# QR decomposition using numpy
def qr_decompose(A):
    Q, R = np.linalg.qr(A)
    return Q, R


# Step 3: One QR iteration step
def qr_step(A):
    Q, R = qr_decompose(A)
    return R @ Q


# Repeat QR iteration
def qr_iteration(A, steps=30):
    A_k = A.copy()
    for i in range(steps):
        A_k = qr_step(A_k)
        print(f"Step {i+1}:")
        print(np.round(A_k, 4))
        print()
    return A_k

def main():
    A = make_matrix()
    print("Original matrix A:")
    print(A)
    print("\nStarting QR iteration\n")

    A_final = qr_iteration(A, steps=30)

    print("Final matrix after QR iteration:")
    print(np.round(A_final, 4))
    print("\nApprox eigenvalues (diagonal):")
    print(np.round(np.diag(A_final), 4))


main()
