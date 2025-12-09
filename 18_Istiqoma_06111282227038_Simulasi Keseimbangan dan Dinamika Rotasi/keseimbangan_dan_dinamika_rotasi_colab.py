"""
Keseimbangan dan Dinamika Rotasi
File Python ini disiapkan untuk dijalankan di Google Colab.
Isi:
- Definisi lintasan setengah-lingkaran: x(t), y(t)
- Perhitungan posisi, kecepatan numerik, kecepatan tangensial, kecepatan sudut (omega), percepatan sudut (alpha)
- Contoh momen inersia untuk beberapa bentuk (titik massa, cincin tipis, cakram padat, batang)
- Perhitungan momen gaya (tau = I * alpha), energi kinetik rotasi, dan energi kinetik translasi
- Plot hasil: lintasan, v_tan(t), omega(t), alpha(t), tau(t), energi

Cara pakai di Colab:
1. Buka Google Colab -> New Python 3 notebook
2. Salin seluruh isi file ini (Ctrl-A, Ctrl-C) lalu paste ke sel pertama Colab
3. Jalankan sel untuk melihat semua grafik dan hasil numerik

Catatan:
- Tidak memerlukan file eksternal
- Anda bisa mengganti parameter (massa, R, T, jenis benda) di bagian "Parameter" di bawah
"""

# Import library
import numpy as np
import matplotlib.pyplot as plt
from math import pi

# ---------- Parameter simulasi ----------
R = 1.0          # jari-jari lintasan (m)
m = 0.5          # massa benda (kg) — jika menggunakan model titik-massa
T = 5.0          # durasi total simulasi (s)
N = 1000         # jumlah langkah waktu

# Pilihan tipe benda untuk momen inersia: 'point', 'ring', 'solid_disk', 'rod_center'
# Jika 'point' maka I = m * R**2
body_type = 'point'

# Fungsi momen inersia untuk berbagai bentuk
def moment_of_inertia(mass, radius, body='point', length=None):
    """Mengembalikan momen inersia I sesuai bentuk yang dipilih.
    - 'point' : titik massa pada jarak radius -> I = m R^2
    - 'ring'  : cincin tipis dengan massa m dan jari-jari R -> I = m R^2 (sama dengan point)
    - 'solid_disk' : cakram padat dengan jari-jari R -> I = 0.5 m R^2
    - 'rod_center' : batang panjang L diputar pada pusat tegak lurus -> I = (1/12) m L^2 (butuh length)
    """
    if body == 'point' or body == 'ring':
        return mass * radius**2
    elif body == 'solid_disk':
        return 0.5 * mass * radius**2
    elif body == 'rod_center':
        if length is None:
            raise ValueError("Untuk 'rod_center' tentukan parameter length (panjang batang).")
        return (1/12) * mass * length**2
    else:
        raise ValueError('Tipe benda tidak dikenal: ' + str(body))

# Hitung momen inersia sesuai pilihan
I = moment_of_inertia(m, R, body=body_type, length=2*R if body_type=='rod_center' else None)

# ---------- Waktu dan lintasan ----------
dt = T / (N - 1)
 t_array = np.linspace(0, T, N)

# Gunakan definisi setengah-lingkaran: theta(t) = pi * t / T
theta = pi * t_array / T
x = R * np.cos(theta)
y = R * np.sin(theta)

# Posisi vektor sebagai array Nx2
r = np.vstack((x, y)).T  # bentuk (N, 2)

# ---------- Kecepatan numerik (beda hingga maju/centered) ----------
# Kita gunakan beda maju di interior (kecuali titik pertama/terakhir) -> gunakan central difference
v = np.zeros_like(r)
# central differences untuk interior
v[1:-1] = (r[2:] - r[:-2]) / (2 * dt)
# endpoint: forward/backward
v[0] = (r[1] - r[0]) / dt
v[-1] = (r[-1] - r[-2]) / dt

# Besar kecepatan
speed = np.linalg.norm(v, axis=1)

# Kecepatan tangensial: karena lintasan melingkar, komponen tangensial = speed
# Tetapi untuk generalitas: kita hitung v_tan sebagai komponen ortogonal terhadap radial
radial_unit = r / np.linalg.norm(r, axis=1)[:, None]  # vektor satuan radial
# Untuk kasus x,y=0 at t=0, pastikan tidak membagi nol
radial_unit[np.isnan(radial_unit)] = np.array([1.0, 0.0])

# Komponen radial (skalar) dan tangensial
v_radial = np.sum(v * radial_unit, axis=1)
v_tangential = np.sqrt(np.clip(speed**2 - v_radial**2, 0, None))

# Kecepatan sudut omega = v_tan / R (untuk lintasan hampir melingkar)
omega = v_tangential / R

