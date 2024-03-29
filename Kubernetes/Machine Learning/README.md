# Deploying Machine Learning Models using Docker

This guide outlines the steps to containerize and deploy a simple machine learning (ML) application using Flask and Docker. The goal is to demonstrate the deployment process rather than focus on model accuracy or complexity.

### Step 1: Train the ML Model

- **Objective**: Deploy the ML application; hence, we prioritize containerizing the app over enhancing model accuracy.
- **Model Choice**: Opt for a straightforward approach using a logistic regression or random forest model without delving deeply into feature engineering or complex model architecture.

### Step 2: Save and Export the ML Model

- **Saving the Model**: Post-training, use pickle/joblib to save the model, facilitating its reuse during predictions.

### Step 3: Create a Flask App Including the UI Layer

- **Flask Application**: Develop a Flask application.
- **UI Layer**: Integrate Flasgger to simplify deploying the ML model.

### Step 4: Build a Custom Docker Image for the App

1. **Base Image**: Specify the base image from Docker Hub.
2. **File Transfer**: Copy all local directory files to the Docker directory.
3. **Port Exposing**: Expose port 5000 for application access.
4. **Working Directory**: Set Docker's working directory to where files are copied.
5. **Dependencies**: Install all necessary dependencies and libraries.
6. **Startup Command**: Define the Dockerfile's final command to launch the application.

### Step 5: Run the App Using a Docker Container

1. **Build Image**: Construct the Docker custom image from the Dockerfile.
2. **Run Container**: Execute the container to launch the ML app.
3. **Access Application**: Navigate to `http://127.0.0.1:5000/apidocs` to access the Swagger UI.

### Step 6: Stop the Container

- **Container Shutdown**: Utilize the `docker stop` or `docker kill` commands to halt the running container.
