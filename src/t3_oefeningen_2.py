import math


def is_even(x):
    if (x % 2) == 0:
        return True
    else :
        return false

def is_oneven(x):
    resultaat = is_even(x)
    if resultaat == True:
        return False
    else:
        return True


def volume_bol(r):
    Volume = 4 / 3 * math.pi * (r ** 3)
    return Volume


def oppervlakte_cirkel(r):
    oppervlakte  = 1 / 2 * 2 * math.pi * r ** 2
    return oppervlakte



def omtrek_cirkel(r):
    """Return omtrek cirkel met straal r"""
    # Deze functie kan je gebruiken om het volume van de donut te berekenen.
    result = 2 * r * math.pi
    return result


def volume_donut(r, R):
    """Return volume donut met straal r en R
    waarbij r de dikte van de donut is, en R
    de grootte van de donut.
    """
    if r == R:
        return -1
    else:
        result = 2 * math.pi ** 2 * r ** 2 * R
        return result


def stats(punten):
    gemiddelde = sum(punten) / len(punten)
    maximum = max(punten)
    minimum = min(punten)
    aantal = len(punten)
    resultaat = [gemiddelde, maximum, minimum, aantal]
    return resultaat


class Cirkel:
    def __init__(self, r):
        self.straal = r

    def omtrek(self):
        """Return de omtrek van de cirkel met straal r"""
        result = 2 * self.straal * math.pi
        return result

    def oppervlakte(self):
        """Return de oppervlakte van de cirkel met straal r"""
        result = 1 / 2 * 2 * math.pi * self.straal ** 2
        return result

    def __str__(self):
        """Return een string zoals aangegeven in de testen"""
        return f"cirkel met straal {self.straal}"


    def pythagoras(a, b):
        """Return de lengte van de schuine zijde als de lengtes
        van de rechthoekszijden gegeven zijn door a en b"""
        if a <= 0:
            return -1
        elif b <= 0:
            return -1
        else:
            result = math.sqrt(a ** 2 + b ** 2)
            return result


def is_palindroom(woord):
    """Return True als het omgekeerde van het woord gelijk
    is aan het woord zelf. Return anders False."""
    w = ",".join(woord)
    w = reversed(w)
    w = "".join(w)
    w = w.replace(",", "")
    if w == woord:
        return True
    else:
        return False
