def convert_number(element):
    # Vérifie si l'élément est composé uniquement de chiffres (entier)
    if element.isdigit():
        return int(element)
    # Vérifie si l'élément est un nombre décimal avec un point ou une virgule
    elif element.replace(".", ",", 1).replace(",", "", 1).isdigit():
        # Correction : Utilisez la méthode format pour formater le nombre décimal
        return "{:.2f}".format(float(element))
    # Si l'élément ne correspond à aucun des cas précédents, retourne None
    else:
        return None
