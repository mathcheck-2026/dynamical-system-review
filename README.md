# dynamical-system-review
Mathematical review of coupled SDE system with saturation functions
# Coupled Nonlinear SDE System - Mathematical Review

## System Description

Four-dimensional coupled stochastic differential equation system with saturation functions:

$$
\begin{cases}
\frac{dx_1}{dt} = -a x_1 + b \frac{x_2}{1+x_2} + c \frac{1}{1+d x_4} + \xi_1(t) \\
\frac{dx_2}{dt} = e x_1 - f x_2(1 + g x_4) + \xi_2(t) \\
\frac{dx_3}{dt} = h \frac{x_2}{1+x_2} - i x_4 - j x_3 + \xi_3(t) \\
\frac{dx_4}{dt} = k \max(x_3,0) - m x_4 + n x_1 + \xi_4(t)
\end{cases}
$$

## Constraints

- $x_1, x_3 \in [0,1]$ (bounded)
- $x_2 \in [0, \infty)$ (accumulating)
- $x_4 \in [0,1]$ (normalized)
- $\xi(t) \sim \mathcal{N}(0, \sigma^2)$, $\sigma \in [0, 0.1]$

## Parameters

| Parameter | Range | Description |
|-----------|-------|-------------|
| $a, f, m$ | [0.1, 0.5] | Decay rates |
| $b, e, h, k$ | [0.2, 1.0] | Coupling strengths |
| $c, n$ | [0.1, 0.8] | Cross-coupling |
| $d, g$ | [0.5, 2.0] | Nonlinear modulation |
| $i, j$ | [0.1, 1.0] | Inhibition |

## Key Questions

1. **Identifiability**: Are all 12 parameters identifiable? Potential collinearity between $f$ and $g$?
2. **Stability**: Fixed points, limit cycles, or finite-time blow-up for $x_2$?
3. **Reduction**: Can $x_3$ be eliminated via algebraic substitution without losing bifurcation behavior?
4. **Bifurcation**: Saddle-node bifurcation as $x_4$ increases?
5. **Noise**: Robustness of attractors at $\sigma = 0.1$?

## External Review

- **StackExchange**: [Cross Validated Post](https://stats.stackexchange.com/questions/674997/)
- **Status**: Awaiting community feedback

## License

MIT License - Open for academic review and validation
