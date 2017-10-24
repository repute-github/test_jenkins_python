pipeline {
    agent { docker 'python:3.5.1' }
    stages {
        stage('build') {
            steps {
                sh 'python --version'
                sh 'pylint ./'
                sh 'python fibon.py'
            }
        }
    }
}
