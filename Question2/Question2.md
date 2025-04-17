### Problem  
Give a numerically stable algorithm to compute eigenvalues, and show it in a concrete example (e.g. on a 3-by-3 matrix) step by step (both manual work and programs are acceptable), and argue why it is stable.

### Answer  

To calculate eigenvalues in a more stable way, we can use QR Iteration. This method is better than Gram-Schmidt because it still holds even when rounding errors do occur. The method is to take a matrix $A$ and decompose it into $Q$ and $R$, where $Q$ is orthogonal and $R$ is upper triangular. We then form a new matrix by multiplying $R$ and $Q$ in reverse order, so $A_{k+1} = R_k Q_k$. We want to do this over and over again. The matrix becomes upper triangular over iterations, and the diagonal entries start to look like the eigenvalues.

Even though we used `numpy` in the code to help with matrix operations, it's still important to understand how the algorithm actually works. The most important part is that each operation keeps the matrix similar to the original one, which means the eigenvalues don’t change, and they become more visible on the diagonal. QR iteration avoids unstable stuff like subtracting nearly equal numbers or solving ill-conditioned systems directly. It’s a more clean way to get approximate eigenvalues just from repeated QR factorizations.bThis method is stable because it satisfies:

$$
\frac{\|\tilde{f}(x) - f(x)\|}{\|f(x)\|} \approx O(\varepsilon_{\text{machine}})
$$

which means the error stays small and controlled, even with floating point math. That’s why QR iteration is preferred, it’s reliable, stable, and it actually works without falling apart like the ol' Gram-Schmidt does.
