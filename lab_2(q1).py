# -*- coding: utf-8 -*-
"""Lab 2(Q1).ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1TW7WkDKAu-A0-Cy42MlejtEjB0ypY2_u

# Question 1
"""

!pip install control
import control as C #import control systems lib
import matplotlib.pyplot as plt
import numpy as np
import sympy as sym

#Defining all symbols
M, m , ell, g, x1, x2, x3 , x4, F = sym.symbols('M, m, ell, g, x1, x2, x3, x4, F')

phi = (4*m*ell*x4**2*sym.sin(x3) + 4*F - 3*m*g*(sym.sin(x3))*(sym.cos(x3))) / (4*(M + m) - 3*m*(sym.cos(x3)**2))
sym.pprint (phi)
print ("")
#Evaluate F,x3,x4 at equilibrium
def evaluate_at_equilibrium (f):
  return f.subs([(F,0), (x3, 0), (x4, 0)])

#derivatives of phi at equilibrium point with respect to F
dphi_F_eq = evaluate_at_equilibrium (phi.diff(F))
print (f'This is the partial derivative of \u03a6 with respect to F:')
sym.pprint (dphi_F_eq)
print ("")

#derivatives of phi at equilibrium point with respect to x3
dphi_x3_eq = evaluate_at_equilibrium (phi.diff(x3))
print (f'This is the partial derivative of \u03a6 with respect to x3:')
sym.pprint (dphi_x3_eq)
print ("")

#derivatives of phi at equilibrium point with respect to x4
dphi_x4_eq = evaluate_at_equilibrium (phi.diff(x4))
print (f'This is the partial derivative of \u03a6 with respect to x4:')
sym.pprint (dphi_x4_eq)
print ("")

psi = -3*((m*ell*x4**2*sym.sin(x3)*sym.cos(x3) + F*sym.cos(x3) - (M+m)*g*sym.sin(x3)) / (4*(M+m) - 3*m*sym.cos(x3)**2)*ell)
sym.pprint (psi)

print ("")
#Evaluate F,x3,x4 at equilibrium
def evaluate_at_equilibrium (f):
  return f.subs([(F,0), (x3, 0), (x4, 0)])

#derivatives of psi at equilibrium point with respect to F
dpsi_F_eq = evaluate_at_equilibrium (psi.diff(F))
print (f'This is the partial derivative of \u03a8 with respect to F:')
sym.pprint (dpsi_F_eq)
print ("")

#derivatives of psi at equilibrium point with respect to x3
dpsi_x3_eq = evaluate_at_equilibrium (psi.diff(x3))
print (f'This is the partial derivative of \u03a8 with respect to x3:')
sym.pprint (dpsi_x3_eq)
print ("")

#derivatives of psi at equilibrium point with respect to x4
dpsi_x4_eq = evaluate_at_equilibrium (psi.diff(x4))
print (f'This is the partial derivative of \u03a8 with respect to x4:')
sym.pprint (dpsi_x4_eq)
print ("")