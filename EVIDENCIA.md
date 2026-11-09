# Evidencia: TDD con IA (UMAD)

Juego de adivinar un número (1-100, 7 intentos, pistas mayor/menor).

## Explicación sencilla
TDD = primero escribes la prueba (falla, "rojo"), luego el código mínimo que la hace pasar ("verde").
Para que la IA no haga trampa, usé **dos agentes distintos**: uno solo escribe pruebas y otro solo escribe código.
Después de cada fase verde comprobé con `git diff` que el agente de código **no tocó las pruebas**.

## Línea de tiempo (cada commit se puede comprobar con `git checkout <hash>` + pytest)

| # | Commit | Qué se hizo | Resultado pytest |
|---|--------|-------------|------------------|
| 1 | `90bfbd8` rojo: contrato + 3 pruebas | Funciones vacías (`raise NotImplementedError`) + 3 pruebas | 3 failed |
| 2 | `4f46887` rojo: pruebas completas | Agente de pruebas amplía a 26 (límites, inválidos, puntajes 1..7) | 26 failed |
| 3 | `fe52a34` verde: funciones | Agente de código implementa `juego.py` | 26 passed |
| 4 | `365f2df` rojo: pruebas del main | Agente de pruebas escribe `test_main.py` (sin existir `main.py`) | error: no existe `main` |
| 5 | `ff70f7e` verde: main | Agente de código crea `main.py` | 35 passed |
| 6 | `fe971ac` rojo: seguir jugando | 5 pruebas nuevas del cambio (s/n tras perder) | 4 failed, 36 passed (solo fallan las nuevas) |
| 7 | (pendiente) verde: seguir jugando | `main.py` modificado, sin commit | 2 failed, 38 passed |

## Qué hace cada archivo
- `especificacion.md`: reglas del juego.
- `juego.py`: `generate_number`, `check_try`, `calculate_score`.
- `main.py`: el juego en consola (usa `juego.` para poder parchar en pruebas).
- `test_juego.py` (26 pruebas) y `test_main.py` (14 pruebas).

## Decisiones de diseño
- `check_try` → "mayor" si el secreto es mayor, "menor", "correcto"; `ValueError` si no es entero 1..100 (también rechaza bool).
- Puntaje: 0 si pierde; si gana `100 - 15*(intentos-1)`.
- Entrada inválida no gasta intento.

## Pendiente
Las 2 pruebas viejas del main (`test_pierde_tras_siete_intentos`, `test_entradas_invalidas_no_consumen_intentos`) chocan con la pregunta nueva s/n.
Decisión: añadirles `"n"` al final de sus respuestas (recomendado) o capturar `StopIteration` en `main.py` (hack).

## Cómo demostrarlo en vivo
```
git log --oneline
.venv\Scripts\python -m pytest -q
.venv\Scripts\python main.py
```
