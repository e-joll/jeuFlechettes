"""
classe des jeux
"""

class Jeu:
    
    liste_joueurs = []
    dict_joueurs = {}
    nb_joueurs = 0
    
    def __init__(self, controller):
        self.cible = controller.frames_droite['Cible']
        self.partie_finie = False
        self.liste_joueurs = Jeu.liste_joueurs.copy()
        self.nb_joueurs = len(self.liste_joueurs)
    
    def decale_ordre_joueurs(self):
        Jeu.liste_joueurs = Jeu.liste_joueurs[1:Jeu.nb_joueurs] + Jeu.liste_joueurs[0:1]

    def decale_ordre_manche(self):
        self.liste_joueurs = self.liste_joueurs[1:self.nb_joueurs] + self.liste_joueurs[0:1]
        
    def conversion_score(self, tir):
        """
        tir : string (comme '12D')
        -------------------------------
        Returns tir en int (comme 24)
        """
        if tir[-1] in ('S','D','T'):
            nb = int(tir[0:-1])
            if tir[-1] == 'S':
                return nb
            elif tir[-1] == 'D':
                return nb*2
            else:
                return nb*3
        else:
            return int(tir)
    
    def zone_vers_tranche(self, zone):
        if zone == '0':
            return '0'
        else:
            return zone[0:-1]
    
    def zone_vers_sdt(self, zone):
        if zone == '0':
            return '0'
        else:
            return zone[-1]
        
    def zone_vers_123(self, zone):
        if zone == '0':
            return 0
        elif zone[-1] == 'S':
            return 1
        elif zone[-1] == 'D':
            return 2
        elif zone[-1] == 'T':
            return 3
                  
    def tranche_suivante(self, num_tranche):
        if int(num_tranche) == 20:
            return 25
        else:
            return int(num_tranche)+1
        
        
    def delier_cible_joueur(self, joueur):
        self.page.res1.unbind('<FocusOut>')
        self.page.res2.unbind('<FocusOut>')
        self.page.res3.unbind('<FocusOut>')  
        joueur.volee[1] = self.page.tir1.get()
        joueur.volee[2] = self.page.tir2.get()
        joueur.volee[3] = self.page.tir3.get()
        
    
        
    def joueur_suivant(self, joueur):
        indice_joueur = self.liste_joueurs.index(joueur)
        if indice_joueur == self.nb_joueurs - 1:
            return self.liste_joueurs[0]
        else:
            return self.liste_joueurs[indice_joueur + 1]
    
    def joueur_precedent(self, joueur):
        indice_joueur = self.liste_joueurs.index(joueur)
        if indice_joueur == 0:
            return self.liste_joueurs[self.nb_joueurs - 1]
        else:
            return self.liste_joueurs[indice_joueur - 1]
        
    def supprimer_joueur(self, joueur, liste):
        liste.append(joueur)
        self.liste_joueurs.remove(joueur)
        self.nb_joueurs -= 1
        
    def tour_fini(self):
        indice_joueur = self.liste_joueurs.index(self.joueur_moment)
        return indice_joueur == self.nb_joueurs - 1
    
    def tri_points_decroissant(self, liste_non_ordonnee, score='points'):
        def ordre_points(joueur):
            return joueur.score[score]
        liste = liste_non_ordonnee.copy()
        liste.sort(key=ordre_points, reverse=True)
        return liste

    def tri_points_croissant(self, liste_non_ordonnee):
        def ordre_points(joueur):
            return joueur.score['points']
        liste = liste_non_ordonnee.copy()
        liste.sort(key=ordre_points, reverse=False)
        return liste
    
    def nouveau_classement(self, liste_du_1er_au_dernier):
        """
        1er: 5pts, 2e: 3pts, 3e: 1pt
        """
        liste_du_1er_au_dernier[0].classement[1] += 1
        liste_du_1er_au_dernier[0].classement['points'] += 5
        
        if Jeu.nb_joueurs > 1:
            liste_du_1er_au_dernier[1].classement[2] += 1
            liste_du_1er_au_dernier[1].classement['points'] += 3
            if Jeu.nb_joueurs > 2:
                liste_du_1er_au_dernier[2].classement[3] += 1
                liste_du_1er_au_dernier[2].classement['points'] += 1





