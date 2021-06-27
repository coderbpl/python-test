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
                sh "python3 -m ${pythonModule} -c config/${params['DEPLOY_ENV']}.yaml -l INFO -d dashboards test"
            }
        }
        stage('Push to grafana'){
            steps{
                withCredentials([string(credentialsId: 'grafan_auth', variable: 'grafana_auth')]) {
    sh """curl -X POST -d '{ "annotations": { "list": [ { "builtIn": 1, "datasource": "-- Grafana --", "enable": true, "hide": true, "iconColor": "rgba(0, 211, 255, 1)", "name": "Annotations & Alerts", "type": "dashboard" } ] }, "description": "", "editable": true, "gnetId": null, "graphTooltip": 0, "id": 1217, "links": [], "panels": [ { "datasource": "fcs-mpp_prometheus-preprod", "fieldConfig": { "defaults": { "color": { "mode": "palette-classic" }, "custom": { "axisLabel": "", "axisPlacement": "auto", "barAlignment": 0, "drawStyle": "line", "fillOpacity": 0, "gradientMode": "none", "hideFrom": { "legend": false, "tooltip": false, "viz": false }, "lineInterpolation": "linear", "lineWidth": 1, "pointSize": 5, "scaleDistribution": { "type": "linear" }, "showPoints": "auto", "spanNulls": false, "stacking": { "group": "A", "mode": "none" }, "thresholdsStyle": { "mode": "off" } }, "mappings": [], "thresholds": { "mode": "absolute", "steps": [ { "color": "green", "value": null }, { "color": "red", "value": 80 } ] }, "unit": "percentunit" }, "overrides": [] }, "gridPos": { "h": 8, "w": 12, "x": 0, "y": 0 }, "id": 2, "options": { "legend": { "calcs": [], "displayMode": "list", "placement": "bottom" }, "tooltip": { "mode": "single" } }, "targets": [ { "exemplar": true, "expr": "sum(jvm_memory_used_bytes{area=\"heap\", service=\"fcs-cerberus-uat\",cf_cluster=\"cerberus-uat-green\",cf_space=\"Adv-Eng_uat\",cf_instance_index=\"0\"}) by (service, cf_cluster, cf_space, cf_instance_index)/sum(jvm_memory_max_bytes{service=\"fcs-cerberus-uat\",cf_cluster=\"cerberus-uat-green\",cf_space=\"Adv-Eng_uat\",cf_instance_index=\"0\"})by (service, cf_cluster, cf_space, cf_instance_index)", "hide": false, "interval": "", "legendFormat": "Heap: Service: {{service}}, Application: {{cf_cluster}},  PCF Space: {{cf_space}}, Instance: {{cf_instance_index}}", "refId": "A" }, { "exemplar": true, "expr": "sum(jvm_memory_used_bytes{area=\"nonheap\", service=\"fcs-cerberus-uat\",cf_cluster=\"cerberus-uat-green\",cf_space=\"Adv-Eng_uat\",cf_instance_index=\"0\"}) by (service, cf_cluster, cf_space, cf_instance_index)/sum(jvm_memory_max_bytes{service=\"fcs-cerberus-uat\",cf_cluster=\"cerberus-uat-green\",cf_space=\"Adv-Eng_uat\",cf_instance_index=\"0\"})by (service, cf_cluster, cf_space, cf_instance_index)", "hide": false, "interval": "", "legendFormat": "Non-Heap: Service: {{service}}, Application: {{cf_cluster}}, PCF Space: {{cf_space}}, Instance: {{cf_instance_index}}", "refId": "B" }, { "exemplar": true, "expr": "sum(jvm_memory_used_bytes{service=\"fcs-cerberus-uat\",cf_cluster=\"cerberus-uat-green\",cf_space=\"Adv-Eng_uat\",cf_instance_index=\"0\"}) by (service, cf_cluster, cf_space, cf_instance_index)/sum(jvm_memory_max_bytes{service=\"fcs-cerberus-uat\",cf_cluster=\"cerberus-uat-green\",cf_space=\"Adv-Eng_uat\",cf_instance_index=\"0\"})by (service, cf_cluster, cf_space, cf_instance_index)", "hide": false, "interval": "", "legendFormat": "Total: Service: {{service}}, Application: {{cf_cluster}},  PCF Space: {{cf_space}}, Instance: {{cf_instance_index}}", "refId": "C" } ], "title": "Percent Memory Used", "type": "timeseries" }, { "datasource": "fcs-mpp_prometheus-preprod", "fieldConfig": { "defaults": { "color": { "mode": "palette-classic" }, "custom": { "axisLabel": "", "axisPlacement": "auto", "barAlignment": 0, "drawStyle": "line", "fillOpacity": 0, "gradientMode": "none", "hideFrom": { "legend": false, "tooltip": false, "viz": false }, "lineInterpolation": "linear", "lineWidth": 1, "pointSize": 5, "scaleDistribution": { "type": "linear" }, "showPoints": "auto", "spanNulls": false, "stacking": { "group": "A", "mode": "none" }, "thresholdsStyle": { "mode": "off" } }, "mappings": [], "thresholds": { "mode": "absolute", "steps": [ { "color": "green", "value": null }, { "color": "red", "value": 80 } ] }, "unit": "reqps" }, "overrides": [] }, "gridPos": { "h": 8, "w": 12, "x": 12, "y": 0 }, "id": 6, "options": { "legend": { "calcs": [], "displayMode": "list", "placement": "bottom" }, "tooltip": { "mode": "single" } }, "targets": [ { "exemplar": true, "expr": "idelta(sum(http_server_requests_seconds_count{service=\"fcs-cerberus-uat\",cf_cluster=\"cerberus-uat-green\",cf_space=\"Adv-Eng_uat\",cf_instance_index=\"0\"}) by(service, cf_cluster, cf_space, cf_instance_index, uri, status)[1m:30s]) > 0", "interval": "", "legendFormat": "Endpoint: {{uri}} Status: {{status}} Service: {{service}}, Application: {{cf_cluster}},  PCF Space: {{cf_space}}, Instance: {{cf_instance_index}}", "refId": "A" }, { "exemplar": true, "expr": "rate(sum(http_server_requests_seconds_count{service=\"fcs-cerberus-uat\",cf_cluster=\"cerberus-uat-green\",cf_space=\"Adv-Eng_uat\",cf_instance_index=\"0\",status=\"200\",uri=\"/master-reset/api/deauthorize/v1/cerberus\"}) by(service, cf_cluster) [1m:30s]) > 0\n", "hide": false, "interval": "", "legendFormat": "Application Total | Service: {{service}}, Application: {{cf_cluster}}", "refId": "B" }, { "exemplar": true, "expr": "rate(sum(http_server_requests_seconds_count{service=\"fcs-cerberus-uat\",cf_cluster=\"cerberus-uat-green\",cf_space=\"Adv-Eng_uat\",cf_instance_index=\"0\",status=\"200\",uri=\"/master-reset/api/deauthorize/v1/cerberus\"}) by(service, cf_cluster, cf_space) [1m:30s]) > 0", "hide": false, "interval": "", "legendFormat": "Space Total | Service: {{service}}, Application: {{cf_cluster}},  PCF Space: {{cf_space}}", "refId": "C" }, { "exemplar": true, "expr": "rate(sum(http_server_requests_seconds_count{service=\"fcs-cerberus-uat\",cf_cluster=\"cerberus-uat-green\",cf_space=\"Adv-Eng_uat\",cf_instance_index=\"0\",status=\"200\",uri=\"/master-reset/api/deauthorize/v1/cerberus\"})by(service, cf_cluster, cf_space, cf_instance_index, uri, status)[1m:30s]) > 0", "hide": false, "interval": "", "legendFormat": "Endpoint: {{uri}} Status: {{status}} Service: {{service}}, Application: {{cf_cluster}},  PCF Space: {{cf_space}}, Instance: {{cf_instance_index}}", "refId": "D" } ], "title": "Endpoint Request Rates", "type": "timeseries" }, { "datasource": "fcs-mpp_prometheus-preprod", "fieldConfig": { "defaults": { "color": { "mode": "palette-classic" }, "custom": { "axisLabel": "", "axisPlacement": "auto", "barAlignment": 0, "drawStyle": "line", "fillOpacity": 0, "gradientMode": "none", "hideFrom": { "legend": false, "tooltip": false, "viz": false }, "lineInterpolation": "linear", "lineWidth": 1, "pointSize": 5, "scaleDistribution": { "type": "linear" }, "showPoints": "auto", "spanNulls": false, "stacking": { "group": "A", "mode": "none" }, "thresholdsStyle": { "mode": "off" } }, "mappings": [], "thresholds": { "mode": "absolute", "steps": [ { "color": "green", "value": null }, { "color": "red", "value": 80 } ] }, "unit": "percentunit" }, "overrides": [] }, "gridPos": { "h": 8, "w": 12, "x": 0, "y": 8 }, "id": 4, "options": { "legend": { "calcs": [], "displayMode": "list", "placement": "bottom" }, "tooltip": { "mode": "single" } }, "targets": [ { "exemplar": true, "expr": "max(process_cpu_usage{service=\"fcs-cerberus-uat\",cf_cluster=\"cerberus-uat-green\",cf_space=\"Adv-Eng_uat\",cf_instance_index=\"0\"}/system_cpu_count{service=\"fcs-cerberus-uat\",cf_cluster=\"cerberus-uat-green\",cf_space=\"Adv-Eng_uat\",cf_instance_index=\"0\"})by (service, cf_cluster, cf_space, cf_instance_index)", "interval": "", "legendFormat": "Service: {{service}}, Application: {{cf_cluster}},  PCF Space: {{cf_space}}, Instance: {{cf_instance_index}}", "refId": "A" } ], "title": "Percent CPU Utilization", "type": "timeseries" }, { "datasource": "fcs-mpp_prometheus-preprod", "fieldConfig": { "defaults": { "color": { "mode": "palette-classic" }, "custom": { "axisLabel": "", "axisPlacement": "auto", "barAlignment": 0, "drawStyle": "line", "fillOpacity": 0, "gradientMode": "none", "hideFrom": { "legend": false, "tooltip": false, "viz": false }, "lineInterpolation": "linear", "lineWidth": 1, "pointSize": 5, "scaleDistribution": { "type": "linear" }, "showPoints": "auto", "spanNulls": false, "stacking": { "group": "A", "mode": "none" }, "thresholdsStyle": { "mode": "off" } }, "mappings": [], "thresholds": { "mode": "absolute", "steps": [ { "color": "green", "value": null }, { "color": "red", "value": 80 } ] }, "unit": "ms" }, "overrides": [] }, "gridPos": { "h": 8, "w": 12, "x": 12, "y": 8 }, "id": 8, "options": { "legend": { "calcs": [], "displayMode": "list", "placement": "bottom" }, "tooltip": { "mode": "single" } }, "targets": [ { "exemplar": true, "expr": "1000 * idelta(sum(http_server_requests_seconds_sum{service=\"fcs-cerberus-uat\",cf_cluster=\"cerberus-uat-green\",cf_space=\"Adv-Eng_uat\",cf_instance_index=\"0\"})by(service, cf_cluster, cf_space, cf_instance_index, uri, status) [1m:30s]) > 0 / idelta(sum(http_server_requests_seconds_count{service=\"fcs-cerberus-uat\",cf_cluster=\"cerberus-uat-green\",cf_space=\"Adv-Eng_uat\",cf_instance_index=\"0\"})by(service, cf_cluster, cf_space, cf_instance_index, uri, status) [1m:30s])", "interval": "", "legendFormat": "Endpoint: {{uri}} Status: {{status}} Service: {{service}}, Application: {{cf_cluster}},  PCF Space: {{cf_space}}, Instance: {{cf_instance_index}}", "refId": "A" }, { "exemplar": true, "expr": "rate(sum(http_server_requests_seconds_sum{service=\"fcs-cerberus-uat\",cf_cluster=\"cerberus-uat-green\",cf_space=\"Adv-Eng_uat\",cf_instance_index=\"0\",status=\"200\",uri=\"/master-reset/api/deauthorize/v1/cerberus\"}) by(service, cf_cluster)[1m:10s]) / rate(sum(http_server_requests_seconds_count{service=\"fcs-cerberus-uat\",cf_cluster=\"cerberus-uat-green\",cf_space=\"Adv-Eng_uat\",cf_instance_index=\"0\",status=\"200\",uri=\"/master-reset/api/deauthorize/v1/cerberus\"}) by(service, cf_cluster)[1m:10s])", "hide": false, "interval": "", "legendFormat": "Application Average | Service: {{service}}, Application: {{cf_cluster}}", "refId": "B" }, { "exemplar": true, "expr": "rate(sum(http_server_requests_seconds_sum{service=\"fcs-cerberus-uat\",cf_cluster=\"cerberus-uat-green\",cf_space=\"Adv-Eng_uat\",cf_instance_index=\"0\",status=\"200\",uri=\"/master-reset/api/deauthorize/v1/cerberus\"}) by(service, cf_cluster, cf_space)[1m:10s]) / rate(sum(http_server_requests_seconds_count{service=\"fcs-cerberus-uat\",cf_cluster=\"cerberus-uat-green\",cf_space=\"Adv-Eng_uat\",cf_instance_index=\"0\",status=\"200\",uri=\"/master-reset/api/deauthorize/v1/cerberus\"})by(service, cf_cluster, cf_space)[1m:10s])", "hide": true, "interval": "", "legendFormat": "Space Average| Service: {{service}}, Application: {{cf_cluster}}, PCF Space: {{cf_space}}", "refId": "C" }, { "exemplar": true, "expr": "rate(sum(http_server_requests_seconds_sum{service=\"fcs-cerberus-uat\",cf_cluster=\"cerberus-uat-green\",cf_space=\"Adv-Eng_uat\",cf_instance_index=\"0\",status=\"200\",uri=\"/master-reset/api/deauthorize/v1/cerberus\"})by(service, cf_cluster, cf_space, cf_instance_index, uri, status)[1m:10s]) / rate(sum(http_server_requests_seconds_count{service=\"fcs-cerberus-uat\",cf_cluster=\"cerberus-uat-green\",cf_space=\"Adv-Eng_uat\",cf_instance_index=\"0\",status=\"200\",uri=\"/master-reset/api/deauthorize/v1/cerberus\"})by(service, cf_cluster, cf_space, cf_instance_index, uri, status)[1m:10s])", "hide": false, "interval": "", "legendFormat": "Endpoint: {{uri}} Status: {{status}} Service: {{service}}, Application: {{cf_cluster}},  Instance: {{cf_instance_index}}, PCF Space: {{cf_space}}", "refId": "D" } ], "title": "Average Endpoint Latency", "type": "timeseries" } ], "schemaVersion": 30, "style": "dark", "tags": [], "templating": { "list": [] }, "time": { "from": "now-2d", "to": "now" }, "timepicker": {}, "timezone": "", "title": "Cerberus 4 golden_vimal", "uid": "1xQOz-gnzdgnfd", "version": 1 }' -H "Content-Type:application/json"  -H "Authorization: Bearer $GRAFANA_AUTH" http://34.71.52.107:3000/api/dashboards/db"""
}
              

            }
        }
    }
}

