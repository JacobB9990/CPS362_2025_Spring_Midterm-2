### Problem
Why the Gram-Schmidt algorithm is never preferred in the eigenvalue revealing problem?
Please argue it from the condition perspective.

### Answer 

Gram-Schmidt isn’t good for eigenvalue problems. When running on a computer the orthogonal vectors it gives can lead to rounding errors, which makes them not really orthogonal anymore. That completely messes with the eigenvalue stuff. Eigenvalue algorithms can be very sensitive, so even small errors lead to bad results. This is why Gram-Schmidt ends up being ill-conditioned.

$$
\frac{\|\tilde{f}(x) - f(x)\|}{\|f(x)\|} \approx O(\varepsilon_{\text{machine}})
$$

but Gram-Schmidt doesn’t give you that. Errors can accumulate way too fast. That’s why people go with QR iteration or Householder Reflection, they don’t break from small floating point errors and give way more reliable results. In the end, Gram-Schmidt just ends up being unreliable and not worth using for eigenvalue revealing problem. We are better off using other methods