class Horloge(Jeu):
    
    def __init__(self, controller):
        Jeu.__init__(self, controller)
        self.page = controller.frames_gauche['PageHorloge']
        self.page.bloque_mauvaise_reponse('sdt')
        self.page.confirme.config(command = self.partie)
        self.cible.ajoute_zones('sdt', self.page.volee)

        self.init_partie()
        self.page.set_score_reference(1)
        self.page.set_nom_joueur_moment(self.joueur_moment)
        self.page.affichage_resultats()

        self.actualiser(self.joueur_moment, self.joueur_moment.get_score()['derniere_tranche_atteinte'])
        
    def choix_tranche_a_atteindre(self):
        print('choix tranche a atteindre')
    
    def init_partie(self):
        #self.score_a_atteindre = self.page.nb_points_depart.get()
        
        for joueur in self.liste_joueurs:
            joueur.set_score([('derniere_tranche_atteinte', 0), ('volee', 0)])
            joueur.volee_a_zero()

        
        self.joueurs_ayant_fini = []
        self.joueur_moment = self.liste_joueurs[0]
        
        """
        *****
        *
        *
        *
        *
        A FINIR
        *
        *
        *
        *
        *****
        """
        
    def verif_vers_25(self, tranche):
        if 21 <= tranche <= 24:
            return 25
        else:
            return tranche
        
    def actualiser(self, joueur, score_tour_precedent):
        self.page.tir1.set('0')
        self.page.tir2.set('0')
        self.page.tir3.set('0')
        self.page.score_reference.set(self.tranche_suivante(joueur.get_score()['derniere_tranche_atteinte']))
        score_aux = score_tour_precedent
        def lier(event):
            joueur.volee[1] = self.conversion_score(self.page.tir1.get())
            joueur.volee[2] = self.conversion_score(self.page.tir2.get())
            joueur.volee[3] = self.conversion_score(self.page.tir3.get())
            #joueur.score['volee'] = joueur.volee[1] + joueur.volee[2] + joueur.volee[3]

            if int(self.zone_vers_tranche(self.page.tir1.get())) == self.tranche_suivante(score_tour_precedent):
                score_aux1 = self.verif_vers_25(score_aux + self.zone_vers_123(self.page.tir1.get()))
                joueur.get_score()['derniere_tranche_atteinte'] = score_aux1
                print('score_aux1 ', score_aux1)
                if int(self.zone_vers_tranche(self.page.tir2.get())) == self.tranche_suivante(score_aux1):
                    score_aux2 = self.verif_vers_25(score_aux1 + self.zone_vers_123(self.page.tir2.get()))
                    joueur.get_score()['derniere_tranche_atteinte'] = score_aux2
                    print('score_aux2 ', score_aux2)
                    if int(self.zone_vers_tranche(self.page.tir3.get())) == self.tranche_suivante(score_aux2):
                        score_aux3 = self.verif_vers_25(score_aux2 + self.zone_vers_123(self.page.tir3.get()))
                        joueur.get_score()['derniere_tranche_atteinte'] = score_aux3
                        print('score_aux3 ', score_aux3)
                elif int(self.zone_vers_tranche(self.page.tir3.get())) == self.tranche_suivante(score_aux1):
                    score_aux2 = self.verif_vers_25(score_aux1 + self.zone_vers_123(self.page.tir3.get()))
                    joueur.get_score()['derniere_tranche_atteinte'] = score_aux2
                    print('score_aux2 ', score_aux2)
            elif int(self.zone_vers_tranche(self.page.tir2.get())) == self.tranche_suivante(score_tour_precedent):
                score_aux1 = self.verif_vers_25(score_aux + self.zone_vers_123(self.page.tir2.get()))
                joueur.get_score()['derniere_tranche_atteinte'] = score_aux1
                print('score_aux1 ', score_aux1)
                if int(self.zone_vers_tranche(self.page.tir3.get())) == self.tranche_suivante(score_aux1):
                    score_aux2 = self.verif_vers_25(score_aux1 + self.zone_vers_123(self.page.tir3.get()))
                    joueur.get_score()['derniere_tranche_atteinte'] = score_aux2
                    print('score_aux2 ', score_aux2)
            elif int(self.zone_vers_tranche(self.page.tir3.get())) == self.tranche_suivante(score_tour_precedent):
                score_aux1 = self.verif_vers_25(score_aux + self.zone_vers_123(self.page.tir3.get()))
                joueur.get_score()['derniere_tranche_atteinte'] = score_aux1
                print('score_aux1 ', score_aux1)
            else:
                joueur.get_score()['derniere_tranche_atteinte'] = score_aux
                
            self.tranche_a_atteindre_moment = self.tranche_suivante(joueur.get_score()['derniere_tranche_atteinte'])
            self.page.score_reference.set(self.tranche_a_atteindre_moment)
            print(joueur.volee, joueur.score['derniere_tranche_atteinte'])
            print('Tranche a atteindre: ', self.tranche_a_atteindre_moment)
        self.page.res1.bind('<FocusOut>', lier)
        self.page.res2.bind('<FocusOut>', lier)
        self.page.res3.bind('<FocusOut>', lier)        
    
    def partie(self):
        self.delier_cible_joueur(self.joueur_moment)
        print(self.joueur_moment.get_nom())
        #affiche le score du joueur
        self.page.resultats_joueurs[Jeu.liste_joueurs.index(self.joueur_moment)][1].\
            config(text=self.joueur_moment.score['derniere_tranche_atteinte'])
            
        joueur_suivant = self.joueur_suivant(self.joueur_moment)
        tour_fini = self.tour_fini()
        
        if self.joueur_moment.score['derniere_tranche_atteinte'] >= 25:
            print('SUPPRESSION de ', self.joueur_moment.get_nom())
            self.supprimer_joueur(self.joueur_moment, self.joueurs_ayant_fini)
        
        
        if len(self.joueurs_ayant_fini) != Jeu.nb_joueurs:
            self.joueur_moment = joueur_suivant
            classement = self.tri_points_decroissant(self.liste_joueurs + self.joueurs_ayant_fini,
                                                     'derniere_tranche_atteinte')
            self.page.mise_a_jour_classement(classement)
            self.page.nom_joueur_moment.set(self.joueur_moment.get_nom())       
            self.page.res1.focus_set()
            self.actualiser(self.joueur_moment, self.joueur_moment.score['derniere_tranche_atteinte'])
        else:    
            self.partie_finie = True        
            self.cible.supprime_zones()
            self.page.premier(Jeu.liste_joueurs.index(self.joueurs_ayant_fini[0]))
            self.page.deuxieme(Jeu.liste_joueurs.index(self.joueurs_ayant_fini[1]))
            self.page.troisieme(Jeu.liste_joueurs.index(self.joueurs_ayant_fini[2]))
            self.nouveau_classement(self.joueurs_ayant_fini)
            self.decale_ordre_joueurs()
            

        
        




