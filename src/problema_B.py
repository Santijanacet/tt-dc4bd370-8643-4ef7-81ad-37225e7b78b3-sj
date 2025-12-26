import time
from collections import OrderedDict


class CacheEnMemoria:

    def __init__(self, capacidad: int, ttl_segundos_por_defecto: int):
       
        self.capacidad = capacidad
        self.ttl_por_defecto = ttl_segundos_por_defecto
        self.cache = OrderedDict()
        self.estadisticas = {
            "llamadas_totales": 0,
            "expiraciones_por_ttl": 0,
            "desalojos_por_lru": 0,
        }

    def _obtener_tiempo_actual(self) -> float:
        return time.time()

    def _esta_expirado(self, momento_expiracion: float) -> bool:
        return momento_expiracion < self._obtener_tiempo_actual()

    def _limpiar_expirados(self) -> None:
        claves_a_eliminar = [
            clave for clave, (_, momento_exp) in self.cache.items()
            if self._esta_expirado(momento_exp)
        ]
        
        for clave in claves_a_eliminar:
            del self.cache[clave]
            self.estadisticas["expiraciones_por_ttl"] += 1

    def establecer(self, clave: str, valor: str) -> None:
        self.estadisticas["llamadas_totales"] += 1
        self._limpiar_expirados()

        momento_expiracion = self._obtener_tiempo_actual() + self.ttl_por_defecto

        # Si la clave existe, la eliminamos para recrearla
        if clave in self.cache:
            del self.cache[clave]

        self.cache[clave] = (valor, momento_expiracion)
        self.cache.move_to_end(clave)

        # Si se supera la capacidad, desalojamos el elemento más antiguo
        if len(self.cache) > self.capacidad:
            self.cache.popitem(last=False)
            self.estadisticas["desalojos_por_lru"] += 1

    def obtener(self, clave: str) -> str | None:
        self.estadisticas["llamadas_totales"] += 1

        if clave not in self.cache:
            return None

        valor, momento_expiracion = self.cache[clave]

        # Si ha expirado, lo eliminamos y retornamos None
        if self._esta_expirado(momento_expiracion):
            del self.cache[clave]
            self.estadisticas["expiraciones_por_ttl"] += 1
            return None

        # Actualizamos la posición LRU y renovamos el TTL
        self.cache.move_to_end(clave)
        self.cache[clave] = (valor, self._obtener_tiempo_actual() + self.ttl_por_defecto)

        return valor

    def eliminar(self, clave: str) -> bool:
        if clave in self.cache:
            del self.cache[clave]
            return True
        return False

    def obtener_claves_y_valores(self) -> dict:
        self._limpiar_expirados()
        return {clave: valor for clave, (valor, _) in self.cache.items()}

    def obtener_estadisticas(self) -> dict:
        return {
            "llamadas_totales": self.estadisticas["llamadas_totales"],
            "elementos_actuales": len(self.cache),
            "expiraciones_por_ttl": self.estadisticas["expiraciones_por_ttl"],
            "desalojos_por_lru": self.estadisticas["desalojos_por_lru"],
        }