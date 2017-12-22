pipeline {
  agent any
  stages {
    stage('build') {
      agent any
      steps {
        sh 'python3 --version'
        sh 'pylint fibon.py'
        sh 'python3 fibon.py'
      }
    }
  }
}
