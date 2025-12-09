import numpy as np
import matplotlib.pyplot as plt

k = 10      # konstanta pegas (N/m)
m = 1       # massa benda (kg)
x = 5.0     # posisi awal (m)
v = 0.0     # kecepatan awal (m/s)
dt = 0.01   # langkah waktu
t_max = 10  # durasi simulasi

time = [0]
x_list = [x]

t = 0
while t < t_max:
    a = -(k/m) * x        # percepatan berdasarkan hukum Hooke
    v = v + a * dt        # update kecepatan
    x = x + v * dt        # update posisi
    t += dt

    time.append(t)
    x_list.append(x)

plt.figure()
plt.plot(time, x_list)
plt.title("Simulasi Osilasi Pegas (Metode Finite Difference)")
plt.xlabel("Waktu (s)")
plt.ylabel("Perpindahan (m)")
plt.grid(True)
plt.show()
