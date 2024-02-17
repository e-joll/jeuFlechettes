"""
classe de joueur
"""

class Joueur:
    
    def __init__(self, nom):
        self.nom = nom
        self.volee = {1: 0, 2: 0, 3: 0}
        self.score = {}
        self.nb_victoire = 0
        self.classement = {1: 0, 2: 0, 3: 0, 'points': 0}
        
    def get_nom(self):
        return self.nom
    
    def get_score(self):
        return self.score
    
    def set_score(self, parametres):
        for p in parametres:
            self.score[p[0]] = p[1]
    
    def volee_a_zero(self):
        for num in self.volee.keys():
            self.volee[num] = 0

    def nb_flechettes_lancees_a_zero(self):
        self.nb_flechettes_lancees = 0
    
    def ajoute_victoire(self):
        self.nb_victoire += 1

"""
def ordre_points(joueur):
    return joueur.score['points']
        
L=[Joueur('Charles'),Joueur('Jules'),Joueur('Martha'),Joueur('Aurélie')]
L[0].set_score([('nb_tranches_ouvertes', 21), ('tranches_fermees', [1,3]),\
                  ('points', 14), ('est_stoppeur', False)])
L[1].set_score([('nb_tranches_ouvertes', 1), ('tranches_fermees', [9,18,20]),\
                  ('points', 256), ('est_stoppeur', False)])
L[2].set_score([('nb_tranches_ouvertes', 21), ('tranches_fermees', []),\
                  ('points', 78), ('est_stoppeur', False)])
L[3].set_score([('nb_tranches_ouvertes', 2), ('tranches_fermees', []),\
                  ('points', 120), ('est_stoppeur', True)])

for i in range(4):
    print(L[i].nom)
print(L)
L.sort(key=ordre_points, reverse=True)
for i in range(4):
    print(L[i].nom)
print(L)
"""

def test():
    j0 = Joueur('Alexis')
    j1 = Joueur('Marianne')
    liste = [j0, j1]
    jeu = Legs(liste)
    j0.nb_flechettes_lancees_a_zero()
    #j1.score_a_zero()
