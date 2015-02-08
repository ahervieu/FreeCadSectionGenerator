import csv



def main() :
    with open('/Users/Aymeric/Generateur_Section_bateau/rsc/coque_data.csv','rU') as csvfile:
        coque = csv.reader(csvfile,delimiter=';',dialect='excel',)
        i = 0
        for row in coque:
            createSection(i,row)
            i=i+1

            print row

def createSection(number, row):

    #0 : A, 1 : B,2 : C, 3 : D, 4 : E, 5 : F, 6 : G, 7 : H, 8 : I, 9 : J, 10 :K , 11 : L, 12 : M
    Ex = -float(row[11])/2
    Ey = 0 -float(row[0])

    EEx = -Ex
    EEy =  Ey

    Bx = -float(row[6])/2
    By =  float(row[1])

    BBx = -Bx
    BBy =  By

    Hx = -float(row[6])/2
    Hy =  float(row[1])- float(row[6])

    Cx = - float(row[6])/2 - float(row[7])
    Cy =   float(row[1]) -  float(row[7])

    CCx = -Cx
    CCy = Cy

    Gx = - float(row[10])
    Gy =  float(row[3]) -  float(row[0])

    GGx = -Gx
    GGy = Gy

    Dx = - float(row[10])
    Dy =  float(row[3]) - float(row[0])

    DDx = -Dx
    DDy = Dy

doc = FreeCAD.newDocument("coque_" +str(number))
Draft.makeLine(FreeCAD.Vector(Ex,Ey.5,0),FreeCAD.Vector(EEx,EEy,0))
Draft.makeLine(FreeCAD.Vector(Bx,By,0),FreeCAD.Vector(BBx,BBy,0))
Draft.makeLine(FreeCAD.Vector(Dx,Dy,0),FreeCAD.Vector(Cx,Cy,0))
Draft.makeLine(FreeCAD.Vector(DDx,DDy,0),FreeCAD.Vector(CCx,CCy,0))
plh=FreeCAD.Placement()
plh.Base=FreeCAD.Vector(Hx,Hy,0.0)
Draft.makeCircle(radius=30,placement=plh,face=False,startangle=-90,endangle=-180.0,support=None)
plhh=FreeCAD.Placement()
plhh.Base=FreeCAD.Vector(HHHx,Hy,0.0)
Draft.makeCircle(radius=30,placement=plhh,face=False,startangle=0,endangle=-90.0,support=None)


plg=FreeCAD.Placement()
plg.Base=FreeCAD.Vector(Gx,Gy,0.0)
Draft.makeCircle(radius=30,placement=plh,face=False,startangle=90,endangle=-180.0,support=None)
plgg=FreeCAD.Placement()
plgg.Base=FreeCAD.Vector(GGx,Gy,0.0)
Draft.makeCircle(radius=30,placement=plhh,face=False,startangle=0,endangle=-90.0,support=None)




createSection(0,['24', '109.5', '133.5', '16', '42', '12', '12', '15', '12', '13', '0', '0', '32'])



