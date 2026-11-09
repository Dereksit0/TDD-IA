from juego import generate_number, check_try, calculate_score


def test_generate_number_en_rango():
    for _ in range(200):
        assert 1 <= generate_number() <= 100


def test_check_try_pistas():
    assert check_try(50, 30) == "mayor"
    assert check_try(50, 80) == "menor"
    assert check_try(50, 50) == "correcto"


def test_calculate_score_primer_intento_y_derrota():
    assert calculate_score(1, True) == 100
    assert calculate_score(3, True) == 70
    assert calculate_score(7, False) == 0
