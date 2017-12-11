pipeline {
    agent any
    stages {
        stage('Test') {
            steps {
                echo 'Testing...'                
                script {
                    for (int i = 1; i <= 10; i++) {
                        echo "Testing ${i} time..."
                        build("Akamai")
                    }
                }
            }
        }
    }
}
