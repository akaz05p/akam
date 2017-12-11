#!/usr/bin/env groovy
pipeline {
    agent any
    stages {
        stage('Test') {
            steps {
                echo 'Testing...'                
                script {
                    for (def i = 1; i <= 10; i++) {
                        echo "Testing ${i} time..."
                        build(job:"Akamai")
                    }
                }
            }
        }
    }
    post {
        success {
             emailext (
                 subject: "SUCCESSFUL: Job '${env.JOB_NAME} [${env.BUILD_NUMBER}]'",
                 body: """<p>SUCCESSFUL: Job '${env.JOB_NAME} [${env.BUILD_NUMBER}]':</p><p>Check console output at "<a href="${env.BUILD_URL}">${env.JOB_NAME} [${env.BUILD_NUMBER}]</a>"</p>""",
                 recipientProviders: [[$class: 'DevelopersRecipientProvider']]
             )
        }
    }
}