"""class Egalite(Jeu):
    
    def __init__(self, controller, jeu):
        Jeu.__init__(self, controller)
        self.page = controller.frames_gauche['PageEgalite']
        self.page.bloque_mauvaise_reponse('sdt')
        self.page.confirme.config(command = self.partie)
        self.cible.ajoute_zones('sdt', self.page.volee)

        self.init_partie()
        self.page.set_score_reference(self.score_a_atteindre)
        self.page.set_nom_joueur_moment(self.joueur_moment)
        self.page.affichage_resultats()

        self.actualiser(self.joueur_moment, self.score_a_atteindre)

    
    def init_partie(self):
        self.liste_joueurs = Jeu.liste_joueurs_a_egalite
        
        for joueur in self.liste_joueurs:
            joueur.set_score([('points', 0)])
            joueur.volee_a_zero()

        self.joueurs_a_egalite = []
        self.liste_rangee = []
        self.joueur_moment = self.liste_joueurs[0]

    def actualiser(self, joueur, score_tour_precedent):
        self.page.tir1.set('0')
        self.page.tir2.set('0')
        self.page.tir3.set('0')
        self.page.score_reference.set(score_tour_precedent)
        def lier(event):
            joueur.volee[1] = self.conversion_score(self.page.tir1.get())
            joueur.volee[2] = self.conversion_score(self.page.tir2.get())
            joueur.volee[3] = self.conversion_score(self.page.tir3.get())
            joueur.score['points'] += joueur.volee[1] + joueur.volee[2] + joueur.volee[3]
            self.page.score_reference.set(joueur.get_score()['points'])
            print(joueur.volee, joueur.score['volee'])
        self.page.res1.bind('<FocusOut>', lier)
        self.page.res2.bind('<FocusOut>', lier)
        self.page.res3.bind('<FocusOut>', lier)        
    
    def regroupement_par_egalite(self):
        joueurs_egaux = False
        for joueur in self.liste_rangee[1:]:
            joueur_precedent = self.joueur_precedent(joueur)
            if joueur.score['points'] == joueur_precedent.score['points']:
                if not(joueurs_egaux):
                    joueurs_egaux = True
                    indice = self.liste_rangee.index(joueur_precedent)
                    self.joueurs_a_egalite.append([indice])
                    self.joueurs_a_egalite[len(self.joueurs_a_egalite)-1].append(joueur_precedent)
                    self.joueurs_a_egalite[len(self.joueurs_a_egalite)-1].append(joueur)
                else:
                    self.joueurs_a_egalite[len(self.joueurs_a_egalite)-1].append(joueur)
            else:
                joueurs_egaux = False
    
    def partie(self):
        self.delier_cible_joueur(self.joueur_moment)
        print(self.joueur_moment.get_nom())
        
        indice_joueur = self.liste_joueurs.index(self.joueur_moment)

        #affiche le score du joueur
        self.page.resultats_joueurs[self.liste_joueurs.index(joueur_aux)][1].\
            config(text=self.joueur_moment.score['points'])
        
        
        if tour_fini:
            self.liste_rangee = self.tri_points_decroissant(self.liste_joueurs)
            self.regroupement_par_egalite()
            """ """
            if len(self.joueurs_a_egalite) == 0:
                #rien de plus
            else:
                #refaire pour departager
            """ """
            
            print('tour fini')
        
        self.joueur_moment = self.joueur_suivant(self.joueur_moment)
        
        if len(self.joueurs_ayant_fini) == Jeu.nb_joueurs:
            self.partie_finie = True
            self.cible.supprime_zones()
            self.joueurs_ayant_fini[0].ajoute_victoire()
            self.page.premier(Jeu.liste_joueurs.index(self.joueurs_ayant_fini[0]))
            self.page.deuxieme(Jeu.liste_joueurs.index(self.joueurs_ayant_fini[1]))
            self.page.troisieme(Jeu.liste_joueurs.index(self.joueurs_ayant_fini[2]))
            self.nouveau_classement(self.joueurs_ayant_fini)
            self.decale_ordre_joueurs()
        else:
            self.page.nom_joueur_moment.set(self.joueur_moment.get_nom())             
            self.page.res1.focus_set()
            self.actualiser(self.joueur_moment, self.joueur_moment.score['points'])"""



