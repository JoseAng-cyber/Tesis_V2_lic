import re
from datetime import datetime

t0 = None
tiempos = []
temperaturas_hotend = []
temperaturas_cama_cuerpo = []

with open("prueba_termica.log") as f:
    for line in f:
        # Detectar el tiempo t0 con el comando de inicio del hotend
        if "M104 S" in line:
            t0 = datetime.strptime(line.split(" - ")[0], "%Y-%m-%d %H:%M:%S,%f")
        
        # Expresión regular actualizada para capturar T (Hotend) y B (Sensor auxiliar en cuerpo)
        m = re.match(
            r"^(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2},\d{3}) - RECV: ok T:([\d.]+)\s*/[\d.]+\s+B:([\d.]+)", 
            line
        )
        
        if m and t0:
            ts = datetime.strptime(m.group(1), "%Y-%m-%d %H:%M:%S,%f")
            tiempos.append(round((ts - t0).total_seconds(), 2))
            temperaturas_hotend.append(float(m.group(2)))
            temperaturas_cama_cuerpo.append(float(m.group(3)))

print("--- EXTRACCIÓN COMPLETADA ---")
print(f"Total de muestras capturadas: {len(tiempos)}")
print("tiempos =", tiempos)
print("temperaturas_hotend =", temperaturas_hotend)
print("temperaturas_sensor_b =", temperaturas_cama_cuerpo)
