import com.fluttr.fltrJenkinsGlobalLib

def fltr

def buildTimestamp

pipeline {
    agent any

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
                script {
                    fltr = new fltrJenkinsGlobalLib()
                    buildTimestamp = fltr.buildTimestamp()
                }
            }
            post {
                success {
                    archiveArtifacts artifacts: '**/*.whl:${buildTimestamp}', fingerprint: true, allowEmptyArchive: true, onlyIfSuccessful: true
                }
            }
        }
    }
}