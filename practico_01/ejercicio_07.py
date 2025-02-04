"""Slicing."""

# a[start:stop:step] start through not past stop, by step

def es_palindromo(palabra: str) -> bool:
    """Toma un string y devuelve un booleano en base a si se lee igual al
    derecho y al revés.

    Restricción: No utilizar bucles - Usar Slices de listas.
    Referencia: https://docs.python.org/3/tutorial/introduction.html#lists
    """
    
    return palabra == palabra[::-1]
    # con ::-1 estoy pidiendo que me devuelva la palabra al revés, y asé compararla con la palabra original

# NO MODIFICAR - INICIO
assert not es_palindromo("amor")
assert es_palindromo("radar")
assert es_palindromo("")
# NO MODIFICAR - FIN


###############################################################################


def mitad(palabra: str) -> str:
    """Toma un string y devuelve la mitad. Si la longitud es impar, redondear
    hacia arriba.

    Restricción: No utilizar bucles - Usar Slices de listas.
    Referencia: https://docs.python.org/3/tutorial/introduction.html#lists
    """
    if len(palabra) % 2 == 0:
        return palabra[:len(palabra)//2]
    else:
        return palabra[:len(palabra)//2 + 1]
    
    #Hay que usar doble barra para las divisiones enteras y una sola para las decimales

# NO MODIFICAR - INICIO
assert mitad("hello") == "hel"
assert mitad("Moon") == "Mo"
assert mitad("") == ""
# NO MODIFICAR - FIN
