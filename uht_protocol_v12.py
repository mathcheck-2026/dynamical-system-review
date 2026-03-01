"""
Unified Hysteresis Testing Protocol v1.2 (UHT-v1.2)
for Quadra-Filter Model Symmetry-Breaking Validation

Model Variables:
x1 = C (Perception-Capitalization) [0,1]
x2 = M (Memory-Consolidation) [0,inf)  
x3 = D (Decision-Arbitration) [0,1]
x4 = L (Life History-Saturation) [0,1] (control parameter)
"""

import numpy as np
from scipy.integrate import odeint
from typing import Dict, Tuple, List, Optional
import warnings
warnings.filterwarnings('ignore')

class QuadraFilterModel:
    def __init__(self, params: Optional[Dict] = None):
        self.default_params = {
            'alpha': 0.3, 'beta': 0.6, 'gamma': 0.4, 'delta': 1.2,
            'epsilon': 0.5, 'zeta': 0.15, 'eta': 1.0, 'theta': 0.7,
            'iota': 0.6, 'kappa_param': 0.4, 'lambda_param': 0.8,
            'mu': 0.2, 'nu': 0.3
        }
        self.params = params if params else self.default_params
        self.sigma = 0.1
        
    def dynamics(self, state, t, L_fixed=None):
        x1, x2, x3, x4 = state
        p = self.params
        if L_fixed is not None:
            x4 = L_fixed
        
        dx1 = (-p['alpha']*x1 + p['beta']*(x2/(1+x2)) + 
               p['gamma']/(1+p['delta']*x4))
        dx2 = (p['epsilon']*x1 - p['zeta']*x2*(1+p['eta']*x4))
        dx3 = (p['theta']*(x2/(1+x2)) - p['iota']*x4 - p['kappa_param']*x3)
        
        if L_fixed is not None:
            dx4 = 0.0
        else:
            dx4 = (p['lambda_param']*max(x3,0) - p['mu']*x4 + p['nu']*x1)
        
        return [dx1, dx2, dx3, dx4]

class UHTProtocol:
    def __init__(self, model: QuadraFilterModel):
        self.model = model
        
    def check_convergence(self, trajectory: np.ndarray, 
                         tolerance: float = 0.001, window: int = 100):
        if len(trajectory) < window:
            return False, np.inf
        final = trajectory[-window:, 0]
        max_deriv = np.max(np.abs(np.diff(final)))
        std_dev = np.std(final)
        return (max_deriv < tolerance and std_dev < 0.05), std_dev
    
    def adversarial_test(self, iota_low: float = 0.2) -> Dict:
        """Test A: Low inhibition to detect parameter freezing"""
        orig = self.model.params.copy()
        self.model.params['iota'] = iota_low
        self.model.params['theta'] = 0.9
        self.model.params['kappa_param'] = 0.3
        
        # Test at L=0.6
        sol = odeint(self.model.dynamics, [0.5, 1.0, 0.5, 0.6], 
                    np.arange(0, 1000, 0.01), args=(0.6,))
        x3_06 = sol[-1, 2]
        
        # Test at L=0.9
        sol = odeint(self.model.dynamics, sol[-1], 
                    np.arange(0, 1000, 0.01), args=(0.9,))
        x3_09 = sol[-1, 2]
        
        self.model.params = orig
        
        return {
            'x3_at_06': x3_06, 'x3_at_09': x3_09,
            'true_bifurcation': (x3_06 > 0.2 and x3_09 < 0.05)
        }
    
    def hysteresis_scan(self, L_vals: np.ndarray = np.linspace(0,1,21)):
        """Test C: Hysteresis measurement"""
        results = {'up': [], 'down': []}
        state = [0.5, 1.0, 0.5, 0.0]
        
        # Upward scan
        for L in L_vals:
            sol = odeint(self.model.dynamics, state, 
                        np.arange(0, 500, 0.01), args=(L,))
            state = sol[-1].tolist()
            state[3] = L
            results['up'].append(state[0])
        
        # Downward scan
        state = [results['up'][-1], 1.5, 0.0, 1.0]
        for L in L_vals[::-1]:
            sol = odeint(self.model.dynamics, state,
                        np.arange(0, 500, 0.01), args=(L,))
            state = sol[-1].tolist()
            state[3] = L
            results['down'].append(state[0])
        
        # Calculate width
        up_arr, down_arr = np.array(results['up']), np.array(results['down'])
        transition_up = 0.05 * np.argmin(np.diff(up_arr))
        transition_down = 0.05 * np.argmax(np.diff(down_arr))
        width = abs(transition_up - transition_down)
        
        return {
            'width': width, 'L_c_plus': transition_up,
            'L_r_minus': transition_down, 'up': results['up'], 
            'down': results['down']
        }

def run_uht_v12():
    model = QuadraFilterModel()
    uht = UHTProtocol(model)
    
    print("UHT-v1.2 Protocol Starting...")
    test_a = uht.adversarial_test()
    print(f"Test A (Adversarial): x3(0.6)={test_a['x3_at_06']:.3f}, "
          f"x3(0.9)={test_a['x3_at_09']:.3f}")
    print(f"True Bifurcation: {test_a['true_bifurcation']}")
    
    test_c = uht.hysteresis_scan()
    print(f"\nTest C (Hysteresis): Width={test_c['width']:.3f}")
    print(f"L_c^+ = {test_c['L_c_plus']:.3f}, L_r^- = {test_c['L_r_minus']:.3f}")
    
    if 0.15 <= test_c['width'] <= 0.25:
        print("✓ PASS: Hysteresis in predicted range")
    else:
        print("✗ FAIL: Outside predicted range [0.15, 0.25]")
    
    return {'test_a': test_a, 'test_c': test_c}

if __name__ == "__main__":
    results = run_uht_v12()
