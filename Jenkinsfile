pipeline {
    agent any
    stages{
        stage('Deploy') {
            steps {
                withEnv(['PYTHON_SCRIPT=python_test']) 
     {
       script {
           currentBuild.description = params.DEPLOY_ENV
   if ((params.DEPLOY_ENV == "UAT")) {
               build job: 'sample', parameters: [string(name: 'DEPLOY_ENV', value: 'uat')], propagate: false, wait: false 
   }else {
       return
   }
       }
     }
            
            }
        }
        
        stage('Checkout') {
            steps {
                checkout([$class: 'GitSCM', branches: [[name: '*/master']], extensions: [], userRemoteConfigs: [[credentialsId: 'a6f4081c-63d6-441b-b8de-c99fd34f8502', url: 'https://github.com/coderbpl/python-test.git']]])
            }
        }
        stage("Load Config") {
             steps {
            configText = sh(
                label: "Read config from disk",
                script: "cat ${env.WORKSPACE}/config/${params['DEPLOY_ENV']}.yaml",
                returnStdout: true,
            )
            config = readYaml(text: configText)
             }
        }
        stage('Build') {
            steps {
                sh 'py params.PYTHON_SCRIPT'
            }
        }
    }
}

