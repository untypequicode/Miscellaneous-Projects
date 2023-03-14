class Planete():
    """
    Classe représentant une planète où les habitants utilisent un système monétaire donné et ont un certain argent.
    La classe permet de calculer les différentes possibilités de portefeuilles et les possibilités d'achats possibles.

    Attributs :
    -----------
    systeme_monetaire : list
        Liste des valeurs des différentes pièces et billets utilisés sur la planète.
    argent : int
        La somme d'argent que chaque habitant possède.

    Méthodes :
    ----------
    get_possibilites_portefeuille() -> list:
        Calcule toutes les combinaisons de pièces et billets qui peuvent être obtenus avec la somme d'argent donnée.
        Les combinaisons sont triées par ordre croissant.
        Retourne une liste de listes contenant les différentes combinaisons possibles.

    get_possibilites_achat() -> list:
        Calcule toutes les combinaisons de pièces et billets qui permettent de payer une somme donnée sans rendre la monnaie.
        Les combinaisons sont triées par ordre décroissant.
        Retourne une liste de listes contenant les différentes combinaisons possibles.

    __get_possibilites_achat_possibilite(tab: list) -> list:
        Calcule les différentes sommes que l'on peut payer avec une combinaison de pièces et billets donnée.
        Retourne une liste de sommes possibles.

    __calcul_possibilites_portefeuille(tab: list):
        Fonction récursive utilisée par get_possibilites_portefeuille pour calculer toutes les combinaisons possibles de pièces et billets.
        Modifie la liste possibilites_portefeuille_sans_tri.

    __tri(tab: list, is_list: bool = True) -> list:
        Trie la liste tab en supprimant les doublons.
        Si is_list est True, trie chaque liste de la liste tab par ordre croissant.
        Si is_list est False, trie la liste tab par ordre croissant.
        Retourne la liste triée.
    """
    def __init__(self, systeme_monetaire: list, argent: int):
        self.systeme_monetaire = systeme_monetaire
        self.argent = argent
        self.possibilites_portefeuille_tri = []
        self.possibilites_portefeuille_sans_tri = []
        self.possibilites_achat = []

    def get_possibilites_portefeuille(self) -> list:
        """
        Calcule et renvoie les différentes combinaisons de pièces et billets qui permettent d'obtenir la somme 
        désirée à partir du système monétaire de la planète.

        Returns:
            list: Une liste de listes représentant les différentes combinaisons de pièces et billets possibles.
        """
        self.possibilites_portefeuille_sans_tri = []
        for elem in self.systeme_monetaire:
            self.__calcul_possibilites_portefeuille([elem])
        self.possibilites_portefeuille_tri = self.__tri(self.possibilites_portefeuille_sans_tri)
        return self.possibilites_portefeuille_tri

    def get_possibilites_achat(self) ->list:
        """
        Retourne une liste contenant toutes les possibilités d'achats possibles,
        en triant les éléments par ordre croissant.

        Returns:
            list: Une liste contenant toutes les possibilités d'achats possibles, triées par ordre croissant.
        """
        possibilites = []
        for elem in self.possibilites_portefeuille_sans_tri:
            possibilites.append(self.__get_possibilites_achat_possibilite(elem))
        possibilites = self.__tri(possibilites)
        possibilites_portefeuille = []
        for elem in possibilites:
            for valeur in elem:
                boolean = True
                for element in possibilites:
                    boolean = boolean and (valeur in element)
                if boolean:
                    possibilites_portefeuille.append(valeur)
        
        possibilites_portefeuille = self.__tri(possibilites_portefeuille, False)    
        return possibilites_portefeuille

    def __get_possibilites_achat_possibilite(self, tableau: list) -> list:
        """
        Calcule toutes les possibilités d'achats pour une combinaison donnée de pièces et de billets.

        Args:
            tab (list): une liste contenant les valeurs des pièces et des billets utilisés pour effectuer l'achat.

        Returns:
            list: une liste de toutes les sommes possibles qui peuvent être payées avec la combinaison de pièces et de billets donnée en entrée. 
                  Le premier élément de la liste est toujours égal à 0, pour indiquer que l'on peut ne rien acheter avec cette combinaison.
        """
        possibilites = [0]
        for elem in tableau:
            possibilites.append(possibilites[-1] + elem)
        return possibilites

    def __calcul_possibilites_portefeuille(self, tableau: list):
        """
        Calcule toutes les combinaisons possibles de pièces ou de billets qui peuvent être utilisées pour atteindre la somme
        d'argent donnée pour cette planète.

        Args:
        tab (list): Combinaison partielle de pièces ou de billets. 

        Returns:
        None

        """
        """
        for elem in self.systeme_monetaire:
            nouvelle_somme = sum(tableau) + elem
            if sum(tableau) == self.argent:
                self.possibilites_portefeuille_sans_tri.append(list(tableau))
            elif nouvelle_somme == self.argent:
                nouvelle_liste = list(tableau)
                nouvelle_liste.append(elem)
                self.possibilites_portefeuille_sans_tri.append(nouvelle_liste)
            elif nouvelle_somme < self.argent:
                nouvelle_liste = list(tableau)
                nouvelle_liste.append(elem)
                self.__calcul_possibilites_portefeuille(nouvelle_liste)
        """
        for elem in self.systeme_monetaire:
            if sum(tableau) == self.argent:
                self.possibilites_portefeuille_sans_tri.append(list(tableau))
            elif sum(tableau) < self.argent:
                nouvelle_liste = list(tableau)
                nouvelle_liste.append(elem)
                self.__calcul_possibilites_portefeuille(nouvelle_liste)

    def __tri(self, tableau: list, is_list: bool = True) -> list:
        """
        Tri le tableau tab en ordre croissant ou décroissant en enlevant les doublons.

        Args:
        - tab (list) : le tableau à trier
        - is_list (bool) : indique si le tableau tab est une liste de listes (True par défaut) ou non

        Returns:
        - tab_result (list) : le tableau trié sans doublons

        """
        tableau_resultat = []
        if is_list:
            for elem in tableau:
                elem.sort()
                if not elem in tableau_resultat:
                    tableau_resultat.append(elem)
        else:
            tableau.sort()
            for elem in tableau:
                if not elem in tableau_resultat:
                    tableau_resultat.append(elem)
        return tableau_resultat


prince = Planete([1, 3, 10], 50)
print(prince.get_possibilites_portefeuille())
print(prince.get_possibilites_achat())