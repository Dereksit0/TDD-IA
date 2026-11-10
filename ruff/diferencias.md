# Ejercicio Ruff: diferencias

## 1. Errores iniciales por regla (original: 13 errores)

| Regla | Cantidad | Qué es | Quién lo resolvió |
|---|---|---|---|
| F401 | 3 | import sin usar (`sys`, `os`, `sqrt`) | ruff `--fix` |
| F841 | 3 | variable asignada y no usada (`error`, `weights`, `average`) | `error`: ruff; `weights` y `average`: manual |
| I001 | 1 | imports sin ordenar | ruff `--fix` |
| F632 | 1 | `is` con literal (`is "approved"`) | ruff `--fix` |
| UP009 | 1 | declaración `# coding: utf-8` innecesaria (línea 2) | protegida con `# noqa: UP009` |
| F402 | 1 | `sqrt` importado y sombreado por la variable del `for` | desapareció al borrar el import; renombré la variable a `student` |
| F601 | 1 | clave `"exam"` repetida en el diccionario | manual (se borró `weights`, que no se usaba) |
| F524 | 1 | `.format` sin argumento para el 2.º `{}` | manual |
| F821 | 1 | nombre no definido `averge` | manual (typo) |
| **Total** | **13** | | |

Resultado: antes 13 errores, después `All checks passed!` (0).
Al corregir F524 apareció una regla nueva (UP032, usar f-string) que antes quedaba oculta; la arregló ruff con `--fix`.

## 2. Qué cambió la IA (diff original → con_ia)

- Línea 2: se conserva y se añadió `  # noqa: UP009`. Python sigue detectando `utf-8` (verificado con `tokenize.detect_encoding`).
- Se eliminaron los imports `sys`, `os` y `from math import sqrt` (ninguno se usaba).
- Se eliminó `weights` (variable nunca usada y con clave duplicada).
- `summarize_grades`: se agregó el cálculo de `highest` y el `return` ahora usa un f-string con `average` y `highest` (antes lanzaba `NameError`).
- `print_approved`: la variable `sqrt` se renombró a `student`; `except ValueError as error` pasó a `except ValueError`; `is "approved"` pasó a `== "approved"`.

Salida del programa: `Average: 8.166666666666666 / Max: 9` y `Ana 20`.

### Hecho por ruff solo (`--fix`)
I001, F401 x3, F841 (`error`), F632 y UP032. (UP009 se habría borrado la línea 2, por eso la protegí con noqa antes.)

### Hecho a mano
Borrar `weights` (F841 + F601), `average` en F841 (pasó a usarse), F524 y F821 (typo `averge` y segundo valor del `format`), y renombrar la variable para el F402.

### Atención: cambio de comportamiento inevitable
El original **no se ejecutaba**: `summarize_grades` lanzaba `NameError` (`averge`) y además faltaba un argumento para `Max`.
No había valor definido para "Max", así que **decidí** usar el mayor de las notas (`highest`). Es una interpretación mía, conviene revisarla.
`ruff --fix --unsafe-fixes` por sí solo habría dejado la función rota (borra `average` y deja `averge`).

## 3. Diferencias IA vs sin IA (BORRADOR: lo reescribo con mis palabras)

**Borrador A**
Con IA el trabajo fue por capas: ruff arregló solo 6 de 13 errores, y la IA resolvió el resto y explicó cada decisión. Sin IA hay que leer cada mensaje de ruff y decidir a mano, lo que es más lento pero obliga a entender cada regla.

**Borrador B**
El mayor riesgo con IA es que cambie el comportamiento sin que se note: aquí el código no corría, y la IA tuvo que inventar qué significa "Max". Sin IA la persona decide eso conscientemente. A favor de la IA: avisó de la trampa de la línea 2 (`--fix` la habría borrado) y de que corregir un error destapó otro (UP032).

_Pendiente: comparar con `sin_ia/` cuando la termines (tiempo real, errores, decisiones)._
