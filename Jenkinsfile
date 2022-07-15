pipeline {
    agent any
    stages {
        stage('Checkout') {
            steps {
                bat "git clone https://github.com/Baruch-Grizman/WorldOfGames_test.git"
            }
        }
        stage('Build') {
            steps {
                bat "docker build -t wog_test ."
            }
        }
        stage('Run') {
            steps {
                bat "docker run --rm -d -p 8777:5000 wog_test"
                bat "pip install flask"
                bat "python ./data/MainScores_test.py"

            }
        }
        stage('Test') {
            steps {
                bat "python ./data/e2e.py"
            }
        }
        stage('Finalize') {
            steps {
                bat "docker tag wog_test baruchgr/wog_test"
                bat "docker push baruchgr/wog_test"
            }
        }
    }
}