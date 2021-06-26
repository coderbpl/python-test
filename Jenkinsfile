pipeline {
    agent any
     environment {
     pythonModule =  "python_test"
   }
    stages{
        stage('Setup parameters') {
            steps {
                script { 
                    properties([
    parameters([
        choice(
            choices: ['uat', 'sandbox', 'e2e', 'prod', 'stage', 'demo', 'all'],
            description: 'Environment that the script should push to.',
            name: 'DEPLOY_ENV'
        ),
    ])
])
                    
                }
            }
        }
    
        stage('Deploy') {
            steps {
                withEnv(["PYTHONPATH=./${pythonModule}"]) 
     {
       script {
           currentBuild.description = params.DEPLOY_ENV
           echo params.DEPLOY_ENV 
            if (params.DEPLOY_ENV == "all") {
            ['sandbox', 'e2e', 'uat', 'stage', 'demo', 'prod'].each { String app ->
                build(
                    job: 'sample', parameters: [string(name: 'DEPLOY_ENV', value: 'uat')],
                    propagate: false,
                    wait: false
                )
            }
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
                 script{
            configText = sh(
                label: "Read config from disk",
                script: "cat ${env.WORKSPACE}/config/${params['DEPLOY_ENV']}.yaml",
                returnStdout: true,
            )
            config = readFile "${env.WORKSPACE}/config/${params['DEPLOY_ENV']}.yaml"
                    
             }
             }
        }
        stage('Build') {
            steps {
                sh py "${params['DEPLOY_ENV']}"
            }
        }
    }
}

