# Movie Recommendation Engine using Alternating Least Squares (ALS)

In this project, we aim to develop a movie recommendation system using Apache Spark's MLlib library, specifically implementing collaborative filtering techniques. It implements a movie recommendation engine using the Alternating Least Squares (ALS) algorithm with the MovieLens dataset. The recommendation engine predicts user ratings for unrated movies and provides personalized movie recommendations.

## Table of Contents

- [Introduction](#introduction)
- [Data Loading and Initialization](#data-loading-and-initialization)
- [Data Preparation and Cleaning](#data-preparation-and-cleaning)
- [Exploratory Data Analysis (EDA)](#exploratory-data-analysis-eda)
- [Train-Test Split](#train-test-split)
- [Building the Recommendation Model using ALS](#building-the-recommendation-model-using-als)
- [Model Evaluation](#model-evaluation)
- [Hyperparameter Tuning](#hyperparameter-tuning)
- [Generating Recommendations](#generating-recommendations)
- [Exploding Recommendations](#exploding-recommendations)
- [Joining with Movie Details](#joining-with-movie-details)
- [Displaying Actual Ratings](#displaying-actual-ratings)
- [Conclusion](#conclusion)
- [Usage](#usage)
- [Dependencies](#dependencies)

## Introduction

The goal of this project is to build a recommendation engine that predicts user ratings for movies they haven't seen and recommends movies based on these predictions. The ALS algorithm is used to factorize the user-item interaction matrix into latent factors representing users and movies.

## Data Loading and Initialization

1. **Loading Data**: Read `movies.csv` and `ratings.csv` into Spark DataFrames.
2. **Spark Initialization**: Initiate a Spark session for distributed processing.

    ```python
    movies = spark.read.csv("movies.csv", header=True)
    ratings = spark.read.csv("ratings.csv", header=True)
    ```

## Data Preparation and Cleaning

1. **Data Type Conversion**: Convert user IDs and movie IDs to integers and ratings to float.
2. **Dropping Unnecessary Columns**: Remove the timestamp column from the ratings DataFrame.

    ```python
    ratings = ratings.\
        withColumn('userId', col('userId').cast('integer')).\
        withColumn('movieId', col('movieId').cast('integer')).\
        withColumn('rating', col('rating').cast('float')).\
        drop('timestamp')
    ```

## Exploratory Data Analysis (EDA)

- **Sparsity Calculation**: Calculate the sparsity of the ratings matrix to understand the proportion of missing ratings.
- **Distribution Analysis**: Group and count ratings by users and movies to identify patterns and the distribution of ratings.

## Train-Test Split

- **Splitting Data**: Divide the data into training (80%) and testing (20%) sets to evaluate the model on unseen data.

    ```python
    (train, test) = ratings.randomSplit([0.8, 0.2], seed=1234)
    ```

## Building the Recommendation Model using ALS

1. **ALS Model Initialization**: Set up the ALS algorithm with parameters like iterations, regularization, and column names.
2. **Model Training**: Fit the ALS model on the training dataset.

    ```python
    als = ALS(maxIter=5, regParam=0.01, userCol="userId", itemCol="movieId", ratingCol="rating", coldStartStrategy="drop")
    model = als.fit(train)
    ```

## Model Evaluation

- **Predictions on Test Set**: Use the trained model to predict ratings for the test set.
- **RMSE Calculation**: Evaluate the model's performance using Root Mean Square Error (RMSE) metric.

    ```python
    predictions = model.transform(test)
    evaluator = RegressionEvaluator(metricName="rmse", labelCol="rating", predictionCol="prediction")
    rmse = evaluator.evaluate(predictions)
    print("Root-mean-square error = " + str(rmse))
    ```

## Hyperparameter Tuning

1. **Parameter Grid Definition**: Define a range of hyperparameters for tuning.
2. **Cross-Validation**: Perform cross-validation to find the best model with optimal hyperparameters.

    ```python
    param_grid = ParamGridBuilder().addGrid(als.rank, [10, 50, 100]).addGrid(als.maxIter, [5, 50, 100]).addGrid(als.regParam, [.01, .05, .1]).build()
    cv = CrossValidator(estimator=als, estimatorParamMaps=param_grid, evaluator=evaluator, numFolds=5)
    model = cv.fit(train)
    ```

## Generating Recommendations

1. **Unrated Movies Selection**: Identify movies that each user has not rated.
2. **Predicting Ratings for Unrated Movies**: Use the ALS model to predict ratings for these unrated movies.
3. **Top-N Recommendations**: Select the top 10 movies with the highest predicted ratings for each user.

    ```python
    nrecommendations = best_model.recommendForAllUsers(10)
    ```

## Exploding Recommendations

- **Transforming Nested Recommendations**: Convert the nested structure of recommendations into a flat table format for easier readability and analysis.

    ```python
    nrecommendations = nrecommendations\
        .withColumn("rec_exp", explode("recommendations"))\
        .select('userId', col("rec_exp.movieId"), col("rec_exp.rating"))
    ```

## Joining with Movie Details

- **Merge with Movie Titles**: Join the recommendations with movie titles and genres to provide detailed information about the recommended movies.
- **Filter for Specific Users**: Filter the recommendations for specific users to see personalized suggestions.

    ```python
    nrecommendations.join(movies, on='movieId').filter('userId = 200').show()
    ratings.join(movies, on='movieId').filter('userId = 200').sort('rating', ascending=False).limit(10).show()
    ```

## Displaying Actual Ratings

- **Top-Rated Movies by User**: Show the top-rated movies by specific users to compare with the model's recommendations and validate the model's performance.

    ```python
    ratings.join(movies, on='movieId').filter('userId = 5').sort('rating', ascending=False).limit(20).show()
    ```

## Conclusion

This project demonstrates the process of building a movie recommendation engine using the ALS algorithm. The engine predicts ratings for unrated movies and provides personalized recommendations. The model's performance is evaluated using RMSE, and hyperparameter tuning is performed to optimize the model.

## Usage

1. Clone the repository.
2. Ensure you have the required dependencies installed.
3. Run the script to build and evaluate the recommendation model.

## Dependencies

- PySpark
- Pandas

Install dependencies using:

```bash
pip install pyspark pandas
