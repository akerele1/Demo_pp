pipeline {
    agent any
    stages {
        stage('Install Dependencies') {
            steps {
                bat 'C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python313\\python.exe -m pip install --user -r requirements.txt'
                bat 'C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python313\\python.exe -m playwright install chromium'
            }
        }
        stage('Run Tests') {
            steps {
                bat 'C:\\Users\\HP\\AppData\\Local\\Programs\\Python\\Python313\\python.exe -m pytest tests/ -v --html=report.html'
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
