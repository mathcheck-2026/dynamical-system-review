# Dynamical System Review: Quadra-Filter Model v1.1

**Status**: Active Review | **Model Version**: v1.1 | **Last Updated**: 2026-03-01

External mathematical audit for Cognitive Capital Life Cycle (CCLC) theory.

## Model Specification

4D Coupled SDE System:
dx1/dt = -α·x1 + β·(x2/(1+x2)) + γ/(1+δ·x4)
dx2/dt = ε·x1 - ζ·x2·(1+η·x4)
dx3/dt = θ·(x2/(1+x2)) - ι·x4 - κ·x3
dx4/dt = λ·max(x3,0) - μ·x4 + ν·x1

**Critical Update v1.1**: Added Q6 (Adversarial Testing) to distinguish true bifurcation from parameter freezing.

## UHT-v1.2 Protocol

Unified Hysteresis Testing Protocol validates:
- **Test A**: Adversarial activation (low inhibition i=0.2)
- **Test C**: Hysteresis width measurement (expect ΔL ∈ [0.15, 0.25])
- **Test D**: Parameter sensitivity (±10% perturbation)

### Quick Start
```bash
pip install numpy scipy
python uht_protocol_v12.py

Review Questions (Open)
Identifiability: Are ζ and η structurally identifiable?
Stability: Does x2 remain bounded given ζ ∈ [0.05, 0.3]?
Model Reduction: Is 3D reduction (eliminating x3) valid?
Bifurcation Type: Saddle-node vs. transcritical?
Noise Robustness: Stability under σ=0.1?
Adversarial: Is bifurcation robust to low inhibition (ι=0.2)?
Links
StackExchange: Question 674997
Paper: CCLC Theory v10.1 (BBS Target Article)
Contact: See paper Author Note for theoretical questions; GitHub Issues for mathematical technicalities

Symbol Map
| Paper  | Code      | Description               |
| ------ | --------- | ------------------------- |
| C      | x1        | Perception-Capitalization |
| M      | x2        | Memory-Consolidation      |
| D      | x3        | Decision-Arbitration      |
| L      | x4        | Life History-Saturation   |
| η\_eff | (derived) | Effective plasticity      |

