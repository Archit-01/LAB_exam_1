pipeline {
    agent any

    environment {
        PY_IMAGE = 'python:3.11-slim'
        NODE_IMAGE = 'node:18-alpine'
        DOCKER = '/usr/local/bin/docker'
        PATH = "/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin"
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
                      -e DOCKER_CONFIG=/tmp \
                      -v "$PWD":/workspace \
                      -w /workspace/smartcalx-service/python_service \
                      ${PY_IMAGE} \
                      /bin/sh -c "pip install -r requirements.txt && pytest -q tests/"
                '''
            }
            post {
                success { echo "✅ Python tests passed successfully!" }
                failure { echo "❌ Python tests failed!" }
            }
        }

        stage('Run Node.js tests') {
            steps {
                echo "🧪 Running Node.js tests inside container..."
                sh '''
                    ${DOCKER} run --rm \
                      -e DOCKER_CONFIG=/tmp \
                      -v "$PWD":/workspace \
                      -w /workspace/smartcalx-service/python_service/node_service \
                      ${NODE_IMAGE} \
                      /bin/sh -c "npm install && npm test"
                '''
            }
            post {
                success { echo "✅ Node.js tests passed successfully!" }
                failure { echo "❌ Node.js tests failed!" }
            }
        }

        stage('Build & Run via Docker Compose') {
            steps {
                echo "🐳 Building and running full stack using docker-compose..."
                sh '''
                    ${DOCKER} compose down || true
                    ${DOCKER} compose up -d --build
                '''
            }
        }

        stage('Verify Containers Running') {
            steps {
                echo "🔍 Verifying services are up..."
                sh '''
                    ${DOCKER} ps
                '''
            }
        }
    }

    post {
        always {
            echo "🧹 Cleaning up containers..."
            sh '''
                ${DOCKER} compose down || true
            '''
        }
        success {
            echo "🎉 All tests passed and containers built successfully!"
        }
        failure {
            sh "${DOCKER} --version"
            echo "⚠️ Build failed — check the logs above for details."
        }
    }
}
