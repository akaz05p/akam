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
}
