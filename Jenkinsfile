pipeline {
  agent any

  environment {
    DOCKER         = "/usr/local/bin/docker"      // Full Docker path on macOS
    PY_IMAGE       = "python:3.11-slim"
    NODE_IMAGE     = "node:18-alpine"
    IMAGE_NAME     = "smartcalc-service"
    CONTAINER_NAME = "smartcalc-service-container"
  }

  stages {

    stage('Checkout') {
      steps {
        echo "📦 Checking out repository..."
        checkout scm
      }
    }

    stage('Run Python tests') {
      steps {
        echo "🐍 Running Python tests inside container..."
        sh '''
          ${DOCKER} run --rm \
            -v "$PWD":/workspace \
            -w /workspace/smartcalx-service/python_service \
            ${PY_IMAGE} \
            /bin/sh -c "pip install -r requirements.txt && pytest -q"
        '''
      }
      post {
        success {
          echo "✅ Python tests passed successfully!"
        }
        failure {
          echo "❌ Python tests failed!"
        }
      }
    }

    stage('Run Node tests') {
      steps {
        echo "🧩 Running Node.js tests inside container..."
        sh '''
          ${DOCKER} run --rm \
            -v "$PWD":/workspace \
            -w /workspace/smartcalx-service/node_service \
            ${NODE_IMAGE} \
            /bin/sh -c "npm ci && npm test --silent"
        '''
      }
      post {
        success {
          echo "✅ Node.js tests passed successfully!"
        }
        failure {
          echo "❌ Node.js tests failed!"
        }
      }
    }

    stage('Build & Run App Container') {
      steps {
        echo "🏗️ Building app Docker image..."
        sh '''
          ${DOCKER} build -t ${IMAGE_NAME} .
          ${DOCKER} rm -f ${CONTAINER_NAME} || true
          ${DOCKER} run -d -p 5050:5000 --name ${CONTAINER_NAME} ${IMAGE_NAME}
        '''
      }
    }

    stage('Verify Container Running') {
      steps {
        sh '${DOCKER} ps'
        sh 'curl -s http://localhost:5050 || echo "App not responding yet"'
      }
    }
  }

  post {
    success {
      echo "🎉 All stages completed successfully! Your app and tests ran fine."
    }
    failure {
      echo "⚠️ Build failed — check above logs for details."
    }
    always {
      sh '${DOCKER} --version || true'
    }
  }
}
