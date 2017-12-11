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
                        timeout(3) {
                            build(job:"Akamai")
                        }
                    }
                }
            }
        }
    }
    post {
        success {
            echo "SUCCESSFUL: Job '${env.JOB_NAME} [${env.BUILD_NUMBER}]' (${env.BUILD_URL})"
        }
    }
}
