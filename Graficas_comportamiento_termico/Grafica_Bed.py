import matplotlib.pyplot as plt

# Datos de ejemplo para el calentamiento de la cama de 25 °C a 50 °C
tiempos_cama = [
    0.0, 15.0, 30.0, 45.0, 60.0, 75.0, 90.0, 105.0, 120.0, 
    135.0, 150.0, 165.0, 180.0, 195.0, 210.0, 225.0, 240.0
]
temperaturas_cama = [
    25.0, 25.2, 25.8, 27.1, 29.3, 32.0, 35.1, 38.4, 41.5, 
    44.2, 46.5, 48.2, 49.3, 49.8, 50.0, 50.0, 50.0
]

# Configuración de estilo académico idéntica
plt.rcParams.update({
    "font.family": "serif",
    "font.serif": ["Latin Modern Roman", "DejaVu Serif"],
    "mathtext.fontset": "cm",
    "axes.edgecolor": "#333333",
    "axes.linewidth": 0.6,
})

fig, ax = plt.subplots(figsize=(4.5, 3.2), dpi=300)

ax.plot(tiempos_cama, temperaturas_cama, color='#1e64c8', linestyle='-', linewidth=1.4, label='Temp. Cama')
ax.axhline(50.0, color='#e66122', linestyle='--', linewidth=1.1, label=r'Setpoint Cama ($50\ ^\circ\mathrm{C}$)')
ax.axvline(210.0, color='#16a05d', linestyle='-.', linewidth=1.0, label=r'Estabilización ($210\ \mathrm{s}$)')

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

ax.tick_params(axis='both', which='major', direction='out', length=3, width=0.6, labelsize=7.5, colors='#333333')
ax.grid(True, linestyle='-', linewidth=0.4, color='#e5e5e5')
ax.set_axisbelow(True)

ax.set_xlabel(r'Tiempo ($\mathrm{s}$)', fontsize=8.5, labelpad=4)
ax.set_ylabel(r'Temperatura ($^\circ\mathrm{C}$)', fontsize=8.5, labelpad=4)

ax.set_xlim(0, 240)
ax.set_ylim(20, 60)
ax.set_xticks([0, 50, 100, 150, 200])
ax.set_yticks([20, 30, 40, 50, 60])

ax.legend(
    loc='lower right',
    frameon=True,
    facecolor='white',
    edgecolor='none',
    framealpha=0.95,
    fontsize=7,
    handlelength=1.8
)

plt.tight_layout()
plt.savefig('respuesta_termica_cama.pdf', bbox_inches='tight', pad_inches=0.05)
plt.savefig('respuesta_termica_cama.png', dpi=300, bbox_inches='tight', pad_inches=0.05)
plt.show()
