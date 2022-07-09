pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                sh "git clone https://github.com/Baruch-Grizman/WorldOfGames_test.git"
            }
        }
        stage('Build') {
            steps {
                sh "docker build -t wog_test ."
            }
        }
        stage('Run') {
            steps {
                sh "docker run -it -p 8777:5000 baruchgr/wog_test sh"
                sh "python3 ./data/MainScores_test.py"

            }
        }
        stage('Test') {
            steps {
                sh "python3 ./data/e2e.py"
            }
        }
        stage('Finalize') {
            steps {
                sh "docker tag wog_test baruchgr/wog_test"
                sh "docker push baruchgr/wog_test"
            }
        }
    }
}