class ScoreAAtteindre(Jeu):
    
    def __init__(self, controller):
        Jeu.__init__(self, controller)
        self.page = controller.frames_gauche['PageAtteindre']
        self.page.bloque_mauvaise_reponse('sdt')
        self.page.confirme.config(command = self.partie)
        self.cible.ajoute_zones('sdt', self.page.volee)

        self.init_partie()
        self.page.set_score_reference(self.score_a_atteindre)
        self.page.set_nom_joueur_moment(self.joueur_moment)
        self.page.affichage_resultats()

        self.actualiser(self.joueur_moment, self.score_a_atteindre)
        
    def choix_score_a_atteindre(self):
        print('choix score a atteindre')
    
    def init_partie(self):
        self.score_a_atteindre = self.page.nb_points_depart.get()
        
        for joueur in self.liste_joueurs:
            joueur.set_score([('points', self.score_a_atteindre), ('volee', 0)])
            joueur.volee_a_zero()

        
        self.joueurs_ayant_fini = []
        self.joueur_moment = self.liste_joueurs[0]

    def actualiser(self, joueur, score_tour_precedent):
        self.page.tir1.set('0')
        self.page.tir2.set('0')
        self.page.tir3.set('0')
        self.page.score_reference.set(score_tour_precedent)
        def lier(event):
            joueur.volee[1] = self.conversion_score(self.page.tir1.get())
            joueur.volee[2] = self.conversion_score(self.page.tir2.get())
            joueur.volee[3] = self.conversion_score(self.page.tir3.get())
            joueur.score['volee'] = joueur.volee[1] + joueur.volee[2] + joueur.volee[3]
            self.score_a_atteindre_moment = score_tour_precedent - joueur.score['volee']
            self.page.score_reference.set(self.score_a_atteindre_moment)
            print(joueur.volee, joueur.score['volee'])
            print('Score a atteindre: ', self.score_a_atteindre_moment)
        self.page.res1.bind('<FocusOut>', lier)
        self.page.res2.bind('<FocusOut>', lier)
        self.page.res3.bind('<FocusOut>', lier)        
    
    def partie(self):
        self.delier_cible_joueur(self.joueur_moment)
        print(self.joueur_moment.get_nom())
        joueur_aux = self.joueur_moment
        tour_fini = self.tour_fini()
        
        self.joueur_moment = self.joueur_suivant(self.joueur_moment)
        
        if joueur_aux.score['points'] - joueur_aux.score['volee'] >= 0:
            joueur_aux.score['points'] -= joueur_aux.score['volee']
            if joueur_aux.score['points'] == 0:
                print('SUPPRIMER')
                self.supprimer_joueur(joueur_aux, self.joueurs_ayant_fini)
                print('joueurs ayant fini', self.joueurs_ayant_fini)
            
        #affiche le score du joueur
        self.page.resultats_joueurs[Jeu.liste_joueurs.index(joueur_aux)][1].\
            config(text=joueur_aux.score['points'])
        
        
        
        
        if tour_fini:
            classement = self.tri_points_croissant(self.liste_joueurs + self.joueurs_ayant_fini)
            self.page.mise_a_jour_classement(classement)
            print('tour fini')
        
        if len(self.joueurs_ayant_fini) == Jeu.nb_joueurs:
            self.partie_finie = True
            self.cible.supprime_zones()
            self.joueurs_ayant_fini[0].ajoute_victoire()
            self.page.premier(Jeu.liste_joueurs.index(self.joueurs_ayant_fini[0]))
            if Jeu.nb_joueurs >= 2:
                self.page.deuxieme(Jeu.liste_joueurs.index(self.joueurs_ayant_fini[1]))
            if Jeu.nb_joueurs >= 3:
                self.page.troisieme(Jeu.liste_joueurs.index(self.joueurs_ayant_fini[2]))
            self.nouveau_classement(self.joueurs_ayant_fini)
            self.decale_ordre_joueurs()
        else:
            self.page.nom_joueur_moment.set(self.joueur_moment.get_nom())             
            self.page.res1.focus_set()
            self.actualiser(self.joueur_moment, self.joueur_moment.score['points'])
         


        







