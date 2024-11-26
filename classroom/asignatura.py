class Asignatura:

    def __init__(self, nombre, salon = "remoto"):  # Se agregó un valor por defecto para el parámetro 'salon'.
        self._nombre = nombre
        self._salon = salon
    
    def __str__(self):  # Se implementó el método __str__, que estaba comentado en el código original.
        return self._nombre + " " + self._salon  # Este método devuelve una representación en cadena de la asignatura.
