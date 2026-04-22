pipeline {
    agent any
    stages {
        stage('Install Dependencies') {
            steps {
                bat 'python -m pip install -r requirements.txt'
                bat 'playwright install chromium'
            }
        }
        stage('Run Tests') {
            steps {
                bat 'python -m pytest tests/ -v --html=report.html'
            }
        }
    }
    post {
        always {
            publishHTML(target: [
                allowMissing: false,
                alwaysLinkToLastBuild: true,
                keepAll: true,
                reportDir: '.',
                reportFiles: 'report.html',
                reportName: 'Playwright Test Report'
            ])
        }
    }
}
