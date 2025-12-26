import pytest
from src.problema_A import minimoSalasReuniones


def test_lista_vacia():
    assert minimoSalasReuniones([]) == 0


def test_una_sola_reunion():
    reuniones = [["08:00", "09:00"]]
    assert minimoSalasReuniones(reuniones) == 1


def test_reuniones_sin_solapamiento():
    reuniones = [
        ["08:00", "09:00"],
        ["09:00", "10:00"],
        ["10:00", "11:00"],
    ]
    assert minimoSalasReuniones(reuniones) == 1


def test_reuniones_con_solapamiento_parcial():
    """Algunas reuniones se solapan."""
    reuniones = [
        ["08:30", "09:45"],
        ["09:00", "10:30"],
        ["10:30", "11:30"],
    ]
    assert minimoSalasReuniones(reuniones) == 2


def test_reuniones_con_solapamiento_total():
    """Todas las reuniones se solapan."""
    reuniones = [
        ["08:00", "12:00"],
        ["09:00", "11:00"],
        ["10:00", "13:00"],
    ]
    assert minimoSalasReuniones(reuniones) == 3


def test_inicio_igual_a_fin():
    reuniones = [
        ["08:00", "09:00"],
        ["09:00", "10:00"],
    ]
    assert minimoSalasReuniones(reuniones) == 1


def test_varios_eventos_mismo_horario():
    reuniones = [
        ["08:00", "09:00"],
        ["08:00", "09:00"],
        ["09:00", "10:00"],
    ]
    assert minimoSalasReuniones(reuniones) == 2


def test_reuniones_desordenadas():
    reuniones = [
        ["10:00", "11:00"],
        ["08:00", "09:00"],
        ["09:30", "10:30"],
    ]
    assert minimoSalasReuniones(reuniones) == 2
