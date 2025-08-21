import numpy as np
import matplotlib.pyplot as plt
from datetime import datetime, timezone
from pysolar.solar import get_altitude, get_azimuth

latitude = 40.4167047
longitude = -3.7035825

hours = np.arange(2, 23)
months = list(range(1, 13))
days = [21] * 12 
month_names = ['Jan', 'Fév', 'Mar', 'Avr', 'Mai', 'Juin', 'Juil', 'Août', 'Sept', 'Oct', 'Nov', 'Déc']

azimuths_by_month = []
altitudes_by_month = []

for month, day in zip(months, days):
    azimuths = []
    altitudes = []
    for hour in hours:
        dt = datetime(2024, month, day, hour, 0, 0, tzinfo=timezone.utc)
        az = get_azimuth(latitude, longitude, dt)
        alt = get_altitude(latitude, longitude, dt)
        azimuths.append(az)
        altitudes.append(alt)
    azimuths_by_month.append(azimuths)
    altitudes_by_month.append(altitudes)

plt.figure(figsize=(16, 10))

used_positions = []
for i, (az, alt) in enumerate(zip(azimuths_by_month, altitudes_by_month)):
    az = np.array(az)
    alt = np.array(alt)
    mask = ~np.isnan(az)
    az = az[mask]
    alt = alt[mask]
    if len(az) > 1:
        plt.plot(az, alt, 'r', lw=1)
        max_idx = np.argmax(alt)
            
for h in range(4, 21):
    az_line = []
    alt_line = []
    for month, day in zip(months, days):
        dt = datetime(2024, month, day, h, 0, 0, tzinfo=timezone.utc)
        az = get_azimuth(latitude, longitude, dt)
        alt = get_altitude(latitude, longitude, dt)
        if alt > 0:
            az_line.append(az)
            alt_line.append(alt)

plt.xlabel("Azimut (°)")
plt.ylabel("Hauteur angulaire (°)")
plt.xlim(0, 400)
plt.ylim(0, 80)
plt.title("Diagramme solaire – Madrid 2024")
plt.xticks([60, 90, 120, 150, 180, 210, 240, 270, 300])
plt.grid(True, linestyle='--', alpha=0.5)
plt.tight_layout()
plt.show()
