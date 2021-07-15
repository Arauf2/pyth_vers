pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                sh '''
                echo 'Building..'
                app="flask"
                if docker ps | awk -v app="$app" 'NR > 1 && $NF == app{ret=1; exit} END{exit !ret}'; then
                docker stop "$app" && docker rm -f "$app"
                fi
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
                # add a check to see if docker container is running, then 
                echo 'Deploying....'
                docker run -p 5000:5000 flask
                '''
            }
        }
    }
}
