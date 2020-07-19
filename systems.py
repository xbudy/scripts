print(" systems solver by : xbudy ")
print("---------------w-")
print("|  Ax  × By   =C")
print("|  A'x × B'y  =C'")
print("----------------w")
##################func
def donn():
    global i, j, k, l, m, n
    eq=input("enter like  a b c space: ")
    eqp=input("enter like a' b' c' space: ")
    aqp=eqp.replace(' ', '/')
    aq=eq.replace(' ', '/')
    i, j, k = aq.split('/')
    l, m, n = aqp.split('/')
##########
def frc(a):
	try:
		b=a.as_integer_ratio()
		c=str(b)
		if len(c)>8:
			a=a
		else:
			if b[1]==1:
				a=a
			else:
				a=str(b).replace(',','/').replace('(','').replace(')','').replace(' ','')
	except:
		pass		
	return a
#####=###
def rmz(rkm):
    v=str(rkm)
    try:
        if v[-1]=='0' and v[-2]=='.':
            rkm=int(rkm)
    except :
       
     if v[-1] != '0':
        rkm=float(rkm) 
##########
    return rkm
def flt(argi):
    try:
        argi=int(argi)
        return argi
    except:
        argi=float(argi)
        return argi 
###################func
########execute
while True:
    try:
        donn()
        break
    except Exception:
        print("error try again !")
        False
    except (KeyboardInterrupt):
        print('\n good bye !')
        exit()
################################variable
a=flt(i)
b=flt(j)
c=flt(k)
ap=flt(l)
bp=flt(m)
cp=flt(n)
##########################Delta
Delta=a*bp - b*ap
##############################
print("---------------w-")
print("|  ",a,"x  + ",b,"y   =",c)
print("|  ",ap,"x  × ",bp,"y   =",cp)
print("---------------w-")
print("      |  ",a,"     ",b,"   |")
print("Delta=|                |=",a,"×",bp,"-",b,"×",ap)
print("      |  ",ap,"     ",bp,"   |  =",frc(rmz(Delta)))
#############################
print("  ")
print("  ")
#######calc
if Delta==0:
    print("!!! le systeme admet.inf or wlo")
if Delta !=0:
    DeltaX=c*bp - cp*b
    DeltaY=a*cp - c*ap
    x=DeltaX/Delta
    y=DeltaY/Delta
    print("---------------w-")
    print("       |  ",c,"     ",b,"   |")
    print("DeltaX=|                |=",c,"×",bp,"-",b,"×",cp)
    print("       |  ",cp,"     ",bp,"   |  =",frc(rmz(DeltaX)))
    print("---------------w-")
    print("       |  ",a,"     ",c,"   |")
    print("DeltaY=|                |=",a,"×",cp,"-",c,"×",ap)
    print("       |  ",ap,"     ",cp,"   |  =",frc(rmz(DeltaY)))
    print("")
    ################
    print("S=(",frc(rmz(x)),":",frc(rmz(y)),")")