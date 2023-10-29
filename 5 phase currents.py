import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Constants
freq = 1
omega = 2 * np.pi * freq

# Create a figure and two axes
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))

# Configure the plot for ax1 (Five phase currents)
ax1.set_title("Balanced five-phase currents")
ax1.set_xlim(0, 2 * np.pi)
ax1.set_ylim(-1.5, 1.5)
ax1.set_xlabel('ωt')
ax1.set_ylabel('Current')
ax1.grid(True)

# Configure the plot for ax2 (Space vector)
ax2.set_title("Space vector")
ax2.set_xlim(-3, 3)  # Adjusted x-axis limits
ax2.set_ylim(-3, 3)  # Adjusted y-axis limits
ax2.set_xlabel('Real')
ax2.set_ylabel('Imaginary')
ax2.grid(True)


# Time points
t = np.linspace(0, 2 * np.pi, 1000)

def update(frame):
    ax1.clear()
    ax1.grid(True)
    ax1.set_title("Balanced five-phase currents")
    ax1.set_xlim(0, 2 * np.pi)
    ax1.set_ylim(-1.5, 1.5)
    ax1.set_xlabel('ωt')
    ax1.set_ylabel('Current')
    
    theta = omega * t[frame]

    # Calculate five-phase currents
    phases = [np.sin(theta - i*2*np.pi/5) for i in range(5)]
    colors = ['r', 'g', 'b', 'c', 'm']
    labels = ['Ia', 'Ib', 'Ic', 'Id', 'Ie']

    for i, phase in enumerate(phases):
        ax1.plot(t[:frame+1], np.sin(omega * t[:frame+1] - i*2*np.pi/5), colors[i]+'-', label=labels[i])

    ax2.clear()
    ax2.grid(True)
    ax2.set_xlim(-3, 3)
    ax2.set_ylim(-3, 3)
    ax2.set_title("Space vector")
    ax2.set_xlabel('Real')
    ax2.set_ylabel('Imaginary')
    
    real = [phases[i] * np.cos(i*2*np.pi/5) for i in range(5)]
    imag = [phases[i] * np.sin(i*2*np.pi/5) for i in range(5)]

    sum_real = sum(real)
    sum_imag = sum(imag)

    # Draw vectors with arrow tips
    x = 0
    y = 0
    for i in range(5):
        ax2.arrow(x, y, real[i], imag[i], head_width=0.1, head_length=0.1, fc=colors[i], ec=colors[i], label=labels[i])
        x += real[i]
        y += imag[i]

    # Resultant space vector
    ax2.arrow(0, 0, sum_real, sum_imag, head_width=0.1, head_length=0.1, fc='k', ec='k', label="Resultant Vector")

    # Legend for the vectors
    ax2.legend(loc="upper right")
    ax1.legend(loc="upper right")

    return 

# Legend for the five phase currents
ax1.legend(loc="upper right")

ani = FuncAnimation(fig, update, frames=len(t), blit=False)

plt.tight_layout()
plt.show()
