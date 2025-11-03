pipeline {
    agent any

    environment {
        // Define Docker image names
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
                      /bin/sh -c "pip install -r requirements.txt && pytest -q"
                '''
            }
            post {
                success { echo "✅ Python tests passed successfully!" }
                failure { echo "❌ Python tests failed!" }
            }
        }

        stage('Run Node tests') {
            steps {
                echo "🧪 Running Node.js tests inside container..."
                sh '''
                    ${DOCKER} run --rm \
                      -e DOCKER_CONFIG=/tmp \
                      -v "$PWD":/workspace \
                      -w /workspace/smartcalx-service/node_service \
                      ${NODE_IMAGE} \
                      /bin/sh -c "npm install && npm test"
                '''
            }
            post {
                success { echo "✅ Node.js tests passed successfully!" }
                failure { echo "❌ Node.js tests failed!" }
            }
        }

        stage('Build & Run App Container') {
            steps {
                echo "🐳 Building and running app container..."
                sh '''
                    ${DOCKER} build -t smartcalc-app .
                    ${DOCKER} run -d --name smartcalc-container -p 5000:5000 smartcalc-app
                '''
            }
        }

        stage('Verify Container Running') {
            steps {
                echo "🔍 Checking if container is running..."
                sh '''
                    ${DOCKER} ps | grep smartcalc-container
                '''
            }
        }
    }

    post {
        always {
            echo "🧹 Cleaning up containers..."
            sh '''
                ${DOCKER} rm -f smartcalc-container || true
            '''
        }
        success {
            echo "🎉 Build and test pipeline completed successfully!"
        }
        failure {
            sh "${DOCKER} --version"
            echo "⚠️ Build failed — check above logs for details."
        }
    }
}
