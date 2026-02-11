# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This repository contains assignment implementations for CSE 3000: Contemporary Issues in Computer Science and Engineering. The focus is on ethical and contemporary issues in machine learning including bot detection, algorithmic bias, and data privacy.

## Repository Structure

The codebase follows a modular pattern where each assignment (module) consists of:
- **Python module** (`.py` file): Core function implementations
- **Jupyter notebook** (`.ipynb` file): Testing, validation, and analysis with discussion questions
- **Data directory**: CSV datasets used by the module

### Current Modules

- **mod02**: Bot prediction using Gradient Boosting Classifier
- **mod04**: Bias analysis using Random Forest and SHAP values
- **mod06**: Deanonymization attack demonstration using quasi-identifiers

## Common Commands

### Running Jupyter Notebooks
```bash
jupyter notebook  # Opens browser interface
jupyter lab       # Alternative interface
```

### Running Individual Notebooks
```bash
jupyter notebook mod02_test_bot_predictor.ipynb
jupyter notebook mod04_bias.ipynb
jupyter notebook mod06_check_deanonymization.ipynb
```

### Executing Notebooks from Command Line
```bash
jupyter nbconvert --to notebook --execute mod02_test_bot_predictor.ipynb
```

### Using Python Modules Directly
```python
# Import and use module functions
from mod02_build_bot_predictor import train_model
from mod06_deanonymize import load_data, link_records, deanonymization_rate
```

## Architecture

### Module Pattern
Each assignment follows this architecture:
1. **Implementation file** (e.g., `mod02_build_bot_predictor.py`): Contains reusable functions that are imported into notebooks
2. **Testing notebook** (e.g., `mod02_test_bot_predictor.ipynb`): Imports functions, loads data, runs analysis, includes discussion questions
3. **Data directory** (e.g., `mod02_data/`): Contains CSV files with training/test data

### Dependencies
The project uses:
- **pandas**: Data manipulation and CSV handling
- **scikit-learn**: Machine learning models (GradientBoostingClassifier, RandomForestRegressor)
- **shap**: Model interpretability and bias analysis
- **matplotlib**: Visualization
- **numpy**: Numerical operations

### Module-Specific Details

#### mod02: Bot Predictor
- Uses `GradientBoostingClassifier` with fixed hyperparameters
- Seed set to 314 for reproducibility
- Implements confusion matrix calculation and error metrics (FPR, FNR, misclassification rate)
- Data split into `train.csv` and `test.csv`

#### mod04: Bias Analysis
- Uses `RandomForestRegressor` with 200 estimators
- Seed set to 2724 for reproducibility
- Analyzes proxy features (zipcode_score) that correlate with protected group membership
- Uses SHAP values to explain model predictions and identify indirect bias
- Demonstrates how models can be biased without directly using protected attributes

#### mod06: Deanonymization
- Implements privacy attack using exact matching on quasi-identifiers (age, gender, zip3)
- Two datasets: `anonymized.csv` (without names) and `auxiliary.csv` (with names)
- Functions `link_records()` and `deanonymization_rate()` are stubs to be implemented
- Demonstrates k-anonymity vulnerabilities

## Development Notes

- All Python modules use a global `seed` variable for reproducibility
- Notebooks contain markdown cells with discussion questions that need text responses
- The `.gitignore` excludes `setup_env.py` and `3000-env/` directory (likely virtual environment)
- No formal testing framework - validation is done through notebooks
- No linting or type checking configured