class Scram(Jeu):
    
    def __init__(self, controller, plusOUplusEtMoins):
        Jeu.__init__(self, controller)
        print('                    JEU SCRAM:::::::', self)
        self.page = controller.frames_gauche['PageScram']
        self.page.confirme.config(command = self.partie)
        self.page.bloque_mauvaise_reponse('sdt')
        self.cible.ajoute_zones('sdt', self.page.volee)
        
        self.plusOUplusEtMoins = plusOUplusEtMoins
        self.init_partie()
        self.page.affichage_resultats()
        
        self.actualiser()

    def init_partie(self):
        for joueur in self.liste_joueurs:
            joueur.set_score([('nb_tranches_ouvertes', 21), ('tranches_fermees', []),\
                              ('points', 0), ('est_stoppeur', False)])
            joueur.volee_a_zero()

        self.joueur_moment = self.liste_joueurs[0]
        self.joueur_moment.set_score([('est_stoppeur', True)])
        self.stoppeur = self.joueur_moment
        self.page.set_nom_joueur_moment(self.joueur_moment)
        self.page.set_score_reference(self.joueur_moment.get_score()['nb_tranches_ouvertes'])
        
        
    def init_tirs_memoire(self):
        self.tirs_memoire = {'tir1': ['0'], 'tir2': ['0'], 'tir3': ['0'],
                             'memoire1': None, 'memoire2': None, 'memoire3': None,
                             'tranches_fermees_tour': []}

    
    def ajoute_memoire_stoppeur(self):
        self.init_tirs_memoire()
        def memoire(var, indx, mode,
                    tir1=self.page.tir1,
                    tir2=self.page.tir2,
                    tir3=self.page.tir3):
            if var == tir1.__str__() and tir1.get() != '':
                #print('memoire  avant', var, self.tirs_memoire[var])
                #print('mem1',tir1.get())
                self.tirs_memoire[var].append(self.zone_vers_tranche(tir1.get()))
                #print(self.tirs_memoire)
                #print('memoire  apres', var, self.tirs_memoire[var])
            elif var == tir2.__str__() and tir2.get() != '':
                #print('memoire  avant', var, self.tirs_memoire[var])
                #print('mem2',tir2.get())
                self.tirs_memoire[var].append(self.zone_vers_tranche(tir2.get()))
                #print(self.tirs_memoire)
                #print('memoire  apres', var, self.tirs_memoire[var])
            elif var == tir3.__str__() and tir3.get() != '':
                #print('memoire  avant', var, self.tirs_memoire[var])
                #print('mem3',tir3.get())
                self.tirs_memoire[var].append(self.zone_vers_tranche(tir3.get()))
                #print('memoire  apres', var, self.tirs_memoire[var])

        self.tirs_memoire['memoire1'] = self.page.tir1.trace_add('write', memoire)
        self.tirs_memoire['memoire2'] = self.page.tir2.trace_add('write', memoire)
        self.tirs_memoire['memoire3'] = self.page.tir3.trace_add('write', memoire)
    
    def supprime_memoire_stoppeur(self):
        self.page.tir1.trace_remove('write', self.tirs_memoire['memoire1'])
        self.page.tir2.trace_remove('write', self.tirs_memoire['memoire2'])
        self.page.tir3.trace_remove('write', self.tirs_memoire['memoire3'])
        """
        del(self.tirs_memoire['memoire1'])
        del(self.tirs_memoire['memoire1'])
        del(self.tirs_memoire['memoire1'])
        """


    
    def les_2_autres_tirs(self, tir_num):
        num = int(tir_num[-1])
        num1 = 1 + (num)%3
        num2 = 1 + (num+1)%3
        return ['tir'+str(num1), 'tir'+str(num2)]
        
        
    def actualiser(self):
        print('ACTUALISER')
        joueur = self.joueur_moment
        self.page.tir1.set('0')
        self.page.tir2.set('0')
        self.page.tir3.set('0')
        
        if joueur.score['est_stoppeur']:
            self.ajoute_memoire_stoppeur()
            def lier(event):
                """
                joueur.volee[1] = int(self.page.tir1.get()[0:-1])
                joueur.volee[2] = int(self.page.tir2.get()[0:-1])
                joueur.volee[3] = int(self.page.tir3.get()[0:-1])
                """
                tir_num = event.widget.cget('textvariable').__str__()
                tir = event.widget.get()[0:-1]
                print('        lier tir memoire[', tir_num,'] ', self.tirs_memoire[tir_num])
                print('XXXX ', self.tirs_memoire)
                if len(self.tirs_memoire[tir_num]) >= 2:
                    tir_memoire = self.tirs_memoire[tir_num][-2]
                else:
                    tir_memoire = self.tirs_memoire[tir_num][0]
                autres_tirs = [self.tirs_memoire[self.les_2_autres_tirs(tir_num)[0]][-1],
                              self.tirs_memoire[self.les_2_autres_tirs(tir_num)[1]][-1]]                  
                print('actualiser lier', tir_num, tir, self.tirs_memoire[tir_num])
                if tir_memoire != tir:
                    if tir_memoire != '0' and tir_memoire != autres_tirs[0] and tir_memoire != autres_tirs[1]\
                            and tir_memoire in self.tirs_memoire['tranches_fermees_tour']:
                        print('  =/= du precedent')
                        #on enleve la tranche self.tirs_memoire[tir_num][-2]
                        print('     remove le dernier:',tir_memoire)
                        joueur.score['tranches_fermees'].remove(tir_memoire)
                        self.tirs_memoire['tranches_fermees_tour'].remove(tir_memoire)
                        self.cible.supprime_tranche(self.tirs_memoire[tir_num][-2])
                        self.joueur_moment.score['nb_tranches_ouvertes'] += 1

                    if not(tir in self.stoppeur.score['tranches_fermees']) and tir != '':
                        print('     ajoute le nouveau:',tir)
                        joueur.score['tranches_fermees'].append(tir)
                        self.tirs_memoire['tranches_fermees_tour'].append(tir)
                        self.cible.ajoute_tranche(tir)
                        self.joueur_moment.score['nb_tranches_ouvertes'] -= 1
                print('NOUVEAU TRANCHES FERMEES', self.joueur_moment.score['nb_tranches_ouvertes'],
                      self.stoppeur.score['tranches_fermees'], '\n')

                self.page.score_reference.set(self.joueur_moment.score['nb_tranches_ouvertes'])
        else:
            points_aux = joueur.score['points']
            def lier(event):
                print(self.plusOUplusEtMoins)
                for (num, tir) in [(1, self.page.tir1.get()), (2, self.page.tir2.get()), (3, self.page.tir3.get())]:
                    if tir[0:-1] in self.stoppeur.score['tranches_fermees']:
                        if self.plusOUplusEtMoins == 'plus':
                            joueur.volee[num]  = 0
                        elif self.plusOUplusEtMoins == 'plusEtMoins':
                            joueur.volee[num]  = -self.conversion_score(tir)
                    else:
                        joueur.volee[num]  = self.conversion_score(tir)
                """
                joueur.volee[1] = self.conversion_score(self.page.tir1.get())
                joueur.volee[2] = self.conversion_score(self.page.tir2.get())
                joueur.volee[3] = self.conversion_score(self.page.tir3.get())
                """
                joueur.score['points'] = points_aux + joueur.volee[1] + joueur.volee[2] + joueur.volee[3]
                print(joueur.volee, joueur.score['points'])
                self.page.score_reference.set(self.joueur_moment.score['points'])
        self.page.res1.bind('<FocusOut>', lier)
        self.page.res2.bind('<FocusOut>', lier)
        self.page.res3.bind('<FocusOut>', lier)
        
    def partie(self):
        print('\n\n\nPARTIE')
        print('Nom      ',self.joueur_moment.get_nom())
        self.delier_cible_joueur(self.joueur_moment)
        
        if self.joueur_moment.score['est_stoppeur']:
            self.supprime_memoire_stoppeur()
            if self.joueur_moment.score['nb_tranches_ouvertes'] == 0:
                self.joueur_moment.score['est_stoppeur'] = False
                self.cible.supprime_toutes_les_tranches()
                if self.joueur_moment != self.liste_joueurs[-1]:
                    self.page.image_stoppeur(self.joueur_suivant(self.joueur_moment))
                    self.joueur_suivant(self.joueur_moment).score['est_stoppeur'] = True
                    self.stoppeur = self.joueur_suivant(self.joueur_moment)
                else:
                    self.partie_finie = True
                    self.cible.supprime_zones()
                    self.liste_joueurs = self.tri_points_decroissant(self.liste_joueurs)
                    self.liste_joueurs[0].ajoute_victoire()
                    self.page.premier(Jeu.liste_joueurs.index(self.liste_joueurs[0]))
                    self.page.deuxieme(Jeu.liste_joueurs.index(self.liste_joueurs[1]))
                    if self.nb_joueurs > 2:
                        self.page.troisieme(Jeu.liste_joueurs.index(self.liste_joueurs[2]))
                    self.nouveau_classement(self.liste_joueurs)
        
        #affiche le score du joueur
        self.page.resultats_joueurs[Jeu.liste_joueurs.index(self.joueur_moment)][1].\
            config(text=self.joueur_moment.score['points'])
        
        if self.tour_fini():
            classement = self.tri_points_croissant(self.liste_joueurs)
            """self.page.mise_a_jour_classement(classement)"""
            print('tour fini')
            
        if not(self.partie_finie):
            self.joueur_moment = self.joueur_suivant(self.joueur_moment)
            self.page.set_nom_joueur_moment(self.joueur_moment)
            #self.page.nom_joueur_moment.set(self.joueur_moment.get_nom())
            if not(self.joueur_moment.score['est_stoppeur']):
                self.init_tirs_memoire()
                self.page.set_score_reference((self.joueur_moment.score['points']))
                #self.page.score_reference.set(self.joueur_moment.score['points'])
            else:
                self.page.set_score_reference((self.joueur_moment.score['nb_tranches_ouvertes']))
            self.page.res1.focus_set()
            self.actualiser()
        

                    
        
        
        
        
