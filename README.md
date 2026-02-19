# Tri-Phasic Cyclic Cosmology

This repository contains the numerical validation scripts for the paper:
**"Emergent Cyclic Cosmology from a Discrete Tri-Phasic Microstructure: Bounce Dynamics and Multi-Scale Tests"**
by Hyun Sang-soo (Want).

## Contents

- `stability_test.py`: Verifies numerical stability of the bounce crossing algorithm by performing a grid convergence test (Corresponding to **Appendix K** of the paper).
- `parameter_robustness.py`: Calculates the BKL instability suppression factor across different stiffening phase parameters (Corresponding to **Appendix L**).

## Usage

To run the tests:

```bash
python stability_test.py
python parameter_robustness.py