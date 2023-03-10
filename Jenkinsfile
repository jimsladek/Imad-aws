pipeline {
    agent any

    stages {
        stage('Build BDD Image') {
            steps {
                dir('BDD') {
                    script {
                        docker.build("bdd", "-f Dockerfile .")
                    }
                }
            }
        }
        stage('Build Backend Image') {
            steps {
                dir('Backend') {
                    script {
                        docker.build("backend", "-f Dockerfile .")
                    }
                }
            }
        }
        stage('Build Frontend Image') {
            steps {
                dir('Frontend') {
                    script {
                        docker.build("frontend", "-f Dockerfile .")
                    }
                }
            }
        }
        stage('Git Checkout') {
            steps {
                git branch: 'master', url: 'https://github.com/jimsladek/Imad-aws.git'
            }
        }
        stage('Start Containers') {
            steps {
                sh 'docker-compose up -d'
            }
        }
    }
}
