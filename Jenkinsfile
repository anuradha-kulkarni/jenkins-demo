pipeline {
  agent any
  stages {
    stage('Git') {
      steps {
        git(url: 'https://github.com/code-with-madhu/jenkins-demo.git', branch: 'main', poll: true)
      }
    }

    stage('Build') {
      steps {
        echo 'From Build Step'
      }
    }

  }
}