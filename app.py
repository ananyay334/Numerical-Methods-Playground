import streamlit as st
import numpy as np
import sympy as sp
import matplotlib.pyplot as plt
from newton import NewtonRaphson
from bisection import Bisection
from secant import Secant
from falseposition import FalsePosition


st.title("Numerical Methods Playground")
st.write("Explore root-finding algorithms interactively!")

method = st.selectbox("Choose a method", ["Newton-Raphson", "Bisection", "Secant", "False-Position"])
func_str = st.text_input("Enter function f(x):", "x**3 - 2*x - 5")
x = sp.Symbol('x')
f = sp.lambdify(x, sp.sympify(func_str), 'numpy')
f_prime = sp.lambdify(x, sp.diff(sp.sympify(func_str), x), 'numpy')

if method == "Newton-Raphson":
    x0 = st.number_input("Initial guess x0:", value=2.0)
    root, steps = NewtonRaphson(f, f_prime, x0,100,1e-6)
elif method == "Bisection":
    a = st.number_input("Interval a:", value=1.0)
    b = st.number_input("Interval b:", value=3.0)
    root, steps = Bisection(f, a, b)
elif method == "Secant":
    x0 = st.number_input("Initial guess x0:", value=2.0)
    x1 = st.number_input("Initial guess x1:", value=3.0)
    root, steps = Secant(f, x0, x1)
else:
    a = st.number_input("Interval a:", value=1.0)
    b = st.number_input("Interval b:", value=3.0)
    root, steps = FalsePosition(f, a, b)

st.subheader("Iterations")
st.write(steps)

st.subheader("Convergence Plot")
errors = [abs(s[1] - root) for s in steps]
plt.plot(errors, marker='o')
plt.xlabel("Iteration")
plt.ylabel("Error")
st.pyplot(plt)

st.success(f"Estimated root: {root:.6f}")