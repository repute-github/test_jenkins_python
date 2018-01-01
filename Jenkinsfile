pipeline {
    agent { any}
    stages {
        stage('build') {
            steps {
                sh 'python3 --version'
                sh 'pylint ./'
                sh 'python3 fibon.py'
            }
        }
    }
}
