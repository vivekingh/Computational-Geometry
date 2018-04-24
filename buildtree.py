import operator
import random
import matplotlib.pyplot as plt
from math import ceil
from sets import Set
from query import SearchKdTree

####################################

class Point:
    def __init__(self,a,b):
        self.x = a
        self.y = b

    
class Line:
    def __init__(self,a,b,c,d,e,f):
        self.x1 = a
        self.y1 = b
        self.x2 = c
        self.y2 = d
        self.left = e
        self.right = f

###################################

res = []

def plotting():
    global res,P
    cols = zip(*P)
    plt.plot(list(cols[0]),list(cols[1]),'ro')
    c = 0
    for i in res:
        plt.plot([i[0],i[1]],[i[2],i[3]],i[4])
        c = c+1
    #plt.legend()
    plt.show()
    
##########################################################################

def BuildKdTree(px,py,xmin,xmax,ymin,ymax,depth):

    #print px
    #print py
    #print ""
    
    global res
    
    if len(px)==0:
        return None
    
    elif len(px)==1:
        return Point(px[0][0],px[0][1])
    
    elif depth%2==0:
        mid = int(ceil(len(px)/2.0))
        pxnew1 = px[:mid]
        pxnew2 = px[mid:]
        
        while len(pxnew2)>0 and pxnew1[len(pxnew1)-1][0]==pxnew2[0][0]:
            pxnew1.append(pxnew2.pop(0))

        pynew1 = []
        pynew2 = []
        mini = pxnew1[0][0]
        maxi = pxnew1[len(pxnew1)-1][0]
        
        for i in py:
            if i[0]<=maxi:
                pynew1.append(i)
            else:
                pynew2.append(i)
        

    else:
        mid = int(ceil(len(py)/2.0))
        pynew1 = py[:mid]
        pynew2 = py[mid:]

        while len(pynew2)>0 and pynew1[len(pynew1)-1][1]==pynew2[0][1]:
            pynew1.append(pynew2.pop(0))
        
        pxnew1 = []
        pxnew2 = []
        mini = pynew1[0][0]
        maxi = pynew1[len(pynew1)-1][1]

        for i in px:
            if i[1]<=maxi:
                pxnew1.append(i)
            else:
                pxnew2.append(i)
                
    if depth%2==0:
        res.append([px[mid-1][0],px[mid-1][0],ymin,ymax,'y'])
        plotting()
        vleft = BuildKdTree(pxnew1,pynew1,xmin,px[mid-1][0],ymin,ymax,depth+1)
        vright = BuildKdTree(pxnew2,pynew2,px[mid-1][0],xmax,ymin,ymax,depth+1)
        return Line(px[mid-1][0],ymin,px[mid-1][0],ymax,vleft,vright)
    else:
        res.append([xmin,xmax,py[mid-1][1],py[mid-1][1],'y'])
        plotting()
        vleft = BuildKdTree(pxnew1,pynew1,xmin,xmax,ymin,py[mid-1][1],depth+1)
        vright = BuildKdTree(pxnew2,pynew2,xmin,xmax,py[mid-1][1],ymax,depth+1)
        return Line(xmin,py[mid-1][1],xmax,py[mid-1][1],vleft,vright)
        
######################################################################

# Change the points here (P variable) for your configuration
# Each Point(element of list) is (x,y)


P = [(1,3),(5,6),(4,2),(3,1),(6,3.5),(2.5,8),(5.63,6.62),(2,5),(4.42,4.42),(7.32,5.5)]
#print P,"\n"

#sorting based on x and y coordinate
Px = sorted(P,key=operator.itemgetter(0))
Py = sorted(P,key=operator.itemgetter(1))

cols = zip(*P)

tree = BuildKdTree(Px,Py,min(list(cols[0])),max(list(cols[0])),min(list(cols[1])),max(list(cols[1])),0)

query_search = [1,7,4,6.62] #[xmin,xmmax,ymin,ymax]

SearchKdTree(tree,query_search,[min(list(cols[0])),max(list(cols[0])),min(list(cols[1])),max(list(cols[1]))],0,1)





