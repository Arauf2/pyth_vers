pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                sh '''
                echo 'Building..'
                docker ps
                docker rm $(docker stop $(docker ps -a -q --filter ancestor=flask --format="{{.ID}}"))
                docker build -t flask:latest .
                '''
            }
        }
        stage('Test') {
            steps {
                sh '''
                echo 'Testing..'
                docker ps
                '''
            }
        }
        stage('Deploy') {
            steps {
                sh '''
                echo 'Deploying....'
                docker run -d -p 5000:5000 flask
                '''
            }
        }
    }
}