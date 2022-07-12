# proyectoFinal
Individual final

#Monitoreo de Adultos Mayores
Esta aplicación está pensada como un servicio gratuito de la Municipalidad para sus vecinos. 
Dicho esto, la aplicación permite que cada vecino, pueda ingresar los datos de un adulto mayor, junto a una prescripción médica firmada y nos indique en que horarios se debe tomar los remedios de esta prescripción, de esta forma una persona llama telefónicamente al adulto mayor. <br>

#Comenzando 🚀
Debes descargar el aplicativo de mi github maspee con el nombre final_individual.

#Pre-requisitos 📋
Activar entorno virtual en Visual Studio Code. En caso de no tener instalado un entorno virtual, debes instalarlo y activarlo.
Una vez activo el entorno virtual, ir a la carpeta del aplicativo y ejecutar python.manage.py runserver

#Ejecutando las pruebas ⚙️
La aplicación comienza en la página principal con un mensaje de bienvenida, que nos explica para que sirve y nos da la opción de Ingresar. 
Esto nos lleva a la pagina de prescripciones médicas y nos permite agregar. Es necesario estar registrado para poder ingresar prescripciones. La aplicación nos permite registrarnos como usuarios. 
Pasos para prueba: 
Ingrese a http://127.0.0.1:8000/ y seleccione Registrate.
Crear usuario.
Ingresa a la aplicación con el usuario recién creado.
En la opción Prescripción médica, agrega una prescripción.
En la opción Contáctanos, podemos dejar mensajes para contactar al administrador de la aplicación.
Intenta eliminar o editar comentarios anteriores.

#Analice las pruebas end-to-end 🔩
Con estas pruebas deducimos lo siguiente:
El sistema graba nuevos usuarios.
Valida que el formulario de creación de usuarios trabaja correctamente.
El sistema permite ingresar prescripciones médicas.
Valida que el formulario trabaja correctamente. 
Valida que no es posible eliminar o editar publicaciones de otro usuario. 

#Construido con 🛠️
El aplicativo esta desarrollado con en el framework Django versión 4.0.5, desarrollado en Python versión 3.10.4.
Utiliza una base de datos PostgreSQL, administrada con pgAdmin..
Para el desarrollo se ha utilizado el editor Visual Studio Code versión 1.69.0.
El aplicativo ha sido probado con Google Chrome

#Autores ✒️
En este proyecto individual participaron activamente: 
•	Mauricio Aspeé Ramos - Alumno - maspee 
•	Joshua Olave - Profesor - jm-olave 

#Expresiones de Gratitud 🎁
•	Gracias a mi familia por el apoyo y atención en este periodo de aprendizaje. 🤓
