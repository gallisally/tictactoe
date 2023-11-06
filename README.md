# Juego de Cruz en Raya (Tic-Tac-Toe) con Django Channels

Este proyecto es una implementación del juego de "Cruz en Raya" (Tic-Tac-Toe) utilizando Django Channels, una extensión de Django que permite la comunicación en tiempo real a través de WebSockets. Permite a dos jugadores jugar al clásico juego de "Cruz en Raya" en línea.

## Características

- Juega en tiempo real contra otro jugador.
- Usa WebSockets para mantener actualizado el estado del juego.
- Realiza un seguimiento de los turnos de los jugadores y declara al ganador.
- Ofrece una experiencia de juego interactiva y dinámica.

## Requisitos

- Python 3.x
- Django
- Django Channels

## Instalación

1. Clona este repositorio:

   ```bash
   -git clone https://github.com/gallisally/tictactoe.git
   -cd tictactoe

2. Crea entorno virtual (recomendado)
   -python -m venv venv
   -source venv/bin/activate  # Linux/Mac
   # o
   -venv\Scripts\activate  # Windows

3. Instala las dependencias
   -pip install -r requirements.txt

4. Realiza las migraciones:
   -python manage.py makemigrations
   -python manage.py migrate

5. Ejecuta la app
   -python manage.py runserver

6. La app esta disponible en:  http://localhost:8000/

## Uso
Puede acceder al juego de tictactoe abriendo su navegador y navegando a http://localhost:8000/tictactoe/. Puede compartir el enlace con un amigo para jugar juntos.

## Caracteristicas
Juego de tictactoe en tiempo real utilizando Django Channels.
Soporte para múltiples salas de juegos.
Sistema de turnos para dos jugadores.
## Principales modulos
1. "game.html": Estilos CSS: Define estilos basicos CSS en línea para personalizar la apariencia de la página y los elementos del juego.

- Contenido Principal: La mayor parte del contenido principal se encuentra dentro del elemento con la clase "wrapper". Aquí se muestran detalles del juego, como el nombre del jugador, el ID de la sala y el estado del oponente. También se crea el tablero de juego dentro del elemento con la clase "container". Cada celda del tablero es un elemento con la clase "box".

- Script de JavaScript: Incluye un script de JavaScript que se encarga de gestionar la lógica del juego. Esto implica el manejo de turnos, la interacción del usuario al hacer clic en las celdas del tablero, el envío de datos al servidor a través de WebSocket y la actualización dinámica de la interfaz del juego.

- Librería SweetAlert2: Se enlaza con la librería SweetAlert2 para mostrar ventanas emergentes con mensajes y opciones interactivas, como mensajes de error, mensajes de victoria o empate, y la opción de reiniciar el juego.

2. 'consumers.py': El archivo "consumers.py" contiene una clase llamada GameConsumer, que es una clase de consumidor de WebSockets basada en Django Channels. Esta clase se encarga de manejar la lógica del juego de tres en raya (Tic-Tac-Toe) en tiempo real a través de WebSockets. A continuación, se comentan las diferentes funciones y métodos dentro de esta clase:

- board: Este diccionario representa el estado del tablero del juego. Cada clave (números del 0 al 8) se mapea a una casilla del tablero, y su valor inicial es una cadena vacía ('').

- connect: Este método se ejecuta cuando un nuevo cliente se conecta al WebSocket. Realiza las siguientes acciones:
   Obtiene el ID de la sala a partir de los argumentos de la URL.
   Comprueba si la sala está llena (máximo 2 personas) y, en ese caso, envía un mensaje de error al cliente y cierra la conexión.
   Agrega el canal actual (cliente) al grupo de la sala.
   Si la sala está llena (exactamente 2 personas), selecciona aleatoriamente al primer jugador y al segundo jugador y les envía un mensaje para iniciar el juego.
-receive_json: Este método se ejecuta cuando el servidor recibe un mensaje JSON del cliente.   Analiza el evento dentro del mensaje y realiza las siguientes acciones:

   Si el evento es "boardData_send," verifica si hay un ganador o empate en el tablero y envía un mensaje al grupo correspondiente con los resultados.
   Si no hay ganador ni empate, envía el tablero actualizado a los otros jugadores en la sala, junto con información sobre de quién es el turno.