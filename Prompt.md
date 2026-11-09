Vamos a hacer el ejercicio "TDD con IA"en este proyecto de Python (pytest).
Lee especificacion.md, juego.py (contrato con raise NotImplementedError) y
test_juego.py (3 pruebas iniciales mías, hechas SIN IA, que ya están en rojo).

REGLAS GENERALES
- Separación de roles: la fase ROJA (escribir pruebas) y la fase VERDE (escribir
  código) las ejecutas con SUBAGENTES DISTINTOS, cada uno con contexto limpio,
  para que quien implementa no haya visto cómo se escribieron las pruebas.
- El agente de la fase ROJA solo puede editar archivos test_*.py.
  El agente de la fase VERDE solo puede editar juego.py y main.py.
- Antes de cada fase verde haz un commit con el rojo. Después de cada fase verde
  ejecuta `git diff -- test_juego.py test_main.py`: si hay cualquier cambio en las
  pruebas, descártalo con `git checkout -- <archivo>`, repite la fase verde y avísame.
- Si git no está inicializado, haz `git init` y un commit inicial.
- Decisiones de diseño: check_try devuelve "mayor" si el secreto es mayor que el
  intento, "menor" si es menor y "correcto" si es igual; lanza ValueError si el
  intento no es un entero entre 1 y 100. calculate_score(attempts, won) devuelve
  0 si no ganó y 100 - 15*(attempts-1) si ganó.

PASO 1 (ROJO): Subagente de pruebas. Completa test_juego.py a partir de la
especificación: generate_number siempre en 1..100; check_try con mayor/menor/
correcto, límites 1 y 100 y entradas inválidas (0, 101, -5, 3.5, "abc") con
ValueError; calculate_score ganando en intentos 1..7 (100,85,70,55,40,25,10) y
perdiendo (0). Conserva mis 3 pruebas originales. No implementes nada.
Ejecuta pytest y verifica que TODO siga en rojo por NotImplementedError.
Commit: "rojo: pruebas completas".

PASO 2 (VERDE): Subagente nuevo. Implementa juego.py con el código mínimo para
pasar test_juego.py. PROHIBIDO modificar test_juego.py. Revisa con git diff
que no tocó las pruebas.

PASO 3: Ejecuta pytest. Si hay errores, pásale el traceback al subagente verde
para que corrija solo juego.py, y repite hasta que todo pase en verde.
Commit: "verde: funciones".

PASO 4 (ROJO del main): Subagente de pruebas. Crea test_main.py con pruebas del
main según la especificación. main.py tendrá main() y usará `import juego` para
llamar juego.generate_number(), juego.check_try() y juego.calculate_score(),
de modo que se puedan parchar con monkeypatch. Simula input() con monkeypatch y
revisa lo impreso con capsys. Casos: gana al primer intento (100 puntos, 1 intento);
pistas mayor y menor; se agotan los 7 intentos (avisa que perdió y muestra el
número secreto); entrada inválida (texto o fuera de 1-100) no consume intento y
vuelve a pedir. No crees main.py. Verifica que fallen (rojo).
Commit: "rojo: pruebas del main".

PASO 5 (VERDE del main): Subagente verde nuevo. Crea main.py con main() y
if __name__ == "__main__": main(), máximo 7 intentos, pistas, mensaje de victoria
con puntaje e intentos usados, mensaje de derrota con el número secreto.
PROHIBIDO tocar test_main.py y test_juego.py. Verifica con git diff, corre pytest
hasta que todo esté en verde y haz una partida de prueba con `python main.py`.
Commit: "verde: main".

PASO 6 (CAMBIO con prompt iterativo, primero ROJO y luego VERDE):
[META ORIGINAL]
Juego de adivinar un número del 1 al 100 en consola, máximo 7 intentos, pistas
mayor/menor, puntaje 100 al primer intento, -15 por intento extra, 0 si pierde.
[REFINAMIENTOS ANTERIORES]
Ninguno.
[ESTADO ACTUAL]
[x] juego.py y main.py implementados y en verde.
[ ] Opción de seguir jugando tras perder.
[NUEVO FEEDBACK]
- Si el jugador agota los 7 intentos y queda en 0 puntos, el juego pregunta si
  quiere seguir jugando hasta adivinar (s/n).
- Si responde "s", puede intentar sin límite de intentos hasta adivinar, con las
  mismas pistas. Al adivinar se le notifica; su puntaje final sigue siendo 0.
- Si responde "n", el juego termina mostrando el número secreto.
[RESTRICCIONES]
- No cambies la lógica de generate_number, check_try ni calculate_score.
- No rompas el comportamiento existente (7 intentos, pistas, puntaje, validación).
- No modifiques las pruebas existentes.
Ejecución: (a) subagente de pruebas agrega pruebas nuevas en test_main.py y
verificas que SOLO las nuevas fallen (rojo); commit "rojo: seguir jugando".
(b) Subagente verde nuevo modifica solo main.py; verifica con git diff que no
tocó pruebas; pytest todo en verde; commit "verde: seguir jugando".

AL FINAL entrégame un resumen corto: la salida de pytest de cada fase (rojo→verde),
la lista de commits (`git log --oneline`) y cualquier decisión que hayas tomado
por tu cuenta.