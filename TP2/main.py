import numpy as np

class Node:
    def __init__(self, content, left: 'Node'=None, right: 'Node'=None):
        self.content = content
        self.left = left
        self.right = right


class ABR():
    def __init__(self, racine: Node=None):
        self.racine = racine

    def __repr__(self):
        return self._repr(self.racine)

    def _repr(self, racine):
        if racine is None:
            return ""
        result = f"{racine.content}"
        if racine.left is not None or racine.right is not None:
            result += f"Gauche={self._repr(racine.left)} Droite={self._repr(racine.right)}"
        return result

    def inserer(self, racine, valeur):
        if racine is None:
            return Node(valeur)
        
        if racine.content < valeur:
            racine.right = self.inserer(racine.right, valeur)
        else:
            racine.left = self.inserer(racine.left, valeur)

        return racine

    def nb_noeuds(self, racine: Node):
        if racine is None:
            return 0
        return 1 + self.nb_noeuds(racine.right) + self.nb_noeuds(racine.left)

    def existe(self, racine, valeur: int):
        if racine.content is None:
            return False
        
        if racine.content == valeur:
            return True

        return self.existe(racine.right) or self.existe(racine.left) 

    def balancer(self, racine):
        
    def existe_compt(self, racine, valeur: int, compteur: int = 0) -> tuple[bool, int]:
        if racine is None:
            return False, compteur+1

        if racine.content == valeur:
            return True, compteur

        droite_result = self.existe_compt(racine.right, valeur, compteur+1)
        gauche_result = self.existe_compt(racine.left, valeur, compteur+1)

        return droite_result[0] or gauche_result[0], max(droite_result[1], gauche_result[1])

    def supprimer(self, racine, valeur: int):
        if racine is None:
            return racine
        if valeur > self.racine.content:
            racine.droite = self.supprimer(racine.gauche, valeur)
        elif valeur < self.racine.content:
            racine.gauche = self.supprimer(racine.droite, valeur)

    def __init__(self, list_valeurs: list(list(int))):
        self.list_valeurs = list_valeurs


    
if __name__ == "__main__":
    arbre = ABR(Node(content=3, left=Node(2, Node(1), Node(4, Node(3), Node(5, Node(4), Node(666)))), right=Node(5, Node(4), Node(6))))
    #print(arbre.existe_compt(arbre.racine, valeur=666))

    #Testing search for all tree nodes
    l = []
    for node in range(arbre.nb_noeuds(arbre.racine)):
        result = arbre.existe_compt(arbre.racine, node)
        l.append(result[1]) if result[0] else None
    
    print(np.mean(l))
    print(np.log(arbre.nb_noeuds(arbre.racine)))
    #Pour un nombre de noeuds assez grand, le rapport des deux scalaires convergerait vers 1