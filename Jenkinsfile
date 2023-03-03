pipeline {
    agent {
      any { image 'python:3' }
    }
    environment {
        FLASK_APP = "app.py"
        FLASK_ENV = "development"
    }
    stages {
        stage('Checkout') {
            steps {
                checkout([$class: 'GitSCM', branches: [[name: 'main']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/jimsladek/Imad-aws.git']]])
            }
        }
        stage('Build backend') {
            steps {
                sh 'cd backend-Python'
                sh 'sudo docker build -t backend .'
            }
        }
        stage('Build frontend') {
            steps {
                sh 'cd ../angular'
                sh 'sudo docker build -t frontend .'
            }
        }
        stage('Run Container') {
            steps {
                sh 'sudo docker-compose up -d --force-recreate'
            }
        }
        stage('Merge to Dev') {
            steps {
                sh 'git checkout Dev && git merge origin/master'
            }
        }
        stage('Deploy to Dev') {
            steps {
                sh 'echo "http://localhost:5000"'
            }
        }
    }
}
