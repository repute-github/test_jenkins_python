pipeline {
  agent any
  stages {
    stage('build') {
      agent any
      steps {
        sh 'python --version'
        sh 'pylint fibon.py'
        sh 'python fibon.py'
      }
    }
  }
}
