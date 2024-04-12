pipeline {
    agent any
    
    stages {
        stage('Parallel Stage') {
            parallel {
                stage('Stage A') {
                    steps {
                        echo 'Executing Stage A'
                        
                    }
                }
                stage('Stage B') {
                    steps {
                        echo 'Executing Stage B'
                        
                    }
                }
                stage('Stage C') {
                    steps {
                        echo 'Executing Stage C'
                        
                    }
                }
            }
        }
    }
}
