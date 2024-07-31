import pytest
from pregunta2.identificar_nivel_ventas import identificar_nivel_ventas


def test_identificar_nivel_ventas():
    assert identificar_nivel_ventas(40, 0) == "Baja"
    assert identificar_nivel_ventas(40, 1) == "Baja"
    assert identificar_nivel_ventas(75, 0) == "Media"
    assert identificar_nivel_ventas(120, 1) == "Media"
    assert identificar_nivel_ventas(81, 0) == "Alta"
    assert identificar_nivel_ventas(150, 1) == "Alta"

    with pytest.raises(ValueError):
        identificar_nivel_ventas(50, 2)
