# import numpy as np
# import matplotlib.pyplot as plt
# from matplotlib.animation import FuncAnimation

# # Constants
# freq = 1
# omega = 2 * np.pi * freq

# # Create a figure and two axes
# fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))

# # Configure the plot for ax1 (Three phase currents)
# ax1.set_title("Balanced three-phase currents")
# ax1.set_xlim(0, 2 * np.pi)
# ax1.set_ylim(-1.5, 1.5)
# ax1.set_xlabel('ωt')
# ax1.set_ylabel('Current')
# ax1.grid(True)

# # Configure the plot for ax2 (Space vector)
# ax2.set_title("Space vector")
# ax2.set_xlim(-1.5, 1.5)
# ax2.set_ylim(-1.5, 1.5)
# ax2.set_xlabel('Real')
# ax2.set_ylabel('Imaginary')
# ax2.grid(True)

# # Initial plots for each phase and the space vector
# line_a, = ax1.plot([], [], 'r-', label="Phase A")
# line_b, = ax1.plot([], [], 'g--', label="Phase B")
# line_c, = ax1.plot([], [], 'b--', label="Phase C")
# vector_a, = ax2.plot([], [], 'ro-', label="Vector A")
# vector_b, = ax2.plot([], [], 'go-', label="Vector B")
# vector_c, = ax2.plot([], [], 'bo-', label="Vector C")
# vector_sum, = ax2.plot([], [], 'mo-', label="Space Vector")

# # Time points
# t = np.linspace(0, 2 * np.pi, 1000)
# ax1.legend()
# ax2.legend()

# def init():
#     line_a.set_data([], [])
#     line_b.set_data([], [])
#     line_c.set_data([], [])
#     vector_a.set_data([], [])
#     vector_b.set_data([], [])
#     vector_c.set_data([], [])
#     vector_sum.set_data([], [])
#     return line_a, line_b, line_c, vector_a, vector_b, vector_c, vector_sum

# def update(frame):
#     theta = omega * t[frame]

#     # Calculate three-phase currents
#     i_a = np.sin(theta)
#     i_b = np.sin(theta - 2 * np.pi / 3)
#     i_c = np.sin(theta + 2 * np.pi / 3)

#     line_a.set_data(t[:frame+1], np.sin(omega * t[:frame+1]))
#     line_b.set_data(t[:frame+1], np.sin(omega * t[:frame+1] - 2 * np.pi / 3))
#     line_c.set_data(t[:frame+1], np.sin(omega * t[:frame+1] + 2 * np.pi / 3))
    
#     # Real and Imaginary components of the vectors
#     real_a = i_a
#     imag_a = 0
#     real_b = i_b * np.cos(2 * np.pi / 3)
#     imag_b = i_b * np.sin(2 * np.pi / 3)
#     real_c = i_c * np.cos(-2 * np.pi / 3) + real_a + real_b
#     imag_c = i_c * np.sin(-2 * np.pi / 3) + imag_a + imag_b

#     vector_a.set_data([0, real_a], [0, imag_a])
#     vector_b.set_data([real_a, real_a + real_b], [imag_a, imag_a + imag_b])
#     vector_c.set_data([real_a + real_b, real_c], [imag_a + imag_b, imag_c])
    
#     # Resultant space vector
#     vector_sum.set_data([0, real_c], [0, imag_c])

#     return line_a, line_b, line_c, vector_a, vector_b, vector_c, vector_sum

# ani = FuncAnimation(fig, update, frames=len(t), init_func=init, blit=True)

# plt.tight_layout()
# plt.show()



import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Constants
freq = 1
omega = 2 * np.pi * freq

# Create a figure and two axes
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))

# Configure the plot for ax1 (Three phase currents)
ax1.set_title("Balanced three-phase currents")
ax1.set_xlim(0, 2 * np.pi)
ax1.set_ylim(-1.5, 1.5)
ax1.set_xlabel('ωt')
ax1.set_ylabel('Current')
ax1.grid(True)

# Configure the plot for ax2 (Space vector)
ax2.set_title("Space vector")
ax2.set_xlim(-1.5, 1.5)
ax2.set_ylim(-1.5, 1.5)
ax2.set_xlabel('Real')
ax2.set_ylabel('Imaginary')
ax2.grid(True)

# Time points
t = np.linspace(0, 2 * np.pi, 1000)

line_a, = ax1.plot([], [], 'r-', label="Phase A")
line_b, = ax1.plot([], [], 'g-', label="Phase B")
line_c, = ax1.plot([], [], 'b-', label="Phase C")

def init():
    line_a.set_data([], [])
    line_b.set_data([], [])
    line_c.set_data([], [])
    return line_a, line_b, line_c

def update(frame):
    ax1.clear()
    ax1.grid(True)
    ax1.set_title("Balanced three-phase currents")
    ax1.set_xlim(0, 2 * np.pi)
    ax1.set_ylim(-1.5, 1.5)
    ax1.set_xlabel('ωt')
    ax1.set_ylabel('Current')
    
    theta = omega * t[frame]

    # Calculate three-phase currents
    i_a = np.sin(theta)
    i_b = np.sin(theta - 2 * np.pi / 3)
    i_c = np.sin(theta + 2 * np.pi / 3)

    ax1.plot(t[:frame+1], np.sin(omega * t[:frame+1]), 'r-', label="Ia")
    ax1.plot(t[:frame+1], np.sin(omega * t[:frame+1] - 2 * np.pi / 3), 'g-', label="Ib")
    ax1.plot(t[:frame+1], np.sin(omega * t[:frame+1] + 2 * np.pi / 3), 'b-', label="Ic")

    ax2.clear()
    ax2.grid(True)
    ax2.set_xlim(-1.5, 1.5)
    ax2.set_ylim(-1.5, 1.5)
    ax2.set_title("Space vector")
    ax2.set_xlabel('Real')
    ax2.set_ylabel('Imaginary')
    
    # Real and Imaginary components of the vectors
    real_a = i_a
    imag_a = 0
    real_b = i_b * np.cos(2 * np.pi / 3)
    imag_b = i_b * np.sin(2 * np.pi / 3)
    real_c = i_c * np.cos(-2 * np.pi / 3) + real_a + real_b
    imag_c = i_c * np.sin(-2 * np.pi / 3) + imag_a + imag_b

    # Draw vectors with arrow tips
    ax2.arrow(0, 0, real_a, imag_a, head_width=0.1, head_length=0.1, fc='r', ec='r', label="Ia")
    ax2.arrow(real_a, imag_a, real_b, imag_b, head_width=0.1, head_length=0.1, fc='g', ec='g', label="Ib")
    ax2.arrow(real_a + real_b, imag_a + imag_b, real_c - real_a - real_b, imag_c - imag_a - imag_b, head_width=0.1, head_length=0.1, fc='b', ec='b', label="Ic")
    ax2.arrow(0, 0, real_c, imag_c, head_width=0.1, head_length=0.1, fc='m', ec='m', label="Resultant Vector")

    # Legend for the vectors
    ax2.legend(loc="upper right")
    ax1.legend(loc="upper right")

    return line_a, line_b, line_c

# Legend for the three phase currents
ax1.legend(loc="upper right")

ani = FuncAnimation(fig, update, frames=len(t), init_func=init, blit=False)

plt.tight_layout()
plt.show()

