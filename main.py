"""Module contenant une fonction vérifiant si une chaîne est un palindrome."""
#### Fonction secondaire


def ispalindrome(p):
    """Retourne True si p est un palindrome (accents et non-alphanum retirés)."""

    # votre code ici
    p = p.lower()
    p = p.replace("æ", "ae")
    p = p.replace("œ", "oe")
    intab = "àâäéèêëîïôöùûüçÿ"
    outtab = "aaaeeeeiioouuucy"
    trantab = p.maketrans(intab, outtab)
    p = p.translate(trantab)
    p = "".join(c for c in p if c.isalnum())

    g = p[0:len(p)//2]
    d = p[(len(p)+1)//2:]
    return g == d[::-1]

#### Fonction principale


def main():
    """Teste quelques chaînes pour vérifier la fonction ispalindrome()."""
    # vos appels à la fonction secondaire ici

    for s in ["radar", "kayak", "level", "rotor", "civique", "deifie"]:
        print(s, ispalindrome(s))


if __name__ == "__main__":
    main()
