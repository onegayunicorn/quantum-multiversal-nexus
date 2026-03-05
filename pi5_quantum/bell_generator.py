#!/usr/bin/env python3
"""
Pi5 Bell State Generator - Φ⁺ Φ⁻ Ψ⁺ Ψ⁻
"""

import numpy as np

class BellStateGenerator:
    def __init__(self):
        self.states = ['Φ⁺', 'Φ⁻', 'Ψ⁺', 'Ψ⁻']
        self.generated = 0
        
    def generate_bell_pair(self, state='Φ⁺'):
        if state == 'Φ⁺':
            pair = np.array([1/np.sqrt(2), 0, 0, 1/np.sqrt(2)])
        elif state == 'Φ⁻':
            pair = np.array([1/np.sqrt(2), 0, 0, -1/np.sqrt(2)])
        elif state == 'Ψ⁺':
            pair = np.array([0, 1/np.sqrt(2), 1/np.sqrt(2), 0])
        else:  # 'Ψ⁻'
            pair = np.array([0, 1/np.sqrt(2), -1/np.sqrt(2), 0])
        
        self.generated += 1
        return pair
    
    def generate_all(self):
        pairs = {}
        for state in self.states:
            pairs[state] = self.generate_bell_pair(state)
            print(f"   ✓ Generated {state} Bell pair")
        return pairs

# Generate all Bell states
if __name__ == "__main__":
    generator = BellStateGenerator()
    generator.generate_all()
    print(f"\n✅ Total Bell pairs generated: {generator.generated}")
