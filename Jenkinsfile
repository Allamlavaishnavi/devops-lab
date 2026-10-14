pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                    python3 -m venv .venv
                    . .venv/bin/activate
                    pip install -r requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
                    . .venv/bin/activate
                    pytest -v
                '''
            }
        }

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t devops-flask-app:${BUILD_NUMBER} .'
            }
        }

        stage('Deploy Flask Application') {
            steps {
                sh '''
                    docker rm -f devops-flask-container-ci || true
                    docker run -d --name devops-flask-container-ci \
                        -p 5001:5000 \
                        devops-flask-app:${BUILD_NUMBER}
                '''
            }
        }
    }
}