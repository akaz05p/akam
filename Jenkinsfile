pipeline {
    agent any

    stages {
        stage('Build') {
            steps {
                echo 'Building..'
            }
        }
        stage('Test01') {
            steps {
                echo 'Testing 1st time...'
            }
        }
        stage('Test02') {
            steps {
                echo 'Testing 2nd time...'
            }
        }
        stage('Test03') {
            steps {
                retry(3) {
                    echo 'Testing 3rd time...'
                }
            }
        }
        stage('Test04') {
            steps {
                echo 'Testing 4th time...'
            }
        }
        stage('Test05') {
            steps {
                echo 'Testing 5th time...'
            }
        }
        stage('Test06') {
            steps {
                echo 'Testing 6th time...'
            }
        }
        stage('Test07') {
            steps {
                echo 'Testing 7th time...'
            }
        }
        stage('Test08') {
            steps {
                echo 'Testing 8th time...'
            }
        }
        stage('Test09') {
            steps {
                echo 'Testing 9th time...'
            }
        }
        stage('Test10') {
            steps {
                echo 'Testing 10th time...'
            }
        }
    }
}
