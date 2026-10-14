
# Short-Term Rainfall Prediction in Dublin

This repository contains an early research implementation for short-term rainfall prediction in Dublin, Ireland, using meteorological reanalysis data.

The project explores data preprocessing, meteorological feature analysis, and machine learning approaches for rainfall forecasting.

## Project Overview

The experimental workflow includes:

- Meteorological data preprocessing and cleaning
- NetCDF-to-CSV data conversion
- Exploratory data analysis
- Feature correlation analysis
- Principal Component Analysis (PCA)
- Machine learning and deep learning experiments
- Rainfall prediction evaluation

## Repository Structure

```text
.
├── README.md
├── flow.py
└── rainfall_forecasting.ipynb
```

## Code Description

### Data Preprocessing

`flow.py`

A Python script for converting meteorological data from NetCDF format into CSV format.

### Rainfall Forecasting

`rainfall_forecasting.ipynb`

A Jupyter Notebook containing data exploration, preprocessing, feature analysis, model development, and forecasting experiments.

## Tools and Libraries

The project uses Python and scientific computing libraries, including:

- TensorFlow / Keras
- Scikit-learn
- XGBoost
- NumPy
- Pandas
- Matplotlib
- Seaborn
- NetCDF4

## Data

The experiments use meteorological reanalysis data for the Dublin region.

Dataset files are not included in the main repository. The original workflow uses local files and Google Colab paths that may require adjustment.

## Notes

This repository preserves an early experimental workflow and is intended primarily for research reference. It is not maintained as a fully reproducible software package.
