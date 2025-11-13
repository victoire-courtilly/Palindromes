#### Fonction secondaire


def ispalindrome(p):

    # votre code ici
    g = p[0:len(p)//2] 
    d = p[(len(p)+1)//2:] 
    return g == d[::-1]

#### Fonction principale


def main():

    # vos appels à la fonction secondaire ici

    for s in ["radar", "kayak", "level", "rotor", "civique", "deifie"]:
        print(s, ispalindrome(s))


if __name__ == "__main__":
    main()