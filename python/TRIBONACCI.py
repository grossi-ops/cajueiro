import numpy as np

# ====================== TRIBONACCI CHAIN GENERATION ======================
def generate_tribonacci_word(N=500):
    rules = {1: [1, 2], 2: [1, 3], 3: [1]}
    word = [1]
    while len(word) < N:
        new_word = []
        for s in word:
            new_word.extend(rules.get(s, [s]))
        word = new_word
    return np.array(word[:N])

# ====================== IMAGINARY-TIME RELAXATION ======================
def imaginary_time_relax(beta, N=500, dt=0.05, max_steps=5000, tol=1e-6):
    # Initial localized Gaussian (common starting point for soliton-like states)
    j = np.arange(N)
    psi = np.exp(-((j - N/2)**2) / (2 * (N/10)**2)) + 0j
    psi /= np.sqrt(np.sum(np.abs(psi)**2))
    
    prev_max = 0.0
    for step in range(max_steps):
        # Linear Laplacian (hopping = 1, open boundaries)
        lap = np.zeros(N, dtype=complex)
        lap[1:] -= psi[:-1]
        lap[:-1] -= psi[1:]
        
        # FOCUSING nonlinearity (attractive cubic term)
        nl = -beta * np.abs(psi)**2 * psi
        
        dpsi = lap + nl
        psi -= dt * dpsi
        
        # Renormalize
        norm = np.sqrt(np.sum(np.abs(psi)**2))
        psi /= norm
        
        max_amp = np.max(np.abs(psi))
        if step % 500 == 0:
            if np.abs(max_amp - prev_max) < tol:
                break
            prev_max = max_amp
    
    return max_amp, step + 1

# ====================== BIFURCATION SCAN ======================
N = 500
word = generate_tribonacci_word(N)
print(f"Tribonacci chain generated: {len(word)} sites")
print(f"First 20 sites: {word[:20]}\n")

betas = np.linspace(0.0, 2.0, 11)
print("Bifurcation scan over nonlinearity β (focusing DNLS on tribonacci chain)\n")
print("β     | max |ψ|   | steps")
print("-" * 30)

results = []
for beta in betas:
    max_amp, steps = imaginary_time_relax(beta, N)
    results.append((round(beta, 2), round(max_amp, 4), steps))
    print(f"{beta:5.2f} | {max_amp:7.4f} | {steps:5d}")

print("\nSummary table:")
for b, amp, s in results:
    print(f"{b:5.2f} | {amp:7.4f} | {s:5d}")
