import time
import numpy as np

# Fungsi untuk menghitung integral menggunakan metode Riemann
def riemann_integral(f, a, b, N):
    dx = (b - a) / N
    total = 0.0
    for i in range(N):
        x = a + i * dx
        total += f(x) * dx
    return total

# Fungsi yang akan diintegrasikan
def f(x):
    return 4 / (1 + x**2)

# Nilai referensi pi
pi_reference = 3.14159265358979323846

# Variasi nilai N
N_values = [10, 100, 1000, 10000]

# Pengujian
results = []

for N in N_values:
    start_time = time.time()
    pi_approx = riemann_integral(f, 0, 1, N)
    end_time = time.time()
    
    # Menghitung galat RMS
    rms_error = np.sqrt((pi_reference - pi_approx)**2)
    
    # Mengukur waktu eksekusi
    execution_time = end_time - start_time
    
    # Menyimpan hasil
    results.append((N, pi_approx, rms_error, execution_time))

# Menampilkan hasil pengujian
for N, pi_approx, rms_error, execution_time in results:
    print(f"N = {N}")
    print(f"Pi approximation: {pi_approx}")
    print(f"RMS error: {rms_error}")
    print(f"Execution time: {execution_time} seconds")
    print()
