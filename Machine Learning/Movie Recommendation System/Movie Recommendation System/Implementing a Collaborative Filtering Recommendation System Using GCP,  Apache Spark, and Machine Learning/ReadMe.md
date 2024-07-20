# Movie Recommendation System using Google Dataproc, Apache Spark, and MLlib (Implementation 1)

This project implements a collaborative filtering movie recommendation system using Apache Spark's MLlib library, Google Dataproc, and machine learning techniques. The goal is to predict user ratings for movies they haven't watched based on their previous ratings and the ratings given by other users with similar preferences.

## Table of Contents

- [Introduction](#introduction)
- [Design](#design)
- [Implementation](#implementation)
- [Test](#test)
- [Enhancement Ideas](#enhancement-ideas)
- [Conclusion](#conclusion)
- [Usage](#usage)
- [Dependencies](#dependencies)

## Introduction

In this project, we aim to develop a movie recommendation system using Apache Spark's MLlib library, specifically implementing collaborative filtering techniques. Collaborative filtering leverages user-item interactions to predict user preferences. The system is built to predict a user's rating for a movie they have not yet watched based on their previous ratings and the ratings given by other users with similar preferences.

### Key Components:
- **Apache Spark**: A powerful open-source processing engine built for speed, ease of use, and sophisticated analytics.
- **Spark MLlib**: The machine learning library of Apache Spark, providing scalable machine learning algorithms including collaborative filtering.

## Design

The project is divided into two primary steps:

### Step 1: Data Conversion
- Preprocess the data from the MovieLens dataset, which contains UserID, MovieID, rating, and Timestamp fields. Only the UserID, MovieID, and rating fields are used.

### Step 2: Implementing Collaborative Filtering using MLlib
- **Loading and Parsing Data**: Load the converted data into an RDD (Resilient Distributed Dataset) and parse to extract UserID, MovieID, and rating.
- **Building the Recommendation Model**: Train a matrix factorization model using the ALS (Alternating Least Squares) algorithm.
- **Model Evaluation**: Evaluate the model's accuracy using Mean Squared Error (MSE).
- **Saving and Loading the Model**: Save the trained model for future use and load it when needed for generating recommendations.

## Implementation

### 1. Set Up a Dataproc Cluster
- Create and configure a Dataproc cluster to handle Spark jobs.

### 2. Accessing the SSH of the Dataproc Cluster
- Use SSH to connect to the Dataproc cluster.

### 3. Upload Source File
- Upload the `u.data` file to the cluster for processing.

### 4. Data Conversion
- Create a `convert_data.py` script to process the input data and convert it to the required format.

### 5. Collaborative Filtering Script
- Create a `recommendation.py` script to implement the collaborative filtering model.

### 6. Uploading File to HDFS
- Ensure the `u.data.csv` file is available in HDFS for further processing by your Spark job.

### 7. Submit Spark Job
- Run your Spark job using the `spark-submit` command.

### 8. Model Evaluation
- Evaluate the performance of the recommendation system using Mean Squared Error (MSE).

## Test

- **Evaluate Performance**: Evaluate the performance of the recommendation system.
- **Test Results**: Mean Squared Error (MSE): 0.4839

## Enhancement Ideas

### Hybrid Recommendation System
- Combine collaborative filtering with content-based filtering.
- Implement a metadata-based approach using movie metadata.

### Model Optimization and Tuning
- Experiment with different hyperparameters for the ALS algorithm.
- Apply cross-validation for robustness and generalizability.

### Scalability and Performance Improvements
- Optimize performance using Spark's capabilities (e.g., data partitioning, caching).
- Explore advanced matrix factorization techniques or deep learning-based models.

## Conclusion

This project demonstrates the implementation of a movie recommendation system using collaborative filtering techniques with Apache Spark's MLlib. By preprocessing the MovieLens dataset and applying the ALS algorithm, we built and evaluated a recommendation model that predicts user ratings for movies.

### Key Achievements
- **Data Preprocessing**: Efficiently converted raw MovieLens data into the required format for collaborative filtering.
- **Model Training**: Trained a matrix factorization model using the ALS algorithm.
- **Model Evaluation**: Evaluated the model using Mean Squared Error (MSE).
- **Recommendations and Predictions**: Implemented functionalities to recommend movies for users and predict ratings for specific user-movie pairs.

## Usage

1. Clone the repository.
2. Ensure you have the required dependencies installed.
3. Run the scripts to preprocess the data, train the model, and generate recommendations.

## Dependencies

- Apache Spark
- Google Dataproc
- Python

Install dependencies using:

```bash
pip install pyspark
