import numpy as np


def polynomial_identifier(velocity, force):
    # Creates the matrix for polynomial with degree of len(velocity)-1
    V = np.vander(velocity, len(velocity))

    # Solve for the polynomial coefficients
    coefficients = np.linalg.solve(V, force)
    return coefficients


def polynomial_solver(values, t):
    # c is the coefficient, and i is the exponent
    return sum(c * (t ** i) for i, c in enumerate(values))


# Our Data:
velocity = [0, 2, 4, 6, 8, 10]
force = [0, 2.90, 14.80, 39.60, 74.30, 119.00]

# After getting the coefficient, we are converting each from numpy object to list object
coefficients = polynomial_identifier(velocity, force)
values = list(float(c) for c in coefficients)

# i --> values[i] = a_i, must reverse to display the proper order for polynomial
values.reverse()
print("Coefficients of the interpolating polynomial:\n", values, "\n")

# test to see if equation matches with data points
t = 0
print("Velocity: 0, Force:", polynomial_solver(values, t))
t = 2
print("Velocity: 2, Force:", polynomial_solver(values, t))
t = 4
print("Velocity: 4, Force:", polynomial_solver(values, t))
t = 6
print("Velocity: 6, Force:", polynomial_solver(values, t))
t = 8
print("Velocity: 8, Force:", polynomial_solver(values, t))
t = 10
print("Velocity: 10, Force:", polynomial_solver(values, t), "\n")


# testing for unrecorded velocities
t = 7.5
print("Velocity: 7.5, Force:", polynomial_solver(values, t) * 100)