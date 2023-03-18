class Planete():

    def __init__(self, systeme_monetaire: list, argent: int):
        self.systeme_monetaire = systeme_monetaire
        self.argent = argent
        self.possibilites_portefeuille_tri = []
        self.possibilites_portefeuille_sans_tri = []
        self.possibilites_achat = []
        self.file_path = "results.txt"

    def get_possibilites_portefeuille(self) -> list:
        self.possibilites_portefeuille_sans_tri = []
        for elem in self.systeme_monetaire:
            self.__calcul_possibilites_portefeuille([elem])
        self.possibilites_portefeuille_tri = self.__tri(self.possibilites_portefeuille_sans_tri)
        return self.possibilites_portefeuille_tri

    def get_possibilites_achat(self) ->list:
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
        possibilites = [0]
        for elem in tableau:
            possibilites.append(possibilites[-1] + elem)
        return possibilites

    def __calcul_possibilites_portefeuille(self, tableau: list):
        pile = [tableau]
        while pile:
            tableau = pile.pop()
            for elem in self.systeme_monetaire:
                if sum(tableau) == self.argent:
                    self.__ajouter_liste_au_fichier(self.possibilites_portefeuille_sans_tri, list(tableau))
                elif sum(tableau) < self.argent:
                    nouvelle_liste = list(tableau)
                    nouvelle_liste.append(elem)
                    pile.append(nouvelle_liste)

    def __tri(self, tableau: list, is_list: bool = True) -> list:
        tableau_resultat = []
        if is_list:
            for elem in tableau:
                elem.sort()
                if elem not in tableau_resultat:
                    tableau_resultat.append(elem)
        else:
            tableau.sort()
            for elem in tableau:
                if elem not in tableau_resultat:
                    tableau_resultat.append(elem)
        return tableau_resultat
    
    def __ajouter_liste_au_fichier(self, liste_resultats: list, nouvelle_liste: list):
        nouvelle_liste.sort()
        if nouvelle_liste not in liste_resultats:
            liste_resultats.append(nouvelle_liste)
            with open(self.file_path, "a") as f:
                f.write(str(nouvelle_liste) + "\n")

prince = Planete([1, 3, 10], 100)
print(prince.get_possibilites_portefeuille())
print(prince.get_possibilites_achat())