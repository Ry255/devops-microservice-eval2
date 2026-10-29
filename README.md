
# Evaluación Parcial N°2 - Ingeniería DevOps

**Estudiante:** Cristobal Emir Sanhueza Fernandez
**Sección:** 801D
**Repositorio:** https://github.com/Ry255/devops-microservice-eval2

## 📖 Descripción del Proyecto

Este proyecto consiste en un microservicio básico desarrollado en Python con **FastAPI**, el cual ha sido contenerizado y automatizado mediante un pipeline de Integración y Entrega Continua (CI/CD) utilizando **GitHub Actions**. El objetivo principal es demostrar la implementación de buenas prácticas DevOps, incluyendo pruebas automatizadas, análisis de seguridad, orquestación de contenedores y despliegue en la nube (AWS EC2).

## 🛠️ Tecnologías y Herramientas Utilizadas

*   **Lenguaje:** Python 3.11
*   **Framework:** FastAPI / Uvicorn
*   **Contenedores:** Docker y Docker Compose
*   **CI/CD:** GitHub Actions
*   **Pruebas Unitarias:** PyTest
*   **Análisis de Calidad y Seguridad:** SonarCloud
*   **Gestión de Dependencias:** Dependabot
*   **Nube:** AWS EC2 (Ubuntu 26.04 LTS)

## ⚙️ Arquitectura del Pipeline CI/CD

El pipeline se activa automáticamente con cada `push` a la rama `main` y consta de tres etapas (jobs) secuenciales:

1.  **Build & Test (IE1, IE2):**
    *   Instala las dependencias de Python.
    *   Ejecuta las pruebas unitarias con `pytest` y genera un reporte de cobertura.
    *   Construye la imagen Docker del microservicio.
2.  **Security & Quality (IE3):**
    *   Descarga el reporte de cobertura generado en el paso anterior.
    *   Ejecuta el escaneo de código estático con **SonarCloud**.
    *   *Bloqueo:* Si SonarCloud detecta fallas críticas de seguridad o calidad, el pipeline se detiene y no permite el despliegue.
3.  **Deploy to EC2 (IE4, IE5):**
    *   Se conecta vía SSH a la instancia de AWS EC2.
    *   Descarga la última versión del código (`git pull`).
    *   Levanta los servicios utilizando **Docker Compose** (`docker compose up -d --build`).
    *   Realiza un *Health Check* para verificar que el servicio esté en línea.

## 📦 Orquestación de Contenedores (IE5)

Para la orquestación, se utiliza **Docker Compose**. El archivo `docker-compose.yml` define la configuración del contenedor del microservicio (puerto 8000, variables de entorno y políticas de reinicio). Esto permite que el despliegue en el entorno cloud (EC2) sea reproducible y fácil de gestionar.

## 📊 Trazabilidad y Calidad (IE4, IE3)

*   **Trazabilidad:** Cada ejecución del pipeline está vinculada a un *commit* específico (identificado por su SHA). Los logs de GitHub Actions y la terminal de la EC2 registran qué versión exacta del código fue desplegada.
*   **Calidad:** Garantizada por la ejecución obligatoria de pruebas unitarias antes de construir la imagen y por el escaneo de seguridad bloqueante de SonarCloud.
*   **Dependencias:** Dependabot revisa semanalmente los paquetes de Python, las imágenes de Docker y las Actions para mantener el proyecto actualizado y seguro.

## 🚀 Cómo probar el servicio

El servicio se encuentra desplegado en la nube y puede ser probado accediendo a las siguientes rutas:

*   **Endpoint Raíz:** `http://http://54.226.63.48:8000/`
    *   *Respuesta esperada:* `{"message": "Hola desde el microservicio DevOps", "version": "2.0.0..."}`
*   **Health Check:** `http://http://54.226.63.48:8000/health`
    *   *Respuesta esperada:* `{"status": "ok"}`

*(Nota: El servicio está corriendo actualmente en la instancia EC2 del estudiante).*

---

## 🤖 Declaración de Uso de Inteligencia Artificial

De acuerdo con las indicaciones de la evaluación, declaro el uso de herramientas de IA de la siguiente manera:

*   **Herramientas utilizadas:** ChatGPT (Modelo de Lenguaje).
*   **Aplicación:** La IA fue utilizada como apoyo para la estructuración inicial del pipeline en formato YAML, la resolución de errores de configuración (ej. transición a `sonarqube-scan-action@v6`) y la redacción de la estructura de este documento README.
*   **Validación:** Todo el código y comandos sugeridos por la IA fueron revisados, probados y validados en el entorno local y en la instancia EC2 por el estudiante.

---

## 💭 Reflexión Personal

**Mi aprendizaje:**
Debido a que realice este trabajo de manera individual fue complicado obligarme a aprender y evitar lo mas posible el uso de IA en el trabajo, aun asi me sorprendo a mi mismo de lo que realmente se y no se, debido a que no soy alguien que repase mucho a veces pienso que olvido lo que pasan en clases, pero despeus de estar haciendo un trabajo en poco tiempo vuelve todo lo pasado en clases y soy capaz de seguir por mi cuenta y agradezco que esta vez el push a GitHub no tuvo problemas a diferencia de fullstack II.

**Dificultades superadas:**
El mayor problema fue conectar mi GitHub a EC2, que habia olvidado agregar los puertos en los grupos de seguridad, despues un problema de pipeline con SornarCloud porque lo marcaba como obsoleta y creo muchas ramas (estan en el repositorio, pense en borrarlas porque se ve feo, pero por mostrar el error y dejar constancia las dejare), al final leyendo en si los errores y buscando el error en foros pude arreglarlo y que no pasara con los proximos push. 

**Conclusión:**
Me parece interesante lo que realice y lo que hemos visto en clases, la verdad las pestañas que tuve que abrir en GitHub como en secrets y actions son cosas que nunca toque en mi vida cuando abro un repositorio, es interesante ver lo mucho que se puede hacer ahi y las muchas cosas que puede almacenar un repositorio, espero poder aprender mas y dejar algun dia algo interesante con GitHub, como un mod para algun juego que requiera actualizaciones constantes por ejemplo.
