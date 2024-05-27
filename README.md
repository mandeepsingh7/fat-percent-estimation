# Body Fat Percent Estimation

This project aims to estimate body fat percent from various physical measurements such as density, weight, height, etc.

## Dataset

- **Source**:
  - Dataset with density: [Kaggle - Body Fat Prediction Dataset](https://www.kaggle.com/datasets/fedesoriano/body-fat-prediction-dataset)
  - Extended Dataset without density: [Kaggle - Body Fat Extended Dataset](https://www.kaggle.com/datasets/simonezappatini/body-fat-extended-dataset)

## Project Overview

1. **Feature Addition**:
   - Added Body Mass Index (BMI) as an additional feature, which may be useful in prediction.

2. **Outlier Detection and Removal**:
   - Detected outliers using the InterQuartile Range (IQR) method.
   - Removed outliers to reduce skewness in the data.

3. **Correlation Analysis**:
   - Observed a high correlation between density and body fat percent.
   - Noted that density scans are expensive, so we experimented with models both including and excluding the density feature.

4. **Model Training and Evaluation**:
   - Trained multiple models and selected the best ones based on R² score.
   - Conducted hyperparameter tuning using Randomized and Grid Search Cross-Validation (CV).

## Models Used

1. **Linear Regression**
2. **Lasso Regression**
3. **Ridge Regression**
4. **ElasticNet Regression**
5. **Random Forest Regression**
6. **Support Vector Regression (SVR)**
7. **K Nearest Neighbors Regression (KNN)**
8. **XGBoost Regression**

## Results

- **Without Density**:
  - **Best Model**: Linear Regression
  - **R² Score on Test Data**: 0.6437

- **With Density**:
  - **Best Model**: Support Vector Regression (SVR)
  - **R² Score on Test Data**: 0.9987

## Conclusion

This project demonstrates the process of predicting body fat percentage using various regression models. The inclusion of the density feature significantly improves the model's performance, as evidenced by the higher R² score. However, excluding the density feature still yields a reasonable prediction accuracy, making the model more practical for scenarios where density measurement is not feasible.


