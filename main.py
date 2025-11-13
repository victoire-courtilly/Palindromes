#### Fonction secondaire


def ispalindrome(p):

    # votre code ici
    i = 0
    while i < len(p)//2 :
        if p[i] != p[len(p)-1-i] :
            return False
        i += 1
    return True

#### Fonction principale


def main():

    # vos appels à la fonction secondaire ici

    for s in ["radar", "kayak", "level", "rotor", "civique", "deifie"]:
        print(s, ispalindrome(s))


if __name__ == "__main__":
    main()