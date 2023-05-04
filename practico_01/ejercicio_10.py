"""For-Else, Any."""

from typing import Iterable


def tiene_pares_basico(numeros: Iterable[int]) -> bool:
    """Toma una lista y devuelve un booleano en función si tiene al menos un
    número par."""
    for n in numeros:
        if n % 2 == 0:
            return True
    return False
# NO MODIFICAR - INICIO
assert tiene_pares_basico([1, 3, 5]) is False
assert tiene_pares_basico([1, 3, 5, 6]) is True
assert tiene_pares_basico([1, 3, 5, 600]) is True
# NO MODIFICAR - FIN


###############################################################################


def tiene_pares_for_else(numeros: Iterable[int]) -> bool:
    """Re-Escribir utilizando for-else con dos return y un break.
    Referencia: https://docs.python.org/3/tutorial/controlflow.html#break-and-continue-statements-and-else-clauses-on-loops
    """
    for n in numeros :
        if n % 2 == 0:
            return True
            break
    else:
        return False
    


# NO MODIFICAR - INICIO
assert tiene_pares_for_else([1, 3, 5]) is False
assert tiene_pares_for_else([1, 3, 5, 6]) is True
assert tiene_pares_for_else([1, 3, 5, 600]) is True
# NO MODIFICAR - FIN


###############################################################################


def tiene_pares_any(numeros: Iterable[int]) -> bool:
    """Re-Escribir utilizando la función any, sin utilizar bucles.
    Referencia: https://docs.python.org/3/library/functions.html#any
    """
    return any(n % 2 == 0 for n in numeros)
    # Any devuelve un bool si al menos uno de los elementos de la lista que le pasé como parámetro es True

# NO MODIFICAR - INICIO
assert tiene_pares_any([1, 3, 5]) is False
assert tiene_pares_any([1, 3, 5, 6]) is True
assert tiene_pares_any([1, 3, 5, 600]) is True
# NO MODIFICAR - FIN
