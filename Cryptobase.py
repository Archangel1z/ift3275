from math import *

def powm(b, e, m): # retourne b^e(mod m)
    ret = 1
    while e > 0:
        if (e & 1 > 0): # e est impair
            ret = (ret * b) % m # on multiplie par la base b
        e >>= 1 # on divise e par 2
        b = (b * b) % m # on élève la base b au carré
    return ret

N = 220478789817846954008896827602146367603094186433902301475580185326213147774974463568692934890539198859855657088843791812533934329430965590114300437318317493890419646373788600314386915862469488995282327815811651143941633771533313955261186965943450155559547749180570873514941111463488772476223162962462970403644521663926858260772192374690667413278915622458501295488132742868927845060077023118972377392538762951151478892289332594612454083158506799745502768698226340978287299829036559684871978533451545448158415420055209724921039601333963345411636216097481662566260428364429674778488994313135030853675723

e = 3

C = 16250093121834914738489778721283850815023220823910545716502847730384833157965639674158854530545421681485384544525983824875


M = int(C**(1/e))

def binar(x) : #transforme un nombre en base 10 en sa chaine de caractères en base 2
    res = ''
    q =-1
    while q != 0 :
        q = x // 2
        r = x % 2
        res = str(r) + res
        x = q
    return res

def invbinar(mot): #fonction inverse de la précédente
    res = 0
    for i in range(len(mot)):
        if mot[i] == '1':
            res += 2**(len(mot)-i-1)
    return res

def blocs(n,k) : #transforme n en une liste de ses chiffres regorupés en blocs de taille k
    nc = str(n)
    if len(nc)%k != 0:
        nc = '0'*(k - len(nc)%k) + nc
    res = [0 for k in range(len(nc)//k)]
    for i in range(len(nc)//k) :
        j = i*k
        res[i] = nc[j:j+k]
    return res



auteurbin = blocs(binar(M),8)
auteur = [0 for i in range(len(auteurbin))]

for m in range(len(auteurbin)):
    auteur[m] = chr(invbinar(auteurbin[m]))

print(auteur)