# Percepatan sudut alpha (beda hingga)
alpha = np.zeros_like(omega)
alpha[1:-1] = (omega[2:] - omega[:-2]) / (2 * dt)
alpha[0] = (omega[1] - omega[0]) / dt
alpha[-1] = (omega[-1] - omega[-2]) / dt

# Momen gaya (torque) yang dibutuhkan agar terjadi alpha: tau = I * alpha
tau = I * alpha

# Energi kinetik translasi dan rotasi
K_trans = 0.5 * m * speed**2
K_rot = 0.5 * I * omega**2
K_total = K_trans + K_rot

# ---------- Cetak ringkasan numerik ----------
print('Parameter simulasi:')
print(f'  R = {R} m, m = {m} kg, T = {T} s, N = {N}')
print(f'  Tipe benda = {body_type}, I = {I:.5f} kg m^2')
print('\nContoh nilai pada beberapa waktu:')
for idx in [0, N//4, N//2, 3*N//4, N-1]:
    print(f' t={t_array[idx]:.3f} s: r=({r[idx,0]:.3f},{r[idx,1]:.3f}), v={speed[idx]:.4f} m/s, omega={omega[idx]:.4f} rad/s, alpha={alpha[idx]:.4f} rad/s^2, tau={tau[idx]:.4f} N m')

# ---------- Plot hasil ----------
plt.rcParams.update({'figure.max_open_warning': 0})
fig, axes = plt.subplots(3, 2, figsize=(12, 12))

# 1) Lintasan
ax = axes[0,0]
ax.plot(x, y)
ax.set_aspect('equal')
ax.set_title('Lintasan (setengah lingkaran)')
ax.set_xlabel('x (m)')
ax.set_ylabel('y (m)')

# 2) Kecepatan tangensial
ax = axes[0,1]
ax.plot(t_array, v_tangential)
ax.set_title('Kecepatan tangensial $v_{tan}(t)$')
ax.set_xlabel('t (s)')
ax.set_ylabel('v_tan (m/s)')

# 3) Omega
ax = axes[1,0]
ax.plot(t_array, omega)
ax.set_title('Kecepatan sudut $\omega(t)$')
ax.set_xlabel('t (s)')
ax.set_ylabel('\omega (rad/s)')

# 4) Alpha
ax = axes[1,1]
ax.plot(t_array, alpha)
ax.set_title('Percepatan sudut $\alpha(t)$')
ax.set_xlabel('t (s)')
ax.set_ylabel('\alpha (rad/s^2)')

# 5) Torque
ax = axes[2,0]
ax.plot(t_array, tau)
ax.set_title('Momen gaya $\tau(t)$')
ax.set_xlabel('t (s)')
ax.set_ylabel('\tau (N m)')

# 6) Energi
ax = axes[2,1]
ax.plot(t_array, K_trans, label='Translasi')
ax.plot(t_array, K_rot, label='Rotasi')
ax.plot(t_array, K_total, label='Total', linestyle='--')
ax.set_title('Energi kinetik')
ax.set_xlabel('t (s)')
ax.set_ylabel('Energy (J)')
ax.legend()

plt.tight_layout()
plt.show()

# ---------- Opsional: Tabel ringkasan waktu (sejumlah titik) ----------
import pandas as pd
summary_idx = np.linspace(0, N-1, 10, dtype=int)
summary = pd.DataFrame({
    't (s)': np.round(t_array[summary_idx], 4),
    'x (m)': np.round(r[summary_idx,0], 4),
    'y (m)': np.round(r[summary_idx,1], 4),
    'v (m/s)': np.round(speed[summary_idx], 6),
    'omega (rad/s)': np.round(omega[summary_idx], 6),
    'alpha (rad/s^2)': np.round(alpha[summary_idx], 6),
    'tau (N m)': np.round(tau[summary_idx], 6),
})

# Tampilkan tabel di Colab dengan baik
from IPython.display import display
print('\nRingkasan (10 titik waktu):')
display(summary)

# ---------- Catatan akhir ----------
print('\nCatatan:')
print('- Model yang digunakan mengasumsikan benda bergerak pada lintasan setengah-lingkaran dengan theta(t) = pi t / T.')
print('- Kecepatan dihitung secara numerik; untuk analitik, omega(t) = dtheta/dt = pi / T jika theta linear.')
print('- Jika theta(t) linear, maka omega konstan dan alpha = 0 sehingga tau = 0.')
print("- Anda dapat memodifikasi theta(t) untuk memasukkan variasi kecepatan sudut (mis. theta(t)=pi*(t/T)**2) dan melihat efeknya pada alpha/tau/energi.")
