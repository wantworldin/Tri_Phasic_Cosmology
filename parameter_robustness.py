import numpy as np

def calculate_suppression(w_s, N_s):
    """
    Calculates the BKL anisotropy suppression factor S.
    Formula: S = exp(-3 * (w_s - 1) * N_s)
    """
    exponent = -3 * (w_s - 1) * N_s
    suppression_factor = np.exp(exponent)
    return suppression_factor

def main():
    print("=== Parameter Robustness Test (Appendix L) ===")
    print("Checking stability against shear anisotropy (BKL instability)")
    print(f"{'Parameters':<25} {'Suppression S':<20} {'Verdict'}")
    print("-" * 65)
    
    test_cases = [
        (1.5, 2.0, "Marginal"),
        (2.0, 3.0, "Stable (Benchmark)"),
        (3.0, 4.0, "Very Stable")
    ]
    
    for w_s, N_s, verdict in test_cases:
        S = calculate_suppression(w_s, N_s)
        param_str = f"ws={w_s}, Ns={N_s}"
        
        # Scientific notation for very small numbers
        if S < 1e-3:
            s_str = f"{S:.1e}"
        else:
            s_str = f"{S:.4f}"
            
        print(f"{param_str:<25} {s_str:<20} {verdict}")

if __name__ == "__main__":
    main()