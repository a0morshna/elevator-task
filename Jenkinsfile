pipeline {
    agent any

    environment {
        BUILD_TS = getBuildTimestamp()
    }

    stages {

        stage('Checkout') {
            steps {
                checkout scm 
            }
        }

        stage('Install python') {
            steps {
                sh '''
                    version=$(python3 --version 2>&1 | grep -Po '(?<=Python )(.+)')
                    if [ -z "$version" ]
                    then
                        echo "No Python!"
                        sudo apt-get update
                        sudo apt install software-properties-common
                        sudo apt install python3.8
                    fi
                '''
            }
        }

        stage('Install packages'){
            steps{
                sh '''
                sudo apt install -y python-pip
                sudo apt install -y python3-setuptools
                sudo pip install wheel
                '''
            }
        }


        stage('Wheel archive') {
            steps {
                sh '''
                python3 setup.py sdist bdist_wheel 
                '''
            }
        }

        stage('Archive') {
            steps {
                archiveArtifacts artifacts: '**/*.whl:${BUILD_TS}', fingerprint: true, allowEmptyArchive: true, onlyIfSuccessful: true
            }
        }
    }
}

def getBuildTimestamp() {
    Date date = new Date()
    buildTimestamp = date.format('yy-MM-dd_HH-mm-ss')
    println("Generated Build Timestamp: " + buildTimestamp)
    return buildTimestamp
}