class Legs(Jeu):
    
    def __init__(self, controller):
        Jeu.__init__(self, controller)
        self.page = controller.frames_gauche['PageLegs']
        self.page.bloque_mauvaise_reponse('sdt')
        self.page.confirme.config(command = self.partie)
        self.cible.ajoute_zones('sdt', self.page.volee)
        
        self.init_partie()
        self.page.nom_joueur_moment.set(self.joueur_moment.get_nom())
        self.page.affichage_resultats()

        self.actualiser(self.joueur_moment, 0)
        
        
    
    def init_partie(self):
        for joueur in self.liste_joueurs:
            joueur.set_score([('vies', 3), ('volee', 0)])
            joueur.volee_a_zero()

        self.score_a_battre = 0
        self.joueurs_elimines = []
        self.joueur_moment = self.liste_joueurs[0]

    def actualiser(self, joueur, score_a_battre):
        self.page.tir1.set('0')
        self.page.tir2.set('0')
        self.page.tir3.set('0')
        self.page.score_reference.set(score_a_battre)
        def lier(event):
            joueur.volee[1] = self.conversion_score(self.page.tir1.get())
            joueur.volee[2] = self.conversion_score(self.page.tir2.get())
            joueur.volee[3] = self.conversion_score(self.page.tir3.get())
            joueur.score['volee'] = joueur.volee[1] + joueur.volee[2] + joueur.volee[3]
            self.score_a_battre_moment = score_a_battre - joueur.score['volee']
            self.page.score_reference.set(self.score_a_battre_moment)
            print(joueur.volee, joueur.score['volee'])
            print('Score a battre: ', self.score_a_battre)
        self.page.res1.bind('<FocusOut>', lier)
        self.page.res2.bind('<FocusOut>', lier)
        self.page.res3.bind('<FocusOut>', lier)
    
    def partie(self):
        self.delier_cible_joueur(self.joueur_moment)
        #affiche le score du joueur
        self.page.resultats_joueurs[Jeu.liste_joueurs.index(self.joueur_moment)][5].\
            config(text=self.joueur_moment.score['volee'])
        
        joueur_aux = self.joueur_moment
        indice_joueur_aux = self.liste_joueurs.index(joueur_aux)
        tour_fini = self.tour_fini()
        self.joueur_moment = self.joueur_suivant(self.joueur_moment)
        
        if indice_joueur_aux == 0:
            self.score_a_battre = joueur_aux.score['volee']
        else:
            if self.score_a_battre >= joueur_aux.score['volee']:
                joueur_aux.score['vies'] -= 1
                self.page.enleve_vie(Jeu.liste_joueurs.index(joueur_aux))
                if joueur_aux.score['vies'] == 0:
                    print('suppression joueur', joueur_aux.get_nom())
                    self.page.mort(Jeu.liste_joueurs.index(joueur_aux))
                    self.supprimer_joueur(joueur_aux, self.joueurs_elimines)
                    print('joueurs elimines', self.joueurs_elimines)
            else:
                print('Nouveau Record')
                self.score_a_battre = joueur_aux.score['volee']


        if tour_fini:
            print('---tour fini---')
            self.score_a_battre = 0
            self.decale_ordre_manche()
            self.joueur_moment = self.liste_joueurs[0]
            self.page.image_joueur_ref(self.joueur_moment)
            self.page.image_joueur(self.liste_joueurs[-1])
            for j in range(Jeu.nb_joueurs):
                self.page.resultats_joueurs[j][5].config(text=0)


        self.page.nom_joueur_moment.set(self.joueur_moment.get_nom())
        print(self.joueur_moment.get_nom())

        self.page.res1.focus_set()
        self.actualiser(self.joueur_moment, self.score_a_battre)
        
        if len(self.joueurs_elimines) == Jeu.nb_joueurs - 1:
            print('PARTIE FINIE')
            self.liste_joueurs[0].ajoute_victoire()
            self.page.premier(Jeu.liste_joueurs.index(self.liste_joueurs[0]))
            self.partie_finie = True
            self.nouveau_classement(self.liste_joueurs+self.joueurs_elimines[::-1])
            self.cible.supprime_zones()
            self.decale_ordre_joueurs()
