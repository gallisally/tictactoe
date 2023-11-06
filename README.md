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