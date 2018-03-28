pipeline {
  agent {
    docker {
      image 'markduell/jenks:1.0'
    }
    
  }
  stages {
    stage('initialise') {
      steps {
        sh 'behave'
      }
    }
  }
}