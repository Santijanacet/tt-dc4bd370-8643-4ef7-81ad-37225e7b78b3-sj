def minimoSalasReuniones(reuniones):
    
    if not reuniones:
        return 0

    def a_minutos(hora):
        """Convierte 'HH:MM' a minutos."""
        h, m = map(int, hora.split(":"))
        return h * 60 + m

    
    eventos = []
    
    for inicio, fin in reuniones:
        eventos.append((a_minutos(inicio), 1))   
        eventos.append((a_minutos(fin), -1))     

   
    eventos.sort(key=lambda x: (x[0], x[1]))

    salas_activas = 0
    max_salas = 0

    for tiempo, tipo in eventos:
        salas_activas += tipo
        max_salas = max(max_salas, salas_activas)

    return max_salas