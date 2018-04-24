
########################################################
# Function Arguments Definition :- 
# R = query range = [xmin,xmax,ymin,ymax] 
# reg = region of a line node = [xmin,xmax,ymin,ymax]
# PN = A point node i.e object of Point class
# depth = depth of the tree (initial passed value = 0)
# lord = 1 implies we are considering left/down the line
########################################################

##########################################################################

def isInRange(PN,R,depth,lord):
    if depth%2==0:
        if lord==1:
            if PN.x>=R[0] and PN.x<=R[1] and PN.y>=R[2] and PN.y<=R[3]:
                return True
        else:
            if PN.x>R[0] and PN.x<=R[1] and PN.y>=R[2] and PN.y<=R[3]:
                return True
    else:
        if lord==1:
            if PN.x>=R[0] and PN.x<=R[1] and PN.y>=R[2] and PN.y<=R[3]:
                return True
        else:
            if PN.x>=R[0] and PN.x<=R[1] and PN.y>R[2] and PN.y<=R[3]:
                return True     
    return False

#################################################################################

def ReportSubtree(root):
    if root!=None:
        if hasattr(root,'x'):
            print "(",root.x,",",root.y,")"
            return
        ReportSubtree(root.left)
        ReportSubtree(root.right)               

################################################################################

def RegionFullyContained(reg,R,depth,lord):
    if depth%2==0:
        if lord==1:
            if reg[0]>=R[0] and reg[1]<=R[1] and reg[2]>=R[2] and reg[3]<=R[3]:
                return True
        else:
            if reg[0]>R[0] and reg[1]<=R[1] and reg[2]>=R[2] and reg[3]<=R[3]:
                return True
    else:
        if lord==1:
            if reg[0]>=R[0] and reg[1]<=R[1] and reg[2]>=R[2] and reg[3]<=R[3]:
                return True
        else:
            if reg[0]>=R[0] and reg[1]<=R[1] and reg[2]>R[2] and reg[3]<=R[3]: 
                return True
    return False

################################################################################

def RegionIntersect(reg,R):
    if reg[0]>R[1] or R[0]>reg[1]:
        return False
    if reg[2]>R[3] or R[2]>reg[3]:
        return False
    return True

###############################################################################

def SearchKdTree(root,R,reg,depth,lord):
    if root==None:
        return
    elif hasattr(root,'x'):
        if isInRange(root,R,depth-1,lord):
            print "(",root.x,",",root.y,")"    
    else:
        
        if depth%2==0:
            lc_region = [reg[0],root.x1,reg[2],reg[3]]
            rc_region = [root.x1,reg[1],reg[2],reg[3]]
        else:
            lc_region = [reg[0],reg[1],reg[2],root.y1]
            rc_region = [reg[0],reg[1],root.y1,reg[3]]

        #print depth," ",reg," ",lc_region," ",rc_region
        
        if RegionFullyContained(lc_region,R,depth,1):
            ReportSubtree(root.left)
        else:
            if RegionIntersect(lc_region,R):
                SearchKdTree(root.left,R,lc_region,depth+1,1)
                
                
        if RegionFullyContained(rc_region,R,depth,0):
            ReportSubtree(root.right)
        else:
            if RegionIntersect(rc_region,R):
                SearchKdTree(root.right,R,rc_region,depth+1,0)
                #print depth," ",rc_region

################################################################################     
                 
