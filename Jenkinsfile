pipeline { 
    agent any 

    stages { 
        stage('Preparar entorno') { 
            steps { 
                echo "Creando entorno virtual..." 
                // Crear entorno virtual
                bat '"C:/Users/BRAYAN XD/AppData/Local/Programs/Python/Python313/python.exe" -m venv venv'
                
                // Instalar dependencias dentro del entorno
                bat '''
                call venv\\Scripts\\activate.bat
                pip install -r requirements.txt
                '''
            } 
        } 

        stage('Ejecutar script') { 
            steps { 
                echo "Ejecutando script principal..." 
                bat '''
                call venv\\Scripts\\activate.bat
                python /hello.py
                '''
            } 
        } 
    } 

    post { 
        success { echo "✅ Pipeline completado con éxito" } 
        failure { echo "❌ Error en alguna etapa del pipeline" } 
    } 
}
