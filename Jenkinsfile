pipeline {
    agent any
    stages{
        stage('Deploy') {
            steps {
                withEnv(['PYTHON_SCRIPT=python_test']) 
     {
       
   
               build job: 'sample', parameters: [string(name: 'DEPLOY_ENV', value: params.DEPLOY_ENV)], propagate: false, wait: false 
     }
            
            }
        }
        
        stage('Checkout') {
            steps {
                checkout([$class: 'GitSCM', branches: [[name: '*/master']], extensions: [], userRemoteConfigs: [[credentialsId: 'a6f4081c-63d6-441b-b8de-c99fd34f8502', url: 'https://github.com/coderbpl/python-test.git']]])
            }
        }
        stage('Build') {
            steps {
                sh 'py params.PYTHON_SCRIPT'
            }
        }
    }
}

