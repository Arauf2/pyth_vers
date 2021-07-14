pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                sh '''
                echo 'Building..'
                docker stop $(docker ps -a -q)
                docker rm (docker ps -a |grep flask |awk '{print $1}')
                docker build -t flask:latest .
                '''
            }
        }
        stage('Test') {
            steps {
                sh '''
                echo 'Testing..'
                docker images
                '''
            }
        }
        stage('Deploy') {
            steps {
                sh '''
                echo 'Deploying....'
                docker run -p 5000:5000 flask
                '''
            }
        }
    }
}
