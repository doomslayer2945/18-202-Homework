import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def f(z):
    return np.sin(z) * np.cos(z)

def P1(z, a):
    return - (z - a)

def P2(z, a):
    return - (z - a)

def P3(z, a):
    return - (z - a) + (2/3) * (z - a)**3


re = np.arange(-2, 2.15, 0.15)
im = np.arange(-2, 2.15, 0.15)
Re, Im = np.meshgrid(re, im)
Z = Re + 1j * Im


f_values = np.abs(f(Z))
P1_values = np.abs(P1(Z, np.pi / 2))
P2_values = np.abs(P2(Z, np.pi / 2))
P3_values = np.abs(P3(Z, np.pi / 2))

fig = plt.figure(figsize=(14, 6))

ax1 = fig.add_subplot(2, 2, 1, projection='3d')
ax1.plot_surface(Re, Im, f_values, cmap='viridis')
ax1.set_title('f(z) = |sin(z) cos(z)|')
ax1.set_xlabel('Re(z)')
ax1.set_ylabel('Im(z)')
ax1.set_zlabel('|f(z)|')

ax2 = fig.add_subplot(2, 2, 2, projection='3d')
ax2.plot_surface(Re, Im, P1_values, cmap='viridis')
ax2.set_title('P1(z) = - (z - π/2)')
ax2.set_xlabel('Re(z)')
ax2.set_ylabel('Im(z)')
ax2.set_zlabel('|P1(z)|')

ax3 = fig.add_subplot(2, 2, 3, projection='3d')
ax3.plot_surface(Re, Im, P2_values, cmap='viridis')
ax3.set_title('P2(z) = - (z - π/2)')
ax3.set_xlabel('Re(z)')
ax3.set_ylabel('Im(z)')
ax3.set_zlabel('|P2(z)|')


ax4 = fig.add_subplot(2, 2, 4, projection='3d')
ax4.plot_surface(Re, Im, P3_values, cmap='viridis')
ax4.set_title('P3(z) = - (z - π/2) + (2/3) * (z - π/2)^3')
ax4.set_xlabel('Re(z)')
ax4.set_ylabel('Im(z)')
ax4.set_zlabel('|P3(z)|')

ax3.set_ylabel('Im(z)', labelpad=20)  
ax4.set_ylabel('Im(z)', labelpad=-40) 

plt.tight_layout()
plt.show()
