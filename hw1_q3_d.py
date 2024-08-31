import matplotlib.pyplot as plt
import numpy as np

def plot_complex_numbers(complex_numbers, labels=None):
    fig, ax = plt.subplots(figsize=(6, 6))
    axis_limit = 40
    colors = plt.cm.viridis(np.linspace(0, 1, len(complex_numbers)))

    for i, number in enumerate(complex_numbers):
        real_part = np.real(number)
        imaginary_part = np.imag(number)

        custom_label = f'{real_part} + {imaginary_part}j'
        if labels and i < len(labels):
            custom_label += f' ({labels[i]})'
        color = colors[i]

        ax.plot(real_part, imaginary_part, 'o', markersize=5, color=color, label=custom_label)

        ax.plot([0, real_part], [0, imaginary_part], color=color)

    ax.annotate('', xy=(-axis_limit, 0), xytext=(axis_limit, 0),
                arrowprops=dict(arrowstyle='<->', linewidth=2, color='k'))
    ax.annotate('', xy=(0, -axis_limit), xytext=(0, axis_limit),
                arrowprops=dict(arrowstyle='<->', linewidth=2, color='k'))

    ax.set_xlabel('Real', fontsize=12, fontweight='bold')
    ax.set_ylabel('Imaginary', fontsize=12, fontweight='bold')
    ax.set_title('Complex Numbers on the Complex Plane', fontsize=14, fontweight='bold')

    ax.grid(True)
    ax.legend()
    ax.set_aspect('equal')  
    ax.set_xlim(-axis_limit, axis_limit)
    ax.set_ylim(-axis_limit, axis_limit)

    plt.show()


complex_numbers = [-31.75+35.26j]
labels = ['z1·z2']
plot_complex_numbers(complex_numbers, labels)
