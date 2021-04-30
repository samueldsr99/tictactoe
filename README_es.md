# Agente Minimax para TicTacToe

Este es un ejemplo básico de uso del algoritmo de búsqueda `minimax` en el juego `TicTacToe`. El agente selecciona el movimiento que maximice sus posibilidades de ganar, sin embargo no tiene en cuenta la cantidad de movimientos para ganar (de existir 2 o más formas de ganar, pudiera seleccionar la más larga). Además, asume que el rival siempre jugará de manera óptima.

## Ejecución

```bash
python3 main.py
```

## Detalles de implementación

> Toda la lógica del agente se implementó en el archivo `agent.py`, permitiendo que el usuario sea capaz de crear un agente por sí mismo para jugar a este juego, el agente creado por usted debe implementar el método `choice(state, turn)`, que recibe el estado actual y el turno del agente y devuelve un entero en el rango `[0..9]` con la posición de la casilla a jugar, las casillas para este caso están numeradas de la siguiente manera
```
 0 | 1 | 2
---|---|---
 3 | 4 | 5
---|---|---
 6 | 7 | 8
```
> Además, el archivo `state.py` contiene funciones útiles para manejar el estado actual.

> (Ver ejemplos de `RandomAgent` y `MinimaxAgent` en `agent.py`)
