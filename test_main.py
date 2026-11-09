import re

import juego
import main

SECRETO = 50
_FIN = object()


def ejecutar(monkeypatch, capsys, respuestas, secreto=SECRETO):
    """Ejecuta main() con secreto fijo y entradas simuladas.

    Devuelve (salida_en_minusculas, iterador_restante).
    Si input() se agota, StopIteration se propaga (la prueba falla).
    """
    monkeypatch.setattr(juego, "generate_number", lambda: secreto)
    it = iter(respuestas)
    monkeypatch.setattr("builtins.input", lambda *a, **k: next(it))
    main.main()
    salida = capsys.readouterr().out.lower()
    return salida, it


def test_gana_al_primer_intento(monkeypatch, capsys):
    salida, _ = ejecutar(monkeypatch, capsys, ["50"])
    assert "100" in salida
    assert re.search(r"\b1\b", salida)
    assert "perdi" not in salida


def test_muestra_pistas_mayor_y_menor(monkeypatch, capsys):
    salida, _ = ejecutar(monkeypatch, capsys, ["10", "90", "50"])
    assert "mayor" in salida
    assert "menor" in salida


def test_pista_mayor(monkeypatch, capsys):
    salida, _ = ejecutar(monkeypatch, capsys, ["10", "50"])
    assert "mayor" in salida


def test_pista_menor(monkeypatch, capsys):
    salida, _ = ejecutar(monkeypatch, capsys, ["90", "50"])
    assert "menor" in salida


def test_pierde_tras_siete_intentos(monkeypatch, capsys):
    salida, it = ejecutar(monkeypatch, capsys, ["10"] * 7 + ["n"])
    assert "perdi" in salida
    assert "50" in salida
    assert next(it, _FIN) is _FIN


def test_gana_en_septimo_intento(monkeypatch, capsys):
    salida, _ = ejecutar(monkeypatch, capsys, ["10"] * 6 + ["50"])
    assert "perdi" not in salida
    assert "10" in salida  # 100 - 15*6 = 10 puntos
    assert re.search(r"\b7\b", salida)


def test_entradas_invalidas_no_consumen_intentos(monkeypatch, capsys):
    respuestas = ["abc", "0", "101"] + ["10"] * 7 + ["n"]
    salida, it = ejecutar(monkeypatch, capsys, respuestas)
    assert "perdi" in salida
    assert "50" in salida
    # Se consumieron las 10 respuestas: los 7 intentos validos se usaron.
    assert next(it, _FIN) is _FIN


def test_invalida_seguida_de_acierto_cuenta_un_intento(monkeypatch, capsys):
    salida, _ = ejecutar(monkeypatch, capsys, ["abc", "50"])
    assert "100" in salida
    assert re.search(r"\b1\b", salida)
    assert "perdi" not in salida


def test_fuera_de_rango_seguida_de_acierto(monkeypatch, capsys):
    salida, _ = ejecutar(monkeypatch, capsys, ["0", "101", "50"])
    assert "100" in salida
    assert "perdi" not in salida


# --- Modo continuo tras agotar los 7 intentos ---


def test_continua_tras_perder_y_adivina(monkeypatch, capsys):
    respuestas = ["10"] * 7 + ["s"] + ["10"] * 10 + ["50"]
    salida, it = ejecutar(monkeypatch, capsys, respuestas)
    assert "adivin" in salida
    assert next(it, _FIN) is _FIN
    assert "ganaste con" not in salida
    assert "100 puntos" not in salida
    assert re.search(r"puntaje\D{0,15}0\b", salida)


def test_no_continuar_muestra_secreto(monkeypatch, capsys):
    salida, it = ejecutar(monkeypatch, capsys, ["10"] * 7 + ["n"])
    assert "50" in salida
    assert next(it, _FIN) is _FIN


def test_continuo_con_entrada_invalida_luego_adivina(monkeypatch, capsys):
    respuestas = ["10"] * 7 + ["s", "abc", "50"]
    salida, it = ejecutar(monkeypatch, capsys, respuestas)
    assert "adivin" in salida
    assert next(it, _FIN) is _FIN


def test_continuo_sigue_mostrando_pistas(monkeypatch, capsys):
    # Pistas tras agotar los intentos: solo "mayor" en los 7 primeros,
    # solo "menor" en modo continuo.
    respuestas = ["10"] * 7 + ["s", "90", "50"]
    salida, _ = ejecutar(monkeypatch, capsys, respuestas)
    assert "menor" in salida


def test_ganar_a_tiempo_no_pregunta_seguir(monkeypatch, capsys):
    salida, it = ejecutar(monkeypatch, capsys, ["10", "10", "50"])
    assert "perdi" not in salida
    assert next(it, _FIN) is _FIN
