"""
Classe de la cible de flechettes
"""
import tkinter
import turtle
from math import *

   
    
class Cible:
    
    ordre = [(13,0), (4,1), (18,2), (1,3), (20,4), (5,5,), (12,6), (9,7), (14,8),\
             (11,9), (8,10), (16,11), (7,12), (19,13), (3,14), (17,15), (2,16),\
             (15,17), (10,18), (6,19)]
    num_tranches = list(range(1,21))+[25]
    
    x = 830
    w = 5
    bord_double_ext = 718 - (x/2)
    bord_double_int = bord_double_ext - 18
    bord_double_int1 = bord_double_ext - 19
    bord_triple_ext = 602 - (x/2)
    bord_triple_int = bord_triple_ext - 18
    bord_triple_int1 = bord_triple_ext - 19
    bord_rond25 = 446 - (x/2)
    bord_rond50 = 428 - (x/2)
    
    r_rond25 = 14
    r_rond50 = 30
    r = 300
    
    def __init__(self, frame, controller):
        self.contenant = tkinter.Frame(frame, background='white')
        self.contenant.grid(row=0, column=0, sticky='nsew')
        self.contenant.grid_columnconfigure(0, weight=1)
        self.contenant.grid_rowconfigure(0, weight=1)
        
        self.cible = tkinter.Canvas(master=self.contenant, width=Cible.x, height=Cible.x, cursor='plus', bg='white')
        self.img=tkinter.PhotoImage(file="cible/img/cible_image2_830.png")
        self.cible.create_image(Cible.x/2, Cible.x/2, image=self.img)
        self.cible.place(height=Cible.x, width=Cible.x, relx=0.5, rely=0.5,anchor='center')
        #self.cible.grid()
        #self.ajoute_zones('sdt',controller.frames_gauche['PageLegs'].volee)
        #self.supprime_zones()

        self.tranches = self.init_dict_tranches()

    def init_dict_tranches(self):
        dict_tranches = {}
        for num in Cible.num_tranches:
            path = "cible/img/tranche"+str(num)+".png"
            dict_tranches[str(num)] = {'img': tkinter.PhotoImage(file=path), 'id': None}
        return dict_tranches
    
    def get_num_tranches(self):
        return Cible.num_tranches
    
    def tranches(self):
        liste_tranches = ['25S']
        for tranche in range(1,21):
            liste_tranches.append(str(tranche))
        return liste_tranches        
    
    def zones(self):
        liste_zones = ['25S', '25D']
        for tranche in range(1,21):
            for sdt in ('S','D','T'):
                liste_zones.append(str(tranche)+sdt)
        return liste_zones
    
    
    
    def ajoute_zones(self,sdtOUtranches, frame_volee):
        
        def affiche(event, frame=frame_volee):
            zone = self.cible.find_closest(event.x,event.y)[0]
            frame.focus_get().delete(0, len(frame.focus_get().get()))
            frame.focus_get().insert(0,self.cible.gettags(zone)[0])
            frame.focus_get().tk_focusNext().focus_set()
            print(self.cible.gettags(zone)[0])
        
        def calcul_x(angle, rayon):
            return cos(radians(angle))*rayon + Cible.x/2

        def calcul_y(angle,rayon):
            return -sin(radians(angle))*rayon + Cible.x/2
    
    
        carre = self.cible.create_polygon([(2,2),(827,2),(827,827),(2,827)], 
                                     fill ='',
                                     activewidth=Cible.w, activeoutline='red', activedash =(3,3),
                                     tags=('0', 'zone'))
        
        self.cible.tag_bind(carre,'<Button-1>',affiche)
        
        if sdtOUtranches == 'sdt':
            for i,j in Cible.ordre:
                a=9+18*j
                c=a+18
                n=(a+c)/2
        
        
                points_double = [(calcul_x(a+0.5, Cible.bord_double_int),calcul_y(a+0.5,Cible.bord_double_int)), 
                                  (calcul_x(a+0.5, Cible.bord_double_int),calcul_y(a+0.5,Cible.bord_double_int)), 
                                  (calcul_x(a+0.5, Cible.r),calcul_y(a+0.5,Cible.r)),
                                  (calcul_x(a+0.5, Cible.r),calcul_y(a+0.5,Cible.r)),
                                  (calcul_x(a+0.5 - 2, Cible.r),calcul_y(a+0.5 - 2,Cible.r)),
                                  (calcul_x(n, Cible.r),calcul_y(n, Cible.r)),
                                  (calcul_x(c + 2, Cible.r),calcul_y(c + 2,Cible.r)),
                                  (calcul_x(c, Cible.r),calcul_y(c,Cible.r)),
                                  (calcul_x(c, Cible.r),calcul_y(c,Cible.r)),
                                  (calcul_x(c, Cible.bord_double_int),calcul_y(c,Cible.bord_double_int)),
                                  (calcul_x(c, Cible.bord_double_int),calcul_y(c,Cible.bord_double_int)),
                                  (calcul_x(n, Cible.bord_double_int),calcul_y(n, Cible.bord_double_int))]
                double = self.cible.create_polygon(points_double, smooth = 1, splinesteps =50,
                                                 fill='', joinstyle='bevel',
                                                 activewidth=Cible.w, activeoutline='white', activedash =(3,3),
                                                 tags=(str(i)+'D','zone'))
                
                points_simplee = [(calcul_x(a+0.5, Cible.bord_double_int1),calcul_y(a+0.5,Cible.bord_double_int1)), 
                                  (calcul_x(a+0.5, Cible.bord_double_int1),calcul_y(a+0.5,Cible.bord_double_int1)), 
                                  (calcul_x(a+0.5, Cible.bord_triple_ext),calcul_y(a+0.5,Cible.bord_triple_ext)),
                                  (calcul_x(a+0.5, Cible.bord_triple_ext),calcul_y(a+0.5,Cible.bord_triple_ext)),
                                  (calcul_x(a+0.5 - 2, Cible.bord_triple_ext),calcul_y(a+0.5 - 2,Cible.bord_triple_ext)),
                                  (calcul_x(n, Cible.bord_triple_ext),calcul_y(n, Cible.bord_triple_ext)),
                                  (calcul_x(c + 2, Cible.bord_triple_ext),calcul_y(c + 2,Cible.bord_triple_ext)),
                                  (calcul_x(c, Cible.bord_triple_ext),calcul_y(c,Cible.bord_triple_ext)),
                                  (calcul_x(c, Cible.bord_triple_ext),calcul_y(c,Cible.bord_triple_ext)),
                                  (calcul_x(c, Cible.bord_double_int1),calcul_y(c,Cible.bord_double_int1)),
                                  (calcul_x(c, Cible.bord_double_int1),calcul_y(c,Cible.bord_double_int1)),
                                  (calcul_x(n, Cible.bord_double_int1),calcul_y(n, Cible.bord_double_int1))]
                simple_ext = self.cible.create_polygon(points_simplee, smooth = 1, splinesteps =50,
                                                 fill='',
                                                 activewidth=Cible.w, activeoutline='white', activedash =(3,3),
                                                 tags=(str(i)+'S','zone'))
        
                points_triple = [(calcul_x(a+0.5, Cible.bord_triple_int),calcul_y(a+0.5,Cible.bord_triple_int)), 
                                  (calcul_x(a+0.5, Cible.bord_triple_int),calcul_y(a+0.5,Cible.bord_triple_int)), 
                                  (calcul_x(a+0.5, Cible.bord_triple_ext),calcul_y(a+0.5,Cible.bord_triple_ext)),
                                  (calcul_x(a+0.5, Cible.bord_triple_ext),calcul_y(a+0.5,Cible.bord_triple_ext)),
                                  (calcul_x(a+0.5 - 2, Cible.bord_triple_ext),calcul_y(a+0.5 - 2,Cible.bord_triple_ext)),
                                  (calcul_x(n, Cible.bord_triple_ext),calcul_y(n, Cible.bord_triple_ext)),
                                  (calcul_x(c + 2, Cible.bord_triple_ext),calcul_y(c + 2,Cible.bord_triple_ext)),
                                  (calcul_x(c, Cible.bord_triple_ext),calcul_y(c,Cible.bord_triple_ext)),
                                  (calcul_x(c, Cible.bord_triple_ext),calcul_y(c,Cible.bord_triple_ext)),
                                  (calcul_x(c, Cible.bord_triple_int),calcul_y(c,Cible.bord_triple_int)),
                                  (calcul_x(c, Cible.bord_triple_int),calcul_y(c,Cible.bord_triple_int)),
                                  (calcul_x(n, Cible.bord_triple_int),calcul_y(n, Cible.bord_triple_int))]
                triple = self.cible.create_polygon(points_triple, smooth = 1, splinesteps =50,
                                                 fill='',
                                                 activewidth=Cible.w, activeoutline='white', activedash =(3,3),
                                                 tags=(str(i)+'T','zone'))
                
                points_simplei = [(calcul_x(a+0.5, Cible.bord_triple_int1),calcul_y(a+0.5,Cible.bord_triple_int1)), 
                                  (calcul_x(a+0.5, Cible.bord_triple_int1),calcul_y(a+0.5,Cible.bord_triple_int1)), 
                                  (calcul_x(a+0.5, Cible.bord_rond25),calcul_y(a+0.5,Cible.bord_rond25)),
                                  (calcul_x(a+0.5, Cible.bord_rond25),calcul_y(a+0.5,Cible.bord_rond25)),
                                  (calcul_x(a+0.5 - 2, Cible.bord_rond25),calcul_y(a+0.5 - 2,Cible.bord_rond25)),
                                  (calcul_x(n, Cible.bord_rond25),calcul_y(n, Cible.bord_rond25)),
                                  (calcul_x(c + 2, Cible.bord_rond25),calcul_y(c + 2,Cible.bord_rond25)),
                                  (calcul_x(c, Cible.bord_rond25),calcul_y(c,Cible.bord_rond25)),
                                  (calcul_x(c, Cible.bord_rond25),calcul_y(c,Cible.bord_rond25)),
                                  (calcul_x(c, Cible.bord_triple_int1),calcul_y(c,Cible.bord_triple_int1)),
                                  (calcul_x(c, Cible.bord_triple_int1),calcul_y(c,Cible.bord_triple_int1)),
                                  (calcul_x(n, Cible.bord_triple_int1),calcul_y(n, Cible.bord_triple_int1))]
                simple_int = self.cible.create_polygon(points_simplei, smooth = 1, splinesteps =50,
                                                 fill='',
                                                 activewidth=Cible.w, activeoutline='white', activedash =(3,3),
                                                 tags=(str(i)+'S','zone'))
                
                self.cible.tag_bind(simple_int,'<Button-1>',affiche)
                self.cible.tag_bind(simple_ext,'<Button-1>',affiche)
                self.cible.tag_bind(double,'<Button-1>',affiche)
                self.cible.tag_bind(triple,'<Button-1>',affiche)
                
                #print(self.cible.gettags(simple_int)[0], type(self.cible.gettags(simple_int)[0]))
        
            points_tranche_rond25 =[]
            for i in range(8):
                a=45*i
                points_tranche_rond25.append((calcul_x(a, Cible.bord_rond25),calcul_y(a,Cible.bord_rond25)))
            rond25 = self.cible.create_polygon(points_tranche_rond25, smooth = 1, splinesteps =50,
                                          fill='',
                                          activewidth=Cible.w, activeoutline='white', activedash =(3,3),
                                          tags=('25S','zone'))
                
            points_tranche_rond50 =[]
            for i in range(20):
                a=18*i
                points_tranche_rond50.append((calcul_x(a, Cible.bord_rond50),calcul_y(a,Cible.bord_rond50)))
            rond50 = self.cible.create_polygon(points_tranche_rond50, smooth = 1, splinesteps =50,
                                          fill='',
                                          activewidth=Cible.w, activeoutline='white', activedash =(3,3),
                                          tags=('25D','zone'))
        
            
            self.cible.tag_bind(rond25,'<Button-1>',affiche)
            self.cible.tag_bind(rond50,'<Button-1>',affiche)
        
        elif sdtOUtranches == 'tranches':
            for i,j in Cible.ordre:
                a=9+18*j
                c=a+18
                n=(a+c)/2
        
        
                points_tranche = [(calcul_x(a+0.5, Cible.r),calcul_y(a+0.5,Cible.r)), 
                                  (calcul_x(a+0.5, Cible.r),calcul_y(a+0.5,Cible.r)), 
                                  (calcul_x(a+0.5, Cible.bord_rond25),calcul_y(a+0.5,Cible.bord_rond25)),
                                  (calcul_x(a+0.5, Cible.bord_rond25),calcul_y(a+0.5,Cible.bord_rond25)),
                                  (calcul_x(a+0.5 - 2, Cible.bord_rond25),calcul_y(a+0.5 - 2,Cible.bord_rond25)),
                                  (calcul_x(n, Cible.bord_rond25),calcul_y(n, Cible.bord_rond25)),
                                  (calcul_x(c + 2, Cible.bord_rond25),calcul_y(c + 2,Cible.bord_rond25)),
                                  (calcul_x(c, Cible.bord_rond25),calcul_y(c,Cible.bord_rond25)),
                                  (calcul_x(c, Cible.bord_rond25),calcul_y(c,Cible.bord_rond25)),
                                  (calcul_x(c, Cible.r),calcul_y(c,Cible.r)),
                                  (calcul_x(c, Cible.r),calcul_y(c,Cible.r)),
                                  (calcul_x(n, Cible.r),calcul_y(n, Cible.r))]
                tranche = self.cible.create_polygon(points_tranche, smooth = 1, splinesteps =50,
                                                 fill='',
                                                 activewidth=Cible.w, activeoutline='white', activedash =(3,3),
                                                 tags=(str(i),'zone'))
                
                self.cible.tag_bind(tranche,'<Button-1>',affiche)

            points_tranche_rond25 = []
            for i in range(8):
                a=45*i
                points_tranche_rond25.append((calcul_x(a, Cible.bord_rond25),calcul_y(a,Cible.bord_rond25)))
            rond25 = self.cible.create_polygon(points_tranche_rond25, smooth = 1, splinesteps =50,
                                          fill='',
                                          activewidth=Cible.w, activeoutline='white', activedash =(3,3),
                                          tags=('25','zone'))
            
            self.cible.tag_bind(rond25,'<Button-1>',affiche)
        
    def supprime_zones(self):
        nb_objets = len(self.cible.find_all())
        for i in range(nb_objets-1,0,-1):
            self.cible.delete(self.cible.find_all()[i])

    def ajoute_tranche(self, num):
        #num doit etre de type string
        if num in self.tranches.keys():
            self.tranches[num]['id'] = self.cible.create_image(830/2, 830/2, image=self.tranches[num]['img'])
        self.cible.tag_raise('zone')
        
    def supprime_tranche(self, num):
        if num in self.tranches.keys():
            self.cible.delete(self.tranches[num]['id'])
            self.tranches[num]['id'] = None
    
    def supprime_toutes_les_tranches(self):
        for tranche in list(self.tranches.values()):
            if tranche['id'] != None:
                self.cible.delete(tranche['id'])

"""
def test():
    r=tkinter.Tk()
    r.title('Cible')
    r.geometry('830x830+0+0')
    r['bg']='red'
    r.columnconfigure(0, minsize=830/2, weight=1)
    r.rowconfigure(0, minsize=830, weight=1)
    bordcontenantGauche = tkinter.Frame(r, background='green', bd=3,\
                                                 width = 830, height = 830)
    bordcontenantGauche.grid(row=0, column=0, sticky='n'+'s'+'e'+'w')
    bordcontenantGauche.grid_columnconfigure(0, weight=1)
    bordcontenantGauche.grid_rowconfigure(0, weight=1)
    c=Cible(bordcontenantGauche,r)    
    c.ajoute_tranche('5')
    c.ajoute_tranche('15')
    c.ajoute_tranche('4')
    c.ajoute_tranche('25')
    #c.supprime_tranche('4')
    #c.supprime_toutes_les_tranches()
    print(['']+c.zones())
    r.mainloop()
"""
