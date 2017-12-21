pipeline {
  agent any
  stages {
    stage('build') {
      agent any
      steps {
        sh 'python --version'
        sh 'pylint ./'
        sh 'python fibon.py'
      }
    }
  }
}