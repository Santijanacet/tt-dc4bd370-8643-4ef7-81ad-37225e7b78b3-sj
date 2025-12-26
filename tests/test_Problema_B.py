import time
from src.problema_B import CacheEnMemoria


def test_establecer_y_obtener():
    cache = CacheEnMemoria(2, 5)
    cache.establecer("a", "1")
    assert cache.obtener("a") == "1"


def test_actualizar_clave_existente():
    cache = CacheEnMemoria(2, 5)
    cache.establecer("a", "1")
    cache.establecer("a", "2")
    assert cache.obtener("a") == "2"


def test_eliminar_clave():
    cache = CacheEnMemoria(2, 5)
    cache.establecer("a", "1")
    assert cache.eliminar("a") is True
    assert cache.obtener("a") is None


def test_obtener_clave_inexistente():
    cache = CacheEnMemoria(2, 5)
    assert cache.obtener("x") is None


def test_expiracion_por_ttl():
    cache = CacheEnMemoria(2, 1)
    cache.establecer("a", "1")
    time.sleep(1.2)
    assert cache.obtener("a") is None


def test_renovacion_ttl_al_obtener():
    cache = CacheEnMemoria(2, 1)
    cache.establecer("a", "1")
    time.sleep(0.6)
    assert cache.obtener("a") == "1"
    time.sleep(0.6)
    assert cache.obtener("a") == "1"


def test_desalojo_lru():
    cache = CacheEnMemoria(2, 10)
    cache.establecer("a", "1")
    cache.establecer("b", "2")
    cache.obtener("a")  # a es la más reciente
    cache.establecer("c", "3")

    assert cache.obtener("b") is None
    assert cache.obtener("a") == "1"
    assert cache.obtener("c") == "3"


def test_obtener_claves_y_valores():
    cache = CacheEnMemoria(2, 10)
    cache.establecer("a", "1")
    cache.establecer("b", "2")

    resultado = cache.obtener_claves_y_valores()
    assert resultado == {"a": "1", "b": "2"}


def test_estadisticas():
    cache = CacheEnMemoria(1, 1)
    cache.establecer("a", "1")
    time.sleep(1.2)
    cache.obtener("a")

    estadisticas = cache.obtener_estadisticas()
    assert estadisticas["expiraciones_por_ttl"] == 1