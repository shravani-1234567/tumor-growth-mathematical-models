# Quantitative Analysis of Tumor Evolution Using Mathematical Models

## Overview

This project implements mathematical models to study tumor growth, treatment response, and cancer invasion using Python.

The project demonstrates how mathematical equations can be translated into computational models and visualized using graphs.

## Models Implemented

### 1. Exponential Growth Model

Models tumor growth when the growth rate is proportional to the current tumor size.

*Python file:* exponential_growth.py

*Result:* Exponential increase in tumor size over time.

---

### 2. Logistic Growth Model

Models tumor growth while considering a limiting carrying capacity.

*Python file:* logistic_growth.py

*Result:* Tumor growth increases initially and gradually approaches the carrying capacity.

---

### 3. Gompertz Growth Model

Models tumor growth with a growth rate that decreases as the tumor becomes larger.

*Python file:* gompertz_growth.py

*Result:* Tumor growth increases rapidly initially and then slows down.

---

### 4. Dynamic Carrying Capacity Model

Models tumor growth using a carrying capacity that changes with time.

*Python file:* dynamic_carrying_capacity.py

*Result:* Tumor growth changes according to the time-dependent carrying capacity.

---

### 5. Tumor Treatment Model

Models tumor growth while including a treatment-related reduction term.

*Python file:* tumor_treatment.py

*Result:* Demonstrates the effect of treatment on tumor growth.

---

### 6. Cancer Invasion PDE Model

Uses a system of partial differential equations to represent cancer-cell concentration, another interacting variable, and tissue/environment dynamics in space and time.

*Python file:* cancer_invasion_pde.py

*Result:* A spatial visualization of cancer-cell concentration.

## Technologies Used

- Python
- NumPy
- Matplotlib
- SymPy
- Visual Studio Code
- Git
- GitHub

## Project Structure

```text
Tumor Growth/
│
├── exponential_growth.py
├── exponential_growth.png
├── logistic_growth.py
├── logistic_growth.png
├── gompertz_growth.py
├── gompertz_growth.png
├── dynamic_carrying_capacity.py
├── dynamic_carrying_capacity.png
├── tumor_treatment.py
├── tumor_treatment.png
├── cancer_invasion_pde.py
├── cancer_invasion.png
└── README.md