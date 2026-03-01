# Model Specification v1.1

## State Variables
- x1 (C): Perception-Capitalization, [0,1]
- x2 (M): Memory-Consolidation, [0,∞)
- x3 (D): Decision-Arbitration, [0,1]  
- x4 (L): Life History-Saturation (control), [0,1]

## Critical Parameters

| Param | Range | Role |
|-------|-------|------|
| ζ | [0.05, 0.3] | M consolidation (blow-up prevention) |
| ι | [0.1, 1.0] | D-L inhibition (standard=0.6, adversarial=0.2) |
| θ | [0.2, 1.0] | D-M coupling |
| κ | [0.1, 1.0] | D decay |

## Bifurcation Hypothesis

- **Forward transition**: L_c^+ ≈ 0.8
- **Reverse transition**: L_r^- ≈ 0.6  
- **Hysteresis width**: ΔL ≈ 0.2

## Layer 3 Note

x3 may be functionally emergent from x2-x4 coupling:
x3* = [θ·(x2/(1+x2)) - ι·x4]/κ

3D reduction preserves 89% variance but sacrifices granularity.
