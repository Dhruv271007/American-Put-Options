# American Put Option Pricing using Binomial Trees, Neural Networks and Reinforcement Learning

Final Project for the Seasons of Code Program IIT Bombay 

Author: **Dhruv Natu**  
Department of Electrical Engineering, IIT Bombay

---

# Overview

This project studies three different approaches for pricing American Put Options and learning the optimal exercise strategy.

The implementations include:

- Cox-Ross-Rubinstein (CRR) Binomial Tree
- Neural Network Price Approximation
- Double Deep Q-Network (Double DQN) Reinforcement Learning Agent

All methods are compared under identical contract parameters whenever applicable.

---

# Project Components

## Week 4 — American Put Pricing

Implemented the Cox-Ross-Rubinstein Binomial Tree for pricing American Put options.

Features

- Risk-neutral valuation
- Early exercise
- Exercise boundary extraction
- Benchmark pricing used throughout the project

---

## Week 6 — Neural Network Price Approximation

Implemented a fully connected neural network trained on CRR-generated labels.

Features

- Synthetic option dataset generation
- Neural network regression
- Price prediction
- Comparison against CRR benchmark using

    - MAE
    - RMSE
    - Bias
    - Maximum Error

---

## Week 7 — Reinforcement Learning Environment

Developed a custom Gym-style environment for the American Put stopping problem.

Features

- Two actions

    - Hold
    - Exercise

- Correct discounted payoff
- Terminal handling
- Random trajectory generation using the CRR model

---

## Week 8 — Double Deep Q Network

Implemented a Double DQN agent to learn the optimal stopping policy.

Features

- Replay Buffer
- Target Network
- Double DQN Bellman Update
- Reward Normalization
- CUDA Acceleration
- Exercise Boundary Visualization

---

# Contract Parameters

Unless otherwise stated, experiments use

| Parameter | Value |
|-----------|------:|
| Initial Stock Price | 100 |
| Strike Price | 100 |
| Risk Free Rate | 5% |
| Volatility | 20% |
| Time to Expiry | 1 Year |
| Number of Steps | 25 |

---

# Installation

Clone the repository

```bash
git clone https://github.com/Dhruv271007/American-Put-Options
```

Enter the repository

```bash
cd American-Put-Options
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# Results

The project compares

- Binomial Tree Pricing
- Neural Network Approximation
- Reinforcement Learning Stopping Policy

using

- MAE
- RMSE
- Bias
- Maximum Error
- Policy Value
- Exercise Rate
- Average Exercise Step

Complete numerical results are available in the accompanying report.

---

# Reproducibility

Random Seed

```
42
```

Training Hyperparameters

- Episodes: 15000
- Learning Rate: 0.01
- Batch Size: 128
- Replay Buffer: 50000
- Hidden Units: 128
- Target Update Frequency: 50
- Epsilon Start: 1.0
- Epsilon Decay: 0.999

---

# Limitations

Current limitations include

- Training performed under a single contract specification
- Deep in-the-money states occur relatively infrequently during training
- Uniform replay sampling
- Limited hyperparameter search
- No prioritized replay or dueling architecture

---

# Future Work

Potential improvements include

- Prioritized Experience Replay
- Dueling Double DQN
- Distributional Reinforcement Learning
- Curriculum Learning
- Generalization across different market parameters

---

# Dependencies

- Python 3.13
- NumPy
- PyTorch
- Gymnasium
- Matplotlib
- Pandas
- Scikit-Learn

---

# Report

The complete project report is included as

```
Report.pdf
```

which contains

- methodology
- experiments
- comparisons
- figures
- discussion
- conclusions

---

# License

This project was developed for educational purposes as part of the Seasons of Code Program 
