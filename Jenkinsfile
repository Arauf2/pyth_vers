pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                sh '''
                echo 'Building..'
                docker build -t rubyapp .
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
                echo 'Deploying....'
            }
        }
    }
}
