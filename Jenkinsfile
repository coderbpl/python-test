def pythonModule = "python_test"

node('deploy') {
    withEnv([
        "PYTHONPATH=./${pythonModule}"
    ]) {
        currentBuild.description = params.DEPLOY_ENV
        if (params.DEPLOY_ENV == "all") {
            ['sandbox', 'e2e', 'uat', 'stage', 'demo', 'prod'].each { String app ->
                build(
                    job: 'grafana/master',
                    parameters: [
                        [$class: 'StringParameterValue', name: 'DEPLOY_ENV', value: app],
                    ],
                    propagate: false,
                    wait: false
                )
            }
            return
        }

        def scmProp
        stage("Pull Repo") {
            scmProp = checkout scm
        }

        def LinkedHashMap config
        stage("Load Config") {
            configText = sh(
                label: "Read config from disk",
                script: "cat ${env.WORKSPACE}/config/${params['DEPLOY_ENV']}.yaml",
                returnStdout: true,
            )
            config = readYaml(text: configText)
        }

        stage("Lint Module") {
            sh "pylint ${pythonModule}"
        }

        stage("Lint Dashboards") {
            // We are more permissive on the dashboards since there is likely some overlap of imports and code repetition
            sh "pylint dashboards --disable=wildcard-import,unused-wildcard-import,unused-import,duplicate-code"
        }

        stage("Validate dashboards") {
            withCredentials([string(credentialsId: "grafana-sre-${config.environment.subscription.toLowerCase()}", variable: 'GRAFANA_AUTH')]) {
                sh "python3 -m ${pythonModule} -c config/${params['DEPLOY_ENV']}.yaml -l INFO -d dashboards test"
            }
        }

        if (env.BRANCH_NAME == "master" || params.DEPLOY_ENV == 'sandbox') {
            stage("Upload dashboards") {
                withCredentials([string(credentialsId: "grafana-sre-${config.environment.subscription.toLowerCase()}", variable: 'GRAFANA_AUTH')]) {
                    sh "python3 -m ${pythonModule} -c config/${params['DEPLOY_ENV']}.yaml -l INFO -d dashboards upload"
                }
            }
        }
    }
}
