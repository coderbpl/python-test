pipeline {
    agent any
    stages{
        stage('Deploy') {
            steps {
                withEnv(['PYTHON_SCRIPT=python_test']) 
     {
        currentBuild.description = params.DEPLOY_ENV
        if (params.DEPLOY_ENV == "UAT") {
   
               build job: 'grafana/master', parameters: [string(name: 'DEPLOY_ENV', value: 'uat')], propagate: false, wait: false 
            
            return
        }
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
                sh 'py python_test.py'
            }
        }
    }
}

