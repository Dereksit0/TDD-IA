import pytest

from juego import generate_number, check_try, calculate_score


def test_generate_number_en_rango():
    for _ in range(200):
        assert 1 <= generate_number() <= 100


def test_generate_number_devuelve_entero():
    assert isinstance(generate_number(), int)


def test_check_try_pistas():
    assert check_try(50, 30) == "mayor"
    assert check_try(50, 80) == "menor"
    assert check_try(50, 50) == "correcto"


@pytest.mark.parametrize(
    "secret, guess, esperado",
    [
        (50, 30, "mayor"),
        (50, 80, "menor"),
        (50, 50, "correcto"),
        (100, 1, "mayor"),
        (1, 100, "menor"),
        (1, 1, "correcto"),
        (100, 100, "correcto"),
    ],
)
def test_check_try_limites(secret, guess, esperado):
    assert check_try(secret, guess) == esperado


@pytest.mark.parametrize("guess", [0, 101, -5, 3.5, "abc"])
def test_check_try_entrada_invalida(guess):
    with pytest.raises(ValueError):
        check_try(50, guess)


def test_calculate_score_primer_intento_y_derrota():
    assert calculate_score(1, True) == 100
    assert calculate_score(3, True) == 70
    assert calculate_score(7, False) == 0


@pytest.mark.parametrize(
    "attempts, esperado",
    [(1, 100), (2, 85), (3, 70), (4, 55), (5, 40), (6, 25), (7, 10)],
)
def test_calculate_score_ganando(attempts, esperado):
    assert calculate_score(attempts, True) == esperado


@pytest.mark.parametrize("attempts", [1, 3, 7])
def test_calculate_score_perdiendo(attempts):
    assert calculate_score(attempts, False) == 0
