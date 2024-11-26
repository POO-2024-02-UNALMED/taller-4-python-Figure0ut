from classroom.asignatura import Asignatura

class Grupo:
    grado = "Grado 12"  # Cambio: Se inicializó 'grado' con un valor predeterminado "Grado 12".

    def __init__(self, grupo="grupo predeterminado", asignaturas=[], estudiantes=[]):  
        # Cambio: El valor por defecto del parámetro 'grupo' se cambió a "grupo predeterminado".
        # Cambio: Los parámetros 'asignaturas' y 'estudiantes' ahora tienen listas vacías como valores por defecto.
        self._grupo = grupo
        self._asignaturas = asignaturas
        self.listadoAlumnos = estudiantes

    def listadoAsignaturas(self, **kwargs):  
        # Cambio: El método ahora utiliza argumentos con nombre (**kwargs) en lugar de un diccionario como argumento.
        for x in kwargs.values():
            self._asignaturas.append(Asignatura(x))

    def agregarAlumno(self, alumno="", lista=None):
        # Cambio: Se modificó la implementación del parámetro 'lista'. Ahora, si no se pasa un valor, será 'None',
        # y se inicializará como una lista vacía dentro del método en lugar de usar una lista mutable como valor predeterminado.
        if lista == None:
            lista = []
        lista.append(alumno)
        self.listadoAlumnos = lista  # Cambio: Ahora 'self.listadoAlumnos' se asigna directamente a 'lista'.

    def __str__(self):
        # Cambio: Se implementó el método __str__, que estaba comentado en el código original.
        # Este método devuelve una descripción en cadena del grupo.
        return "Grupo de estudiantes: " + self._grupo

    @ classmethod
    def asignarNombre(cls, nombre="Grado 10"):
        cls.grado = nombre
    
    @ classmethod
    def asignarNombre(cls, nombre="Grado 4"):
        cls.grado = nombre

    @ classmethod
    def asignarNombre(cls, nombre="Grado 6"):
        cls.grado = nombre
