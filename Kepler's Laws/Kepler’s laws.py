# Simple Kepler's Laws Visualization
import numpy as np
import matplotlib.pyplot as plt

# Ellipse parameters
a = 1.5  # semi-major axis
b = 1.0  # semi-minor axis
star_pos = (-0.5, 0)  # Star at one focus

# Angle positions (simulate planet motion along ellipse)
theta = np.linspace(0, 2*np.pi, 200)

# Parametric ellipse
x = a * np.cos(theta)
y = b * np.sin(theta)

# Adjust so star is at focus
x = x + star_pos[0]

# Simulate speed variation for Kepler's Second Law
# More points when near star (faster) and fewer when far (slower)
# We use a simple weighting: theta closer to pi (far side) → slower
weights = 1 + 0.5*np.cos(theta)
x_kepler = a * np.cos(theta * weights) + star_pos[0]
y_kepler = b * np.sin(theta * weights)

# Plot the ellipse (First Law)
plt.figure(figsize=(6,6))
plt.plot(x, y, 'b-', label='Planet Orbit (Ellipse)')
plt.plot(star_pos[0], star_pos[1], 'yo', markersize=10, label='Star (Focus)')
plt.xlabel('x position (AU)')
plt.ylabel('y position (AU)')
plt.title("Kepler's First Law: Elliptical Orbit")
plt.legend()
plt.axis('equal')
plt.grid(True)
plt.show()

# Plot “planet speed” along orbit (Second Law illustration)
plt.figure(figsize=(6,6))
plt.scatter(x_kepler, y_kepler, c=theta, cmap='viridis', s=10)
plt.plot(star_pos[0], star_pos[1], 'yo', markersize=10, label='Star (Focus)')
plt.xlabel('x position (AU)')
plt.ylabel('y position (AU)')
plt.title("Kepler's Second Law: Faster near Star, Slower far")
plt.legend()
plt.axis('equal')
plt.grid(True)
plt.show()

