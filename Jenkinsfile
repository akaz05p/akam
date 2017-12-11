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
            mail to: cpeng@akamai.com, subject: '[Jenkins] ${env.JOB_NAME} completed.'
        }
    }
}
