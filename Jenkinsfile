pipeline {
    agent { label params['agent-name'] } 

   parameters{
      agentParameter name:'agent-name'
   }
    stages {
        stage('Hello') {
         steps {
            print params['agent-name'] 
         }
      }
        stage('Checkout') {
            steps {
                checkout([$class: 'GitSCM', branches: [[name: '*/master']], extensions: [], userRemoteConfigs: [[credentialsId: 'a6f4081c-63d6-441b-b8de-c99fd34f8502', url: 'https://github.com/coderbpl/python-test.git']]])
            }
        }
        stage('Build') {
            steps {
                sh 'py python_test.py'
            }
        }
    }
}

