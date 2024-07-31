import pytest
from pregunta1.obtener_dominio import obtener_dominio


def test_obtener_dominio():
    assert obtener_dominio("usuario@dominio.com") == "dominio.com"
    assert obtener_dominio("usuario@sub.dominio.com") == "sub.dominio.com"

    with pytest.raises(ValueError):
        obtener_dominio("usuario@")

    with pytest.raises(ValueError):
        obtener_dominio("usuariodominio.com")

    with pytest.raises(ValueError):
        obtener_dominio("usuario@dominio@otro.com")
