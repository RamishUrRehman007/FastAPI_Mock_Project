# FastAPI Mock Project

This project is a FastAPI application that demonstrates a mock setup, containerized with Docker for easy setup and deployment.

## Prerequisites

Before you begin, ensure you have installed:

- [Docker](https://www.docker.com/products/docker-desktop)
- [Git](https://git-scm.com/downloads)

## Setup and Installation

### Step 1: Clone the Repository

To clone the repository securely, you need to use your GitHub username and a personal access token. Follow these steps:

1. **Set Your GitHub Credentials**: 
   Replace `YOUR_USERNAME` and `YOUR_ACCESS_TOKEN` with your GitHub username and personal access token.

    ```bash
    export GITHUB_USERNAME=YOUR_USERNAME
    export GITHUB_TOKEN=YOUR_ACCESS_TOKEN
    ```

    _Note: You can generate a personal access token by following the instructions on [GitHub's documentation](https://docs.github.com/en/github/authenticating-to-github/creating-a-personal-access-token)._

2. **Clone the Repository**:
   
    ```bash
    git clone https://$GITHUB_USERNAME:$GITHUB_TOKEN@github.com/RamishUrRehman007/FastAPI_Mock_Project.git
    ```

### Step 2: Running the Application

Navigate to the project directory and use Docker Compose to start the application:

```bash
cd FastAPI_Mock_Project
docker-compose up
```

## Accessing the Application

Open your web browser and navigate to http://localhost:10000. This is the default address where FastAPI applications run, unless configured otherwise. This default url redirects to the `http://localhost:10000/docs` - automatic documentation generated by FastAPI.


## Stopping the Application
To stop the application, use `Ctrl+C` in the terminal where Docker Compose is running, or run `docker-compose down` in a separate terminal.
