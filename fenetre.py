"""
Classe de la fenetre du jeu
"""


import tkinter
from cible import *
from joueur import *
from jeux import *


font_aide = ('Kristen ITC',15)
font_joueur = ('Kristen ITC',15)
font_titre = ('Kristen ITC',23)

class Fenetre:

    def __init__(self):
        self.y = 840
        self.x = 2*self.y
        
        self.root = tkinter.Tk()
        self.root.title("Jeu de fléchettes")
        self.root.configure(background='white')
        self.root.geometry(str(self.x)+'x'+str(self.y))

        self.root.columnconfigure(0, minsize=self.y/2, weight=1)
        self.root.columnconfigure(1, minsize=self.y/2, weight=1)
        self.root.rowconfigure(0, minsize=self.y, weight=1)
        

        self.bordcontenantGauche = tkinter.Frame(self.root, background='green', bd=3,\
                                                 width = self.y, height = self.y)
        self.bordcontenantGauche.grid(row=0, column=0, sticky='n'+'s'+'e'+'w')
        self.bordcontenantGauche.grid_columnconfigure(0, weight=1)
        self.bordcontenantGauche.grid_rowconfigure(0, weight=1)
        
        self.contenantGauche = tkinter.Frame(self.bordcontenantGauche, background='white')
        self.contenantGauche.grid(row=0, column=0, sticky='n'+'s'+'e'+'w')
        self.contenantGauche.grid_columnconfigure(0, weight=1)
        self.contenantGauche.grid_rowconfigure(0, weight=1)
        
        self.bordcontenantDroit = tkinter.Frame(self.root, background='red', bd=3,\
                                             width = self.y, height = self.y)
        

        self.bordcontenantDroit.grid(row=0, column=1, sticky='n'+'s'+'e'+'w')
        self.bordcontenantDroit.grid_columnconfigure(0, weight=1)
        self.bordcontenantDroit.grid_rowconfigure(0, weight=1)
        
        self.contenantDroit = tkinter.Frame(self.bordcontenantDroit, background='white')
        self.contenantDroit.grid(row=0, column=0, sticky='n'+'s'+'e'+'w')
        self.contenantDroit.grid_columnconfigure(0, weight=1)
        self.contenantDroit.grid_rowconfigure(0, weight=1)
        
        
        
        self.frames_gauche = {}
        for F in (PageJoueur, PageChoixDuJeu, PageClassement,\
                  PageHorloge,
                  PageLegs, PageScram, PageAtteindre):
            page_name = F.__name__
            frame = F(self.contenantGauche, controller = self)
            self.frames_gauche[page_name] = frame
            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
            
            
        self.frames_droite = {}
        for F in (Cible, PageJoueur, PageChoixDuJeu):
            page_name = F.__name__
            frame = F(self.contenantDroit, controller = self)
            self.frames_droite[page_name] = frame
            # put all of the pages in the same location;
            # the one on the top of the stacking order
            # will be the one that is visible.
        
        for nom_du_jeu in ('Atteindre', 'Horloge', 'Cricket', 'Legs','Scram'):
            frame = PageInfo(self.contenantDroit, nom_du_jeu, controller = self)
            page_name = frame.__name__()
            self.frames_droite[page_name] = frame

        self.show_frame_gauche("PageJoueur")
        self.show_frame_droite("Cible")
        

        

    def show_frame_gauche(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames_gauche[page_name]
        frame.contenant.tkraise()
        
    def show_frame_droite(self, page_name):
        '''Show a frame for the given page name'''
        frame = self.frames_droite[page_name]
        frame.contenant.tkraise()
        

        self.root.update()
        self.root.mainloop()
    


    
class Page:

    def __init__(self, frame, nom_page, controller):
        
        self.controller = controller

        self.contenant = tkinter.Frame(frame, background='white')
        self.contenant.grid(row=0, column=0, sticky='nsew')
        self.contenant.grid_columnconfigure(0, weight=1)
        self.contenant.grid_rowconfigure(0, weight=1)
        
        self.haut = tkinter.Frame(self.contenant, bg='white', cursor='circle')
        self.haut.pack(fill=tkinter.BOTH)
        titre = tkinter.Label(self.haut, text=nom_page, bg='white',
                              font=font_titre, fg='grey')
        titre.pack()

        self.bas = tkinter.Frame(self.contenant,bg='white', cursor='man')
        self.bas.pack(expand=True, fill=tkinter.BOTH)
        
        self.contenant_bas = tkinter.Frame(self.bas, cursor = 'cross', bg='white')
        self.contenant_bas.place(relwidth=0.90, relheight=0.88, relx=0.5, rely=0.46, anchor='center')
        
        self.contenant_boutons = tkinter.Frame(self.bas, cursor = 'cross', bg='white')
        self.contenant_boutons.place(relwidth=0.85, relheight=0.1, relx=0.5, rely=0.95, anchor='center')
        self.contenant_boutons.columnconfigure(0,weight=1)
        self.contenant_boutons.columnconfigure(1,weight=1)
        

        self.img_or = tkinter.PhotoImage(file="img/modele_medal_or.png")
        self.img_argent = tkinter.PhotoImage(file="img/modele_medal_argent.png")
        self.img_bronze = tkinter.PhotoImage(file="img/modele_medal_bronze.png")




class PageClassement(Page):

    def __init__(self, frame, controller):
        Page.__init__(self, frame, 'Classement', controller)
        self.contenant_resultats = tkinter.Frame(self.contenant_bas, bg='white')
        self.contenant_resultats.place(relx=0.5, rely=0.57, anchor='center')
        self.contenant_resultats.columnconfigure(0,weight=1)
        self.contenant_resultats.columnconfigure(1,weight=1)
        self.contenant_resultats.columnconfigure(2,weight=1)
        self.contenant_resultats.columnconfigure(3,weight=1)
        self.contenant_resultats.columnconfigure(4,weight=1)
        
        self.img_user = tkinter.PhotoImage(file="img/modele_user.png")
        
        self.img_arrow_left = tkinter.PhotoImage(file="img/modele_arrow_left.png")
        self.bouton_fermer = tkinter.Button(self.contenant_boutons, relief='flat',
                                             bg='white', activebackground='white',
                                             image=self.img_arrow_left,
                                             command=self.retour)
        #self.bouton_fermer.place(relx=0.5, rely=0.5, anchor='center')
        self.bouton_fermer.grid(columnspan=2)
        
        self.resultats_joueurs = [[]]
        self.resultats_joueurs[0].append(tkinter.Label(self.contenant_resultats,
                                     image=self.img_user,
                                     font = font_joueur, padx=10, bg='white'))
        self.resultats_joueurs[0].append(tkinter.Label(self.contenant_resultats,
                                     image=self.img_or,
                                     font = font_joueur, padx=10, bg='white',
                                     compound='left'))
        self.resultats_joueurs[0].append(tkinter.Label(self.contenant_resultats,
                                     image=self.img_argent,
                                     font = font_joueur, padx=10, bg='white',
                                     compound='left'))
        self.resultats_joueurs[0].append(tkinter.Label(self.contenant_resultats,
                                     image=self.img_bronze,
                                     font = font_joueur, padx=10, bg='white',
                                     compound='left'))
        self.resultats_joueurs[0].append(tkinter.Label(self.contenant_resultats,
                                     text='Points', font = font_joueur, padx=10, bg='white',
                                     compound='left'))    

        self.resultats_joueurs[0][0].grid(row=0, column=0, pady=10)
        self.resultats_joueurs[0][1].grid(row=0, column=1, padx=10)
        self.resultats_joueurs[0][2].grid(row=0, column=2, padx=10)
        self.resultats_joueurs[0][3].grid(row=0, column=3, padx=10)
        self.resultats_joueurs[0][4].grid(row=0, column=4)



    def classement(self):
        def ordre_points(joueur):
            return joueur.classement['points']
        liste = Jeu.liste_joueurs.copy()
        liste.sort(key=ordre_points, reverse=True)
        print('CLASSEMENT')
        for i in liste:
            print(i.classement['points'])
        
        num = 0
        for joueur in liste:
            num += 1
            self.j0 = []
            self.j0.append(tkinter.Label(self.contenant_resultats,
                                         text=joueur.get_nom(), font = font_joueur, padx=10, bg='white'))
            self.j0.append(tkinter.Label(self.contenant_resultats,
                                         text=joueur.classement[1], font = font_joueur, padx=10, bg='white',
                                         compound='left'))
            self.j0.append(tkinter.Label(self.contenant_resultats,
                                         text=joueur.classement[2], font = font_joueur, padx=10, bg='white',
                                         compound='left'))
            self.j0.append(tkinter.Label(self.contenant_resultats,
                                         text=joueur.classement[3], font = font_joueur, padx=10, bg='white',
                                         compound='left'))
            self.j0.append(tkinter.Label(self.contenant_resultats,
                                         text=joueur.classement['points'], font = font_joueur, padx=10, bg='white',
                                         compound='left'))

            self.j0[0].grid(row=num, column=0)
            self.j0[1].grid(row=num, column=1, padx=45)
            self.j0[2].grid(row=num, column=2, padx=45)
            self.j0[3].grid(row=num, column=3, padx=45)
            self.j0[4].grid(row=num, column=4)

            self.resultats_joueurs.append(self.j0)
            

    def reset(self):
        for joueur in range(Jeu.nb_joueurs, 0, -1):
            for i in range(4, -1, -1):
                self.resultats_joueurs[joueur][i].destroy()
                del(self.resultats_joueurs[joueur][i])
            del(self.resultats_joueurs[joueur])
    
    def retour(self):
        self.reset()
        self.controller.show_frame_gauche("PageChoixDuJeu")
        
        
        
class PageJeu(Page):
    
    def __init__(self, frame, nom_page, controller):
        Page.__init__(self, frame, nom_page, controller)
        
        #### LIGNE 0 ####
        self.contenant_joueur_moment = tkinter.Frame(self.contenant_bas, bg='white')
        self.contenant_joueur_moment.place(relx=0.5, rely=0, relwidth=1, anchor='n')
        self.contenant_joueur_moment.columnconfigure(0,weight=2)
        self.contenant_joueur_moment.columnconfigure(1,weight=1)
        self.contenant_joueur_moment.columnconfigure(2,weight=1)
        
        
        #### COLONNE 0 ####
        self.nom_joueur_moment = tkinter.StringVar(name='nom_joueur_moment')
        self.score_reference = tkinter.IntVar(name='score_reference')
        self.img_user_clock = tkinter.PhotoImage(file="img/modele_user_clock.png")
        
        self.joueur_moment = tkinter.Label(self.contenant_joueur_moment, image = self.img_user_clock,
                                     textvariable=self.nom_joueur_moment, font = font_joueur, padx=10, bg='white',
                                     compound='left')       
        self.joueur_moment.grid(row=0, column=0, sticky='wsn')
        
        #### COLONNE 1 ####
        self.img_bullseye_arrow = tkinter.PhotoImage(file="img/modele_bullseye_arrow.png")
        
        self.score_moment = tkinter.Label(self.contenant_joueur_moment, image = self.img_bullseye_arrow,
                                     textvariable = self.score_reference, font = font_joueur, padx=10, bg='white',
                                     compound='left')
        self.score_moment.grid(row=0, column=1, sticky='ewsn')
        

        #### COLONNE 2 ####
        self.tir1=tkinter.StringVar(value=0, name='tir1')
        self.tir2=tkinter.StringVar(value=0, name='tir2')
        self.tir3=tkinter.StringVar(value=0, name='tir3')
        self.img_check = tkinter.PhotoImage(file="img/modele_check.png")
        
        self.volee = tkinter.Frame(self.contenant_joueur_moment, bg='white')
        self.volee.grid(row=0, column=2, sticky='e')
        
        self.res1 = tkinter.Entry(self.volee,highlightcolor='red', highlightthickness=3,highlightbackground='green',
                                  textvariable=self.tir1, font=font_joueur, width=4, justify = 'center')
        self.res1.grid(row=0, column=0, padx=2)
        
        self.res2 = tkinter.Entry(self.volee,highlightcolor='red', highlightthickness=3,highlightbackground='green',
                                  textvariable=self.tir2, font=font_joueur, width=4, justify = 'center')
        self.res2.grid(row=0, column=1, padx=2)
        
        self.res3 = tkinter.Entry(self.volee,highlightcolor='red', highlightthickness=3,highlightbackground='green',
                                  textvariable=self.tir3, font=font_joueur, width=4, justify = 'center')
        self.res3.grid(row=0, column=2, padx=2)
        
        self.confirme = tkinter.Button(self.volee, image=self.img_check,
                                       relief='flat', bg='white', activebackground='white')
        self.confirme.grid(row=0, column=3, padx=2)
        
        
        self.contenant_resultats = tkinter.Frame(self.contenant_bas, bg='white')
        self.contenant_resultats.place(relx=0.5, rely=0.57, anchor='center')
        
    def set_score_reference(self, score_joueur):
        self.score_reference.set(score_joueur)
        
    def set_nom_joueur_moment(self, joueur):
        self.nom_joueur_moment.set(joueur.get_nom())
        
    def premier(self, num_joueur):
        self.resultats_joueurs[num_joueur][0].config(image=self.img_or)
        
    def deuxieme(self, num_joueur):
        self.resultats_joueurs[num_joueur][0].config(image=self.img_argent)

    def troisieme(self, num_joueur):
        self.resultats_joueurs[num_joueur][0].config(image=self.img_bronze)
    """
    def affichage_medailles(self, listePremierAuDernier):
        ### a finir
    """
    def bloque_mauvaise_reponse(self, sdtOUtranches):
        if sdtOUtranches == 'sdt':
            zones = ['', '0']+self.controller.frames_droite['Cible'].zones()
            def zoneValide(nouvelle_entree):
                if not(nouvelle_entree in zones):
                    return False
                return True
            
            OkayCommand = self.res1.register(zoneValide)
            
        elif sdtOUtranches == 'tranches':
            tranches = ['', '0']+self.controller.frames_droite['Cible'].tranches()
            def zoneValide(nouvelle_entree):
                if not(nouvelle_entree in tranches):
                    return False
                return True
            OkayCommand = self.register(zoneValide)
        
        self.res1.configure(validate='key', validatecommand=(OkayCommand,'%P'))
        self.res2.configure(validate='key', validatecommand=(OkayCommand,'%P'))
        self.res3.configure(validate='key', validatecommand=(OkayCommand,'%P'))
        

class PageEgalite(PageJeu):

    def __init__(self, frame, controller):
        PageJeu.__init__(self, frame, 'Score à atteindre', controller)
        self.contenant_resultats.columnconfigure(0,weight=1)
        self.contenant_resultats.columnconfigure(1,weight=1)
        
        self.img_user = tkinter.PhotoImage(file="img/modele_user.png")
        self.img_arrow_left = tkinter.PhotoImage(file="img/modele_arrow_left.png")
        self.nb_points_depart = tkinter.IntVar(value=150)
        
        
        self.bouton_fermer = tkinter.Button(self.contenant_boutons, relief='flat',
                                             bg='white', activebackground='white',
                                             image=self.img_arrow_left,
                                             command=self.retour)
        self.bouton_fermer.place(relx=0.5, rely=0.5, anchor='center')        
        
        self.resultats_joueurs = []    
    
    def affichage_resultats(self, liste_joueurs_a_egalite):
        if self.resultats_joueurs != []:
            self.reset()
            self.resultats_joueurs = []
        self.res1.focus_set()
        print('affichage egalite')
        print(Jeu.liste_joueurs, '   ', Jeu.dict_joueurs, '    ', len(Jeu.liste_joueurs))
        for num in range(len(liste_joueurs_a_egalite)):
            self.j0 = []
            self.j0.append(tkinter.Label(self.contenant_resultats, image = self.img_user,
                                         text=liste_joueurs_a_egalite[num].nom, font = font_joueur, padx=10, bg='white',
                                         compound='left'))
            self.j0.append(tkinter.Label(self.contenant_resultats,
                                         text=liste_joueurs_a_egalite.get_score()['volee'], font = font_joueur, padx=10, bg='white',
                                         compound='left'))
        
            self.j0[0].grid(row=num, column=0, sticky='wsn')
            self.j0[1].grid(row=num, column=1, padx=60)

            self.resultats_joueurs.append(self.j0)

    def reset(self):
        for joueur in range(len(Jeu.liste_joueurs)-1,-1,-1):
            for i in (1,0):
                self.resultats_joueurs[joueur][i].destroy()
                del(self.resultats_joueurs[joueur][i])
            del(self.resultats_joueurs[joueur]) 

    def retour(self):
        self.controller.show_frame_gauche("PageChoixDuJeu")
        self.controller.frames_droite['Cible'].supprime_toutes_les_tranches()
        self.controller.frames_droite['Cible'].supprime_zones()
        self.reset()
        
        
        
class PageHorloge(PageJeu):
    
    def __init__(self, frame, controller):
        PageJeu.__init__(self, frame, 'Horloge', controller)
        self.contenant_resultats.columnconfigure(0,weight=1)
        self.contenant_resultats.columnconfigure(1,weight=1)
        self.contenant_resultats.columnconfigure(2,weight=1)
        
        self.img_user = tkinter.PhotoImage(file="img/modele_user.png")
        self.img_arrow_left = tkinter.PhotoImage(file="img/modele_arrow_left.png")
        #self. = tkinter.IntVar(value=150)
        
        
        self.bouton_fermer = tkinter.Button(self.contenant_boutons, relief='flat',
                                             bg='white', activebackground='white',
                                             image=self.img_arrow_left,
                                             command=self.retour)
        self.bouton_fermer.place(relx=0.5, rely=0.5, anchor='center')        
        
        self.resultats_joueurs = []
        
    """
    def affichage_choix_score_depart(self):
        def jouer():
            self.reset_choix()
            ScoreAAtteindre(self.controller)
        
        self.points_depart = tkinter.Entry(self.contenant_resultats, 
                              textvariable=self.nb_points_depart, font=font_joueur,
                              width=4, justify = 'center', relief='solid')
        self.label_depart = tkinter.Label(self.contenant_resultats, bg='white',
                                     text='Nombre de points à atteindre:', font=font_joueur)
        self.bouton_valider = tkinter.Button(self.contenant_resultats, relief='flat',
                                             bg='white', image=self.img_check,
                                             command=jouer)
        self.label_depart.grid(row=0, column=2)
        self.points_depart.grid(row=1, column=2)
        self.bouton_valider.grid(row=2, column=2)

    def reset_choix(self):
        self.points_depart.destroy()
        self.label_depart.destroy()
        self.bouton_valider.destroy()
    """

    def affichage_resultats(self):
        if self.resultats_joueurs != []:
            self.reset()
            self.resultats_joueurs = []
        self.res1.focus_set()
        print('affichage horloge')
        print(Jeu.liste_joueurs, '   ', Jeu.dict_joueurs, '    ', len(Jeu.liste_joueurs))
        for num in range(len(Jeu.liste_joueurs)):
            self.j0 = []
            self.j0.append(tkinter.Label(self.contenant_resultats, image = self.img_user,
                                         text=Jeu.liste_joueurs[num].nom, font = font_joueur, padx=10, bg='white',
                                         compound='left'))
            self.j0.append(tkinter.Label(self.contenant_resultats,
                                         text=Jeu.liste_joueurs[num].get_score()['derniere_tranche_atteinte'],
                                         font = font_joueur, padx=10, bg='white',
                                         compound='left'))
            self.j0.append(tkinter.Label(self.contenant_resultats, text = 'Classement',
                                          font = font_joueur, bg='white'))
        
            self.j0[0].grid(row=num, column=0, sticky='wsn')
            self.j0[1].grid(row=num, column=1, padx=60)
            self.j0[2].grid(row=num, column=2, sticky='esn')

            self.resultats_joueurs.append(self.j0)

    def reset(self):
        for joueur in range(len(Jeu.liste_joueurs)-1,-1,-1):
            for i in (2,1,0):
                self.resultats_joueurs[joueur][i].destroy()
                del(self.resultats_joueurs[joueur][i])
            del(self.resultats_joueurs[joueur]) 

    
    def mise_a_jour_classement(self, classement):
        place = 1
        for joueur in classement:
            num = Jeu.liste_joueurs.index(joueur)
            self.resultats_joueurs[num][2].config(text=place)
            place += 1
    
    def retour(self):
        self.controller.show_frame_gauche("PageChoixDuJeu")
        self.controller.frames_droite['Cible'].supprime_toutes_les_tranches()
        self.controller.frames_droite['Cible'].supprime_zones()
        self.reset()
        #del(self.controller.frames_gauche["PageChoixDuJeu"].jeu_en_cours)
            
            

class PageAtteindre(PageJeu):
    
    def __init__(self, frame, controller):
        PageJeu.__init__(self, frame, 'Score à atteindre', controller)
        self.contenant_resultats.columnconfigure(0,weight=1)
        self.contenant_resultats.columnconfigure(1,weight=1)
        self.contenant_resultats.columnconfigure(2,weight=1)
        
        self.img_user = tkinter.PhotoImage(file="img/modele_user.png")
        self.img_arrow_left = tkinter.PhotoImage(file="img/modele_arrow_left.png")
        self.nb_points_depart = tkinter.IntVar(value=150)
        
        
        self.bouton_fermer = tkinter.Button(self.contenant_boutons, relief='flat',
                                             bg='white', activebackground='white',
                                             image=self.img_arrow_left,
                                             command=self.retour)
        self.bouton_fermer.place(relx=0.5, rely=0.5, anchor='center')        
        
        self.resultats_joueurs = []
        
        
    def affichage_choix_score_depart(self):
        def jouer():
            self.reset_choix()
            self.jeu_en_cours = ScoreAAtteindre(self.controller)
        
        self.points_depart = tkinter.Entry(self.contenant_resultats, 
                              textvariable=self.nb_points_depart, font=font_joueur,
                              width=4, justify = 'center', relief='solid')
        self.label_depart = tkinter.Label(self.contenant_resultats, bg='white',
                                     text='Nombre de points à atteindre:', font=font_joueur)
        self.bouton_valider = tkinter.Button(self.contenant_resultats, relief='flat',
                                             bg='white', image=self.img_check,
                                             command=jouer)
        self.label_depart.grid(row=0, column=2)
        self.points_depart.grid(row=1, column=2)
        self.bouton_valider.grid(row=2, column=2)

    def reset_choix(self):
        self.points_depart.destroy()
        self.label_depart.destroy()
        self.bouton_valider.destroy()

    def affichage_resultats(self):
        if self.resultats_joueurs != []:
            self.reset()
            self.resultats_joueurs = []
        self.res1.focus_set()
        print('affichage scram')
        print(Jeu.liste_joueurs, '   ', Jeu.dict_joueurs, '    ', len(Jeu.liste_joueurs))
        for num in range(len(Jeu.liste_joueurs)):
            self.j0 = []
            self.j0.append(tkinter.Label(self.contenant_resultats, image = self.img_user,
                                         text=Jeu.liste_joueurs[num].nom, font = font_joueur, padx=10, bg='white',
                                         compound='left'))
            self.j0.append(tkinter.Label(self.contenant_resultats,
                                         text=Jeu.liste_joueurs[num].get_score()['points'], font = font_joueur, padx=10, bg='white',
                                         compound='left'))
            self.j0.append(tkinter.Label(self.contenant_resultats, text = 'Classement',
                                          font = font_joueur, bg='white'))
        
            self.j0[0].grid(row=num, column=0, sticky='wsn')
            self.j0[1].grid(row=num, column=1, padx=60)
            self.j0[2].grid(row=num, column=2, sticky='esn')

            self.resultats_joueurs.append(self.j0)

    def reset(self):
        for joueur in range(len(Jeu.liste_joueurs)-1,-1,-1):
            for i in (2,1,0):
                self.resultats_joueurs[joueur][i].destroy()
                del(self.resultats_joueurs[joueur][i])
            del(self.resultats_joueurs[joueur]) 

    
    def mise_a_jour_classement(self, classement):
        place = 1
        for joueur in classement:
            num = Jeu.liste_joueurs.index(joueur)
            self.resultats_joueurs[num][2].config(text=place)
            place += 1
    
    def retour(self):
        self.controller.show_frame_gauche("PageChoixDuJeu")
        self.controller.frames_droite['Cible'].supprime_toutes_les_tranches()
        self.controller.frames_droite['Cible'].supprime_zones()
        self.reset()
        del(self.jeu_en_cours)






class PageScram(PageJeu):
    
    def __init__(self, frame, controller):
        PageJeu.__init__(self, frame, 'Scram', controller)
        self.contenant_resultats.columnconfigure(0,weight=1)
        self.contenant_resultats.columnconfigure(1,weight=1)
        self.contenant_resultats.columnconfigure(2,weight=1)
        
        self.img_user = tkinter.PhotoImage(file="img/modele_user.png")
        self.img_stoppeur = tkinter.PhotoImage(file="img/modele_user_shield.png")
        
        
        self.img_arrow_left = tkinter.PhotoImage(file="img/modele_arrow_left.png")
        self.bouton_fermer = tkinter.Button(self.contenant_boutons, relief='flat',
                                             bg='white', activebackground='white',
                                             image=self.img_arrow_left,
                                             command=self.retour)
        self.bouton_fermer.place(relx=0.5, rely=0.5, anchor='center')
        
        self.resultats_joueurs = []
       
        
    def affichage_choix(self):
        def jouer1():
            self.reset_choix()
            self.jeu_en_cours = Scram(self.controller, 'plus')
        def jouer2():
            self.reset_choix()
            self.jeu_en_cours = Scram(self.controller, 'plusEtMoins')
        
        self.bouton_option1 = tkinter.Button(self.contenant_resultats, relief='flat',
                                               overrelief='solid', bg='white',
                                               activebackground='white',
                                               text='Que des +', font=('Kristen ITC',15),
                                               command=jouer1)
        self.bouton_option2 = tkinter.Button(self.contenant_resultats, relief='flat',
                                               overrelief='solid', bg='white',
                                               activebackground='white',
                                               text='Des + et des -', font=('Kristen ITC',15),
                                               command=jouer2)        
        
        self.bouton_option1.grid(row=0, column=2)
        self.bouton_option2.grid(row=1, column=2)

    def reset_choix(self):
        self.bouton_option1.destroy()
        self.bouton_option2.destroy()      


    def affichage_resultats(self):
        self.res1.focus_set()
        print('affichage scram')
        print(Jeu.liste_joueurs, '   ', Jeu.dict_joueurs, '    ', len(Jeu.liste_joueurs))
        for num in range(len(Jeu.liste_joueurs)):
            self.j0 = []
            self.j0.append(tkinter.Label(self.contenant_resultats, image = self.img_user,
                                         text=Jeu.liste_joueurs[num].nom, font = font_joueur, padx=10, bg='white',
                                         compound='left'))
            self.j0.append(tkinter.Label(self.contenant_resultats,
                                         text=Jeu.liste_joueurs[num].get_score()['points'], font = font_joueur, padx=10, bg='white',
                                         compound='left'))
            self.j0.append(tkinter.Label(self.contenant_resultats, text = 'Classement 1e',
                                          font = font_joueur, bg='white'))
        
            self.j0[0].grid(row=num, column=0, sticky='wsn')
            self.j0[1].grid(row=num, column=1, padx=60)
            self.j0[2].grid(row=num, column=2, sticky='esn')

            self.resultats_joueurs.append(self.j0)
            
        self.resultats_joueurs[0][0].config(image=self.img_stoppeur)

    def reset(self):
        for joueur in range(len(Jeu.liste_joueurs)-1,-1,-1):
            for i in (2,1,0):
                self.resultats_joueurs[joueur][i].destroy()
                del(self.resultats_joueurs[joueur][i])
            del(self.resultats_joueurs[joueur])
    
    def image_stoppeur(self, joueur):
        num_joueur = Jeu.liste_joueurs.index(joueur)
        self.resultats_joueurs[num_joueur - 1][0].config(image=self.img_user)
        self.resultats_joueurs[num_joueur][0].config(image=self.img_stoppeur)

    def retour(self):
        self.controller.show_frame_gauche("PageChoixDuJeu")
        self.controller.frames_droite['Cible'].supprime_toutes_les_tranches()
        self.controller.frames_droite['Cible'].supprime_zones()
        self.reset()
        del(self.jeu_en_cours)
                
                
                
                
        
class PageLegs(PageJeu):
    
    def __init__(self, frame, controller):
        PageJeu.__init__(self, frame, 'Legs', controller)
        self.contenant_resultats.columnconfigure(0,weight=1)
        self.contenant_resultats.columnconfigure(1,weight=1)
        self.contenant_resultats.columnconfigure(2,weight=1)
        
        self.img_user = tkinter.PhotoImage(file="img/modele_user.png")
        self.img_user2 = tkinter.PhotoImage(file="img/modele_user2.png")
        self.img_skull_crossbones = tkinter.PhotoImage(file="img/modele_skull_crossbones.png")
        self.img_heartbeat = tkinter.PhotoImage(file="img/modele_heartbeat.png")
        self.img_vide = tkinter.PhotoImage(file="img/modele_heartbeat_transparent.png")
        
        self.img_arrow_left = tkinter.PhotoImage(file="img/modele_arrow_left.png")
        self.bouton_fermer = tkinter.Button(self.contenant_boutons, relief='flat',
                                             bg='white', activebackground='white',
                                             image=self.img_arrow_left,
                                             command=lambda: self.controller.show_frame_gauche("PageChoixDuJeu"))
        self.bouton_fermer.place(relx=0.5, rely=0.5, anchor='center')
        
        self.resultats_joueurs = []
        
        

        
    def affichage_resultats(self):
        if self.resultats_joueurs != []:
            self.reset()
            self.resultats_joueurs = []
        self.res1.focus_set()
        print('affichage')
        #print(Jeu.liste_joueurs, '   ', Jeu.dict_joueurs, '    ', len(Jeu.liste_joueurs))
        for num in range(len(Jeu.liste_joueurs)):
            self.j0 = []
            self.j0.append(tkinter.Label(self.contenant_resultats, image = self.img_user,
                                         text=Jeu.liste_joueurs[num].nom, font = font_joueur, padx=10, bg='white',
                                         compound='left'))
            self.j0.append(tkinter.Frame(self.contenant_resultats, bg='white'))
            self.j0.append(tkinter.Label(self.j0[1], image = self.img_heartbeat,
                                         bg='white'))
            self.j0.append(tkinter.Label(self.j0[1], image = self.img_heartbeat,
                                         bg='white'))
            self.j0.append(tkinter.Label(self.j0[1], image = self.img_heartbeat,
                                         bg='white'))
            self.j0.append(tkinter.Label(self.contenant_resultats, text = Jeu.liste_joueurs[num].get_score()['volee'],
                                          font = font_joueur, bg='white'))    
        
            self.j0[0].grid(row=num, column=0, sticky='wsn')
            self.j0[1].grid(row=num, column=1, padx=60)
            self.j0[2].grid(row=num, column=0, padx=2)
            self.j0[3].grid(row=num, column=1, padx=2)
            self.j0[4].grid(row=num, column=2, padx=2)
            self.j0[5].grid(row=num, column=2, sticky='esn')
            
            self.resultats_joueurs.append(self.j0)
        
        self.resultats_joueurs[0][0].config(image=self.img_user2)

    def reset(self):
        for joueur in range(len(Jeu.liste_joueurs)-1,-1,-1):
            for i in (5,1,0):
                self.resultats_joueurs[joueur][i].destroy()        
                del(self.resultats_joueurs[joueur][i])
            del(self.resultats_joueurs[joueur])
            
    def enleve_vie(self, num_joueur):
        joueur = Jeu.liste_joueurs[num_joueur]
        nb_vie_restante = joueur.score['vies']
        self.resultats_joueurs[num_joueur][nb_vie_restante + 2].config(image=self.img_vide)
        
    def mort(self, num_joueur):
        joueur = Jeu.liste_joueurs[num_joueur]
        self.resultats_joueurs[num_joueur][0].config(image=self.img_skull_crossbones)
        
    def image_joueur_ref(self, joueur):
        num_joueur = Jeu.liste_joueurs.index(joueur)
        self.resultats_joueurs[num_joueur][0].config(image=self.img_user2)
    
    def image_joueur(self, joueur):
        num_joueur = Jeu.liste_joueurs.index(joueur)
        self.resultats_joueurs[num_joueur][0].config(image=self.img_user)        
    
    def retour(self):
        self.controller.show_frame_gauche("PageChoixDuJeu")
        self.controller.frames_droite['Cible'].supprime_toutes_les_tranches()
        self.controller.frames_droite['Cible'].supprime_zones()
        self.reset()        
        
        
        
        

class PageJoueur(Page):
    
    def __init__(self, frame, controller):
        Page.__init__(self, frame, 'Joueurs', controller)
        self.contenant_bas.columnconfigure(0,weight=1)
        self.contenant_bas.columnconfigure(1,weight=1)

        self.img_user_plus = tkinter.PhotoImage(file="img/modele_user_plus.png")
        self.img_user_minus = tkinter.PhotoImage(file="img/modele_user_minus.png")

        
        self.nom_joueur0 = tkinter.StringVar()
        self.image0 = tkinter.Label(self.contenant_bas, image=self.img_user_plus, bg='white', cursor='plus')
        self.image0.grid(row=0, column=0, pady=1,sticky='e')
        self.entre_joueur0 = tkinter.Entry(self.contenant_bas, font=font_joueur, 
                                           relief='solid',textvariable = self.nom_joueur0)
        self.entre_joueur0.grid(row=0, column=1, padx=20, sticky='w')
        
        
        self.nom_joueur1 = tkinter.StringVar()
        self.image1 = tkinter.Label(self.contenant_bas, image=self.img_user_plus, bg='white', cursor='plus')
        self.image1.grid(row=1, column=0, pady=1,sticky='e')
        self.entre_joueur1 = tkinter.Entry(self.contenant_bas, font=font_joueur, 
                                           relief='solid',textvariable = self.nom_joueur1)
        self.entre_joueur1.grid(row=1, column=1, padx=20, sticky='w')
        
        
        self.nom_joueur2 = tkinter.StringVar()
        self.image2 = tkinter.Label(self.contenant_bas, image=self.img_user_plus, bg='white', cursor='plus')
        self.image2.grid(row=2, column=0, pady=1,sticky='e')
        self.entre_joueur2 = tkinter.Entry(self.contenant_bas, font=font_joueur, 
                                           relief='solid',textvariable = self.nom_joueur2)
        self.entre_joueur2.grid(row=2, column=1, padx=20, sticky='w')
        

        self.nom_joueur3 = tkinter.StringVar()
        self.image3 = tkinter.Label(self.contenant_bas, image=self.img_user_plus, bg='white', cursor='plus')
        self.image3.grid(row=3, column=0, pady=1,sticky='e')
        self.entre_joueur3 = tkinter.Entry(self.contenant_bas, font=font_joueur, 
                                           relief='solid',textvariable = self.nom_joueur3)
        self.entre_joueur3.grid(row=3, column=1, padx=20, sticky='w')
        
        
        self.nom_joueur4 = tkinter.StringVar()
        self.image4 = tkinter.Label(self.contenant_bas, image=self.img_user_plus, bg='white', cursor='plus')
        self.image4.grid(row=4, column=0, pady=1,sticky='e')
        self.entre_joueur4 = tkinter.Entry(self.contenant_bas, font=font_joueur, 
                                           relief='solid',textvariable = self.nom_joueur4)
        self.entre_joueur4.grid(row=4, column=1, padx=20, sticky='w')
        
        
        self.nom_joueur5 = tkinter.StringVar()
        self.image5 = tkinter.Label(self.contenant_bas, image=self.img_user_plus, bg='white', cursor='plus')
        self.image5.grid(row=5, column=0, pady=1,sticky='e')
        self.entre_joueur5 = tkinter.Entry(self.contenant_bas, font=font_joueur, 
                                           relief='solid',textvariable = self.nom_joueur5)
        self.entre_joueur5.grid(row=5, column=1, padx=20, sticky='w')
        

        self.nom_joueur6 = tkinter.StringVar()
        self.image6 = tkinter.Label(self.contenant_bas, image=self.img_user_plus, bg='white', cursor='plus')
        self.image6.grid(row=6, column=0, pady=1,sticky='e')
        self.entre_joueur6 = tkinter.Entry(self.contenant_bas, font=font_joueur, 
                                           relief='solid',textvariable = self.nom_joueur6)
        self.entre_joueur6.grid(row=6, column=1, padx=20, sticky='w')
        

        self.nom_joueur7 = tkinter.StringVar()
        self.image7 = tkinter.Label(self.contenant_bas, image=self.img_user_plus, bg='white', cursor='plus')
        self.image7.grid(row=7, column=0, pady=1,sticky='e')
        self.entre_joueur7 = tkinter.Entry(self.contenant_bas, font=font_joueur, 
                                           relief='solid',textvariable = self.nom_joueur7)
        self.entre_joueur7.grid(row=7, column=1, padx=20, sticky='w')
        

        self.nom_joueur8 = tkinter.StringVar()
        self.image8 = tkinter.Label(self.contenant_bas, image=self.img_user_plus, bg='white', cursor='plus')
        self.image8.grid(row=8, column=0, pady=1,sticky='e')
        self.entre_joueur8 = tkinter.Entry(self.contenant_bas, font=font_joueur, 
                                           relief='solid',textvariable = self.nom_joueur8)
        self.entre_joueur8.grid(row=8, column=1, padx=20, sticky='w')  
    
    
        self.liste_nom_joueurs = [self.nom_joueur0,
                                  self.nom_joueur1,
                                  self.nom_joueur2,
                                  self.nom_joueur3,
                                  self.nom_joueur4,
                                  self.nom_joueur5,
                                  self.nom_joueur6,
                                  self.nom_joueur7,
                                  self.nom_joueur8]      
        self.liste_joueurs = []
        self.dict_joueurs = []
        
        def creer_liste_joueurs(liste_nom_joueurs = self.liste_nom_joueurs):
            liste_joueurs = []
            for nom in liste_nom_joueurs:
                if nom.get() != '':
                    liste_joueurs.append(Joueur(nom.get()))
            return liste_joueurs

        def creer_dict_joueurs(liste_nom_joueurs = self.liste_nom_joueurs):
            dict_joueurs = {}
            for nom in liste_nom_joueurs:
                if nom.get() != '':
                    dict_joueurs[nom.get()] = Joueur(nom.get())
            return dict_joueurs
        
        def jouer():
            controller.show_frame_gauche("PageChoixDuJeu")
            self.liste_joueurs = creer_liste_joueurs()
            self.dict_joueurs = creer_dict_joueurs()
            Jeu.liste_joueurs = self.liste_joueurs
            Jeu.dict_joueurs = self.dict_joueurs
            Jeu.nb_joueurs = len(self.liste_joueurs)
            #print(self.liste_joueurs)

    
        self.gamepad = tkinter.PhotoImage(file="img/modele_gamepad.png")
        self.bouton_valider = tkinter.Button(self.contenant_boutons, relief='flat',
                                             bg='white', image=self.gamepad,
                                             command=jouer)
        self.bouton_valider.place(relx=0.5, rely=0.5, anchor='center')
        



class PageChoixDuJeu(Page):
           
    def __init__(self, frame, controller):
        Page.__init__(self, frame, 'Choix du jeu', controller)
        
        self.contenant_noms_jeux = tkinter.Frame(self.contenant_bas, bg='white')
        self.contenant_noms_jeux.place(relx=0.5, rely=0.5, anchor='center')
        self.contenant_noms_jeux.columnconfigure(0,weight=1)
        self.contenant_noms_jeux.columnconfigure(1,weight=1)
        
        self.img_info_circle = tkinter.PhotoImage(file="img/modele_info_circle.png")
        
        #SCORE A ATTEINDRE
        self.bouton_atteindre = tkinter.Button(self.contenant_noms_jeux, relief='flat',
                                               overrelief='solid', bg='white',
                                               activebackground='white',
                                               text='Score à atteindre', font=('Kristen ITC',15),
                                               command=self.lancer_atteindre)
        self.bouton_atteindre.grid(row=0, column=0, padx=20, sticky='e')
        self.image_atteindre = tkinter.Button(self.contenant_noms_jeux, relief='flat',
                                         image=self.img_info_circle, 
                                         bg='white', activebackground='white',
                                         cursor='question_arrow',
                                         command=self.info_atteindre)
        self.image_atteindre.grid(row=0, column=1, pady=1,sticky='w')
        
            
        #HORLOGE
        self.bouton_horloge = tkinter.Button(self.contenant_noms_jeux, relief='flat', 
                                             overrelief='solid', bg='white',
                                             activebackground='white',
                                             text='Horloge', font=('Kristen ITC',15),
                                             command=self.lancer_horloge)
        self.bouton_horloge.grid(row=1, column=0, padx=20, sticky='e')
        self.image_horloge = tkinter.Button(self.contenant_noms_jeux, relief='flat',
                                         image=self.img_info_circle, 
                                         bg='white', activebackground='white',
                                         cursor='question_arrow',
                                         command=self.info_horloge)
        self.image_horloge.grid(row=1, column=1, pady=1,sticky='w')
        
            
        #CRICKET
        self.bouton_cricket = tkinter.Button(self.contenant_noms_jeux, relief='flat', 
                                             overrelief='solid', bg='white',
                                             activebackground='white',
                                             text='Cricket', font=('Kristen ITC',15),
                                             command=self.lancer_cricket)
        self.bouton_cricket.grid(row=2, column=0, padx=20, sticky='e')
        self.image_cricket = tkinter.Button(self.contenant_noms_jeux, relief='flat',
                                         image=self.img_info_circle, 
                                         bg='white', activebackground='white',
                                         cursor='question_arrow',
                                         command=self.info_cricket)
        self.image_cricket.grid(row=2, column=1, pady=1,sticky='w')
        

        #LEGS
        self.bouton_legs = tkinter.Button(self.contenant_noms_jeux, relief='flat', 
                                          overrelief='solid', bg='white',
                                          activebackground='white',
                                          text='Legs', font=('Kristen ITC',15),
                                          command=self.lancer_legs)
        self.bouton_legs.grid(row=3, column=0, padx=20, sticky='e')
        self.image_legs = tkinter.Button(self.contenant_noms_jeux, relief='flat',
                                         image=self.img_info_circle, 
                                         bg='white', activebackground='white',
                                         cursor='question_arrow',
                                         command=self.info_legs)
        self.image_legs.grid(row=3, column=1, pady=1,sticky='w')
        
        
        #SCRAM
        self.bouton_scram = tkinter.Button(self.contenant_noms_jeux, relief='flat', 
                                           overrelief='solid', bg='white',
                                           activebackground='white',
                                           text='Scram', font=('Kristen ITC',15),
                                           command=self.lancer_scram)
        self.bouton_scram.grid(row=4, column=0, padx=20, sticky='e')
        self.image_scram = tkinter.Button(self.contenant_noms_jeux, relief='flat',
                                         image=self.img_info_circle, 
                                         bg='white', activebackground='white',
                                         cursor='question_arrow',
                                         command=self.info_scram)
        self.image_scram.grid(row=4, column=1, pady=1,sticky='w')
        
        
        
        #RETOUR AUX NOMS DES JOUEURS
        self.user_edit = tkinter.PhotoImage(file="img/modele_user_edit.png")
        self.bouton_valider = tkinter.Button(self.contenant_boutons, relief='flat',
                                             bg='white', activebackground='white',
                                             image=self.user_edit,
                                             command=lambda: self.controller.show_frame_gauche("PageJoueur"))
        #self.bouton_valider.place(relx=0.5, rely=0.5, anchor='center')
        self.bouton_valider.grid(row=0, column=0, ipadx=20, sticky='ens')
        
        #CLASSEMENT
        self.trophee = tkinter.PhotoImage(file="img/modele_trophy.png")
        self.bouton_classement = tkinter.Button(self.contenant_boutons, relief='flat',
                                             bg='white', activebackground='white',
                                             image=self.trophee,
                                             command=self.nouveau_classement)
        #self.bouton_classement.place(relx=0.8, rely=0.5, anchor='center')        
        self.bouton_classement.grid(row=0, column=1, ipadx=20, sticky='wns')
    
    #SCORE A ATTEINDRE
    def lancer_atteindre(self):
        print('Lancer atteindre')
        self.controller.show_frame_gauche('PageAtteindre')
        self.controller.frames_gauche['PageAtteindre'].affichage_choix_score_depart()
        
    def info_atteindre(self):
        self.controller.show_frame_droite("PageInfoAtteindre")
        print('Info atteindre')
    
    #HORLOGE
    def lancer_horloge(self):
        print('Lancer horloge')
        self.controller.show_frame_gauche('PageHorloge')
        self.jeu_en_cours = Horloge(self.controller)
    
    def info_horloge(self):
        self.controller.show_frame_droite("PageInfoHorloge")
        print('Info horloge')
        
    #CRICKET
    def lancer_cricket(self):
        print('Lancer cricket')
        
    def info_cricket(self):
        self.controller.show_frame_droite("PageInfoCricket")
        print('Info cricket')
    
    #LEGS
    def lancer_legs(self):
        print('Lancer legs')
        self.controller.show_frame_gauche('PageLegs')
        self.jeu_en_cours = Legs(self.controller)
        
        
    def info_legs(self):
        self.controller.show_frame_droite("PageInfoLegs")
        print('Info legs')
    
    #SCRAM
    def lancer_scram(self):
        print('Lancer scram')
        self.controller.show_frame_gauche('PageScram')
        self.controller.frames_gauche['PageScram'].affichage_choix()
        #self.jeu_en_cours = Scram(self.controller)

        
    def info_scram(self):
         self.controller.show_frame_droite("PageInfoScram")
         print('Info scram') 
         
    #CLASSEMENT
    def nouveau_classement(self):
        self.controller.frames_gauche['PageClassement'].classement()
        self.controller.show_frame_gauche('PageClassement')



class PageInfo(Page):
    
    def __init__(self, frame, nom_du_jeu, controller):
        Page.__init__(self, frame, nom_du_jeu, controller)
        
        self.close = tkinter.PhotoImage(file="img/modele_close.png")
        self.bouton_valider = tkinter.Button(self.contenant_boutons, relief='flat',
                                             bg='white', image=self.close,
                                             command=lambda: self.controller.show_frame_droite("Cible"))
        self.bouton_valider.place(relx=0.5, rely=0.5, anchor='center')
        self.nom_du_jeu = nom_du_jeu
        if nom_du_jeu == 'Scram':
            self.regles_scram()
            
    def __name__(self):
        return 'PageInfo'+self.nom_du_jeu
        
    def regles_scram(self):
        self.regles = tkinter.Label(self.contenant_bas, justify='left', \
                                    font=font_aide, bg='white',
                                    width =736, wraplength=690, text="\
Le jeu se déroule en 2 manches.\n\
A la première manche, un des deux joueurs est stoppeur et l'autre est \
marqueur. A la deuxième manche, les rôles sont inversés.\
En début de partie, tous les secteurs sont ouverts.\n\
LE STOPPEUR:\n\
    Il commence en premier à chaque tour.\n\
    Son but est de fermer tous les secteurs pour empêcher le marqueur de marquer des points. \n\
LE MARQUEUR:\n\
    Il commence en deuxième à chaque tour.\n\
    Son but est de faire le plus de points possibles: il marque des points seulement en touchant des secteurs ouverts.\n\
\n")
        self.regles.place(relx=0.5, rely=0.5, anchor='center')





        
"""   
def test():
    r=tkinter.Tk()
    r.title('Cible')
    r.geometry('800x800')
    can = tkinter.Canvas(r)
    can.pack(expand=1, fill=tkinter.BOTH)
    c=Cible(can)
    r.update()
    a=input('a1')
    c.colorer_tranche(int(a))
    a=input('a2')
    c.colorer_tranche(int(a))
    a=input('a3')
    c.colorer_tranche(int(a))
    a=input('a4')
    c.colorer_tranche(int(a))
    input('top')
    c.reset()
    r.mainloop()
"""

#Fenetre()

