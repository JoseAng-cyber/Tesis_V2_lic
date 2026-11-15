import matplotlib.pyplot as plt

tiempos = [
    0.38, 3.51, 6.56, 9.65, 12.78, 15.87, 18.97, 22.07, 25.15, 28.23,
    31.36, 34.45, 37.54, 40.62, 43.76, 46.91, 49.99, 53.15, 56.27, 59.39,
    62.46, 65.52, 68.56, 71.64, 74.73, 77.83, 80.92, 84.02, 87.13, 90.22,
    93.3, 96.41, 99.49, 102.57, 105.69, 108.76, 111.84, 114.94, 118.0, 121.12,
    124.2, 127.23, 130.34, 133.42, 136.49, 139.58, 142.67, 145.78, 148.87, 151.97,
    155.04, 158.13, 161.29, 164.41, 167.5, 170.6, 173.73, 176.79, 179.9, 182.97,
    186.07, 189.16, 192.26, 195.38, 198.52, 201.62, 204.74, 207.83, 210.91, 214.04,
    217.14, 220.22, 223.31, 226.43, 229.55, 232.65, 235.76, 238.87
]

temperaturas = [
    25.43, 25.74, 28.18, 32.66, 38.6, 45.08, 52.17, 59.51, 66.35, 73.58,
    80.64, 87.43, 93.65, 100.09, 106.1, 112.0, 117.66, 123.11, 128.35, 133.32,
    137.94, 142.59, 146.79, 151.09, 154.99, 159.0, 162.89, 166.65, 170.23, 173.71,
    177.06, 180.38, 183.46, 186.67, 187.92, 187.08, 184.62, 182.33, 181.73, 182.36,
    183.89, 186.02, 188.31, 189.77, 190.91, 191.82, 192.27, 192.73, 193.64, 194.12,
    195.0, 195.09, 195.45, 195.45, 195.45, 195.0, 195.0, 195.0, 195.0, 195.0,
    195.0, 195.0, 195.0, 195.0, 195.0, 195.0, 195.0, 195.0, 195.0, 195.0,
    195.0, 195.11, 195.03, 195.0, 195.0, 195.03, 195.0, 195.0
]

plt.rcParams.update({
    "font.family": "serif",
    "font.serif": ["Latin Modern Roman", "DejaVu Serif"],
    "mathtext.fontset": "cm",
    "axes.edgecolor": "#333333",
    "axes.linewidth": 0.6,
})

# 1. Área física más compacta (ancho 4.5 pulgadas, alto 3.2 pulgadas)
fig, ax = plt.subplots(figsize=(4.5, 3.2), dpi=300)

ax.axhline(195.0, color='#e66122', linestyle='--', linewidth=1.1, label=r'Setpoint ($195\ ^\circ\mathrm{C}$)')
ax.axvline(155.04, color='#16a05d', linestyle='-.', linewidth=1.0, label=r'Tiempo subida ($155.0\ \mathrm{s}$)')
ax.plot(tiempos, temperaturas, color='#1e64c8', linestyle='-', linewidth=1.4, label='Temperatura medida')

ax.spines['top'].set_visible(False)
ax.spines['right'].set_visible(False)

ax.tick_params(axis='both', which='major', direction='out', length=3, width=0.6, labelsize=7.5, colors='#333333')
ax.grid(True, linestyle='-', linewidth=0.4, color='#e5e5e5')
ax.set_axisbelow(True)

ax.set_xlabel(r'Tiempo ($\mathrm{s}$)', fontsize=8.5, labelpad=4)
ax.set_ylabel(r'Temperatura ($^\circ\mathrm{C}$)', fontsize=8.5, labelpad=4)

ax.set_xlim(0, 240)
ax.set_ylim(20, 215)
ax.set_xticks([0, 50, 100, 150, 200])
ax.set_yticks([25, 50, 75, 100, 125, 150, 175, 200])

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

# 2. Elimina los espacios en blanco sobrantes alrededor de la figura al guardar
plt.savefig('respuesta_termica_hotend.pdf', bbox_inches='tight', pad_inches=0.05)
plt.savefig('respuesta_termica_hotend.png', dpi=300, bbox_inches='tight', pad_inches=0.05)
plt.show()
