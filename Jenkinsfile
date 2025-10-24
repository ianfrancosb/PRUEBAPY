pipeline {
    agent any

    environment {
        EMAIL_RECIPIENTS = "tu_correo@mapfre.com, otro@correo.com"
    }
    stages {
        stage('Preparar entorno') {
            steps {
                echo "🔧 Creando entorno virtual..."
                bat '"C:/Users/BRAYAN XD/AppData/Local/Programs/Python/Python313/python.exe" -m venv venv'
                bat 'venv\\Scripts\\activate && pip install -r requirements.txt || echo Sin requerimientos adicionales'
            }
        }
        stage('Ejecutar script de reporte') {
            steps {
                echo "📄 Ejecutando script de Python..."
                bat 'venv\\Scripts\\activate && python reporte_clientes.py'
            }
        }
        stage('Publicar resultados') {
            steps {
                echo "📤 Mostrando contenido del reporte:"
                bat 'type reporte.txt'
            }
        }
    }
    post {
        success {
            emailext(
                subject: "✅ Pipeline exitoso - Reporte Clientes Mapfre",
                body: "El pipeline se ejecutó correctamente y se generó el reporte de clientes.",
                to: "${EMAIL_RECIPIENTS}",
                attachmentsPattern: 'reporte.txt'
            )
            echo "✅ Pipeline completado y correo enviado."
        }
        failure {
            emailext(
                subject: "❌ Error en Pipeline - Reporte Clientes Mapfre",
                body: "El pipeline falló durante la ejecución. Revisar Jenkins para más detalles.",
                to: "${EMAIL_RECIPIENTS}"
            )
            echo "❌ Error en el pipeline."
        }
    }
}
