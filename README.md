# Body Fat Percent Prediction 
- In this project, we estimate body fat percent from measurements such as density, weight, height, etc.
- Source of dataset : 
  - Dataset with density : https://www.kaggle.com/datasets/fedesoriano/body-fat-prediction-dataset
  - Extended Dataset without density : https://www.kaggle.com/datasets/simonezappatini/body-fat-extended-dataset
- We add an additional feature BMI which may be useful in our prediction
- We observe that there is skewness in data because of outliers. We detect the outliers using InterQuartile Range and then remove them.
- After removing outliers, we don't observe any skewness.
- We observe that there is a high correlation between density and body fat percent.
- Density scan is really expensive, so we try to predict body fat percent with and without using density
- We use different models to train and choose the model which gives the best R2 score values.
- We do hyperparameter tuning using Randomised and Grid Search CV
- Models used :
  - Linear Regression
  - Lasso Regression
  - Ridge Regression
  - ElasticNet Regression
  - Random Forest Regression
  - Support Vector Regression
  - K Nearest Neighbors Regression
  - XG Boost Regression.
- We observe an R2 score of 0.6437 on test data when we don't use density as feature. Best Model - Linear Regression
- We observe an R2 score of 0.9987 on test data when we use density as feature. Best Model - Support Vector Regression
