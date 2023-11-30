class Rectangle():
    _nbrRectangle = 0
    def __init__(self, Largeur, Longueur):
        self._Largeur = Largeur
        self._Longueur = Longueur
        Rectangle._nbrRectangle += 1

    def GetLargeur(self):
        return self._Largeur
    
    def SetLargeur(self,NewLargeur):
        self._Largeur = NewLargeur
    
    def GetLongeur(self):
        return self._Largeur
    
    def SetLongeur(self,NewLongueur):
        self._Longueur = NewLongueur

    def GetNbrRectangle(self):
        return self._nbrRectangle
    
    def Equals(self):
        if(self._Longueur == self._Largeur):
            return True
        else:
            return False
        
    def Perimetre(self):
        return (self._Longueur + self._Largeur) * 2
    
    def Surface(self):
        return (self._Longueur * self._Largeur)
    
    def ToString(self):
        return "Largeur = "+str(self._Largeur)+"\nLongueur = "+str(self._Longueur)+"\nSurface = "+str(Rectangle.Surface(self))+"\nPerimetre = "+str(Rectangle.Perimetre(self))+"\nNombre " +str( Rectangle.GetNbrRectangle(self))+" de rectangle"
    
class parallelipipede(Rectangle):
    _nbrparallelipipede = 0
    def __init__(self, Largeur, Longueur, hauteur):
        Rectangle.__init__(self,Largeur, Longueur)
        self._hauteur = hauteur
        parallelipipede._nbrparallelipipede +=1
    
    def GetHauteur(self):
        return self._hauteur
    
    def SetHauteur(self,NewHauteur):
        self._hauteur = NewHauteur

    def GetNbrParallelipipede(self):
        return self._nbrparallelipipede
    
    def Equals(self):
        if(Rectangle.GetLongeur == Rectangle.GetLargeur):
            return True
        else:
            return False
    
    def Surface(self):
        return 2 * (Rectangle.GetLongeur * Rectangle.GetLargeur + Rectangle.GetLongeur * self._hauteur + Rectangle.GetLargeur * self._hauteur)
    
    def Volume(self):
        return Rectangle.GetLongeur(self) * Rectangle.GetLargeur(self) * self._hauteur
    
    def ToString(self):
        return super().ToString() + "\nLa hauteur : "+str(self._hauteur)+"\nLe volume = "+str(parallelipipede.Volume(self))
    
print("Les coordonnees du rectangle")
R1 = Rectangle(13,25)
print(R1.ToString())
print("**********************")
print("Les coordonnees du rectangle")
p1 = parallelipipede(15,19,24)
print(p1.ToString())
