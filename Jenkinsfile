pipeline {
  agent any
  stages {
    stage('Build') {
      parallel {
        stage('Build') {
          steps {
            sh 'echo "building PythonBreakMe"'
          }
        }
      }
    }
  
    stage('Test') {
      steps {
        sh 'pytest'
      }
    }
  
    stage('Deploy')
    {
      steps {
        echo "deploying the application"
      }
    }
  }