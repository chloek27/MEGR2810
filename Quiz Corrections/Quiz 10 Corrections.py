# Question 1: A simply supported bean of length is subjected to a uniformly distributed load. 
# The deflection y(x) of the bean at a distance x from the left support is given by:
# y(x) = 1/24 * (L**3*x - 2*L**3 + x**4)
# Write Python code to use numerical methods to find the first, second, third, and fourth derivates of the deflection function.
# Evaluate the derivatives at x = 5.

import numpy as np
import matplotlib.pyplot as plt

L = 10 # length of the beam
x0 = 5 # the interval point to evaluate the derivative at.
h = 0.01 # step size

def beam_deflection(x): # defining the beam deflection function
    return (1/24) * (L**3 * x - 2 * L**3 + x**4) 


def first_derivative(f, x, h):
    return (f(x + h) - f(x - h)) / (2 * h) # Central difference formula

def second_derivative(f, x, h):
    return (f(x + h) - 2*f(x) + f(x - h)) / (h**2) #derivatives taken from lecture notes

def third_derivative(f, x, h):
    return (f(x + 2*h) - 2*f(x + h) + 2*f(x - h) - f(x - 2*h)) / (2 * h**3)

def fourth_derivative(f, x, h):
    return (f(x + 2*h) - 4*f(x + h) + 6*f(x) - 4*f(x - h) + f(x - 2*h)) / (h**4)

y1 = first_derivative(beam_deflection, x0, h) # defines the f, x, and h values
y2 = second_derivative(beam_deflection, x0, h)
y3 = third_derivative(beam_deflection, x0, h)
y4 = fourth_derivative(beam_deflection, x0, h)

print(f"First derivative: {y1:.6f}")
print(f"Second derivative: {y2:.4f}")
print(f"Third derivative: {y3:.4f}")
print(f"Fourth derivative: {y4:.4f}")