pipeline {
  agent any
  environment {
    // if you want to run inside docker images, we will pull official images
    PY_IMAGE = 'python:3.11-slim'
    NODE_IMAGE = 'node:18-alpine'
  }
  stages {
    stage('Checkout') {
      steps {
        checkout scm
        echo "Checked out ${env.GIT_COMMIT}"
      }
    }

    stage('Run Python tests') {
      steps {
        script {
          // Run tests inside a python docker container (requires docker on Jenkins node and socket mounted)
          sh '''
            echo "Running Python tests..."
            docker run --rm -v "$PWD":/workspace -w /workspace/smartcalx-service/python_service ${PY_IMAGE} /bin/sh -c "pip install -r requirements.txt && pytest -q"
          '''
        }
      }
      post {
        success {
          echo "Python tests passed"
        }
        failure {
          echo "Python tests failed"
        }
      }
    }

    stage('Run Node tests') {
      steps {
        script {
          sh '''
            echo "Running Node tests..."
            docker run --rm -v "$PWD":/workspace -w /workspace/smartcalx-service/node_service ${NODE_IMAGE} /bin/sh -c "npm ci && npm test --silent"
          '''
        }
      }
      post {
        success {
          echo "Node tests passed"
        }
        failure {
          echo "Node tests failed"
        }
      }
    }
  }
  post {
    always {
      // Print a marker so it's easy to spot results
      echo "PIPELINE DONE - See above for test pass/fail"
    }
  }
}
