

import gspread, collections

class champ:


    def starIcon(self):
        if self.sig == 0:
            return "*"
        else:
            return "#"
    


    def __init__(self, owner ="", champCsv = ""):
        self.owner  = owner
        input = champCsv.split(",")
        self.name   = input[0]
        self.star   = int(input[1])
        self.rank   = int(input[2])
        self.level  = int(input[3])
        if self.level == 0:
            self.level = (self.rank*10) + ((self.star==5) * 15)
    
        self.sig    = int(input[4])
        self.PI     = 0 #int(input[5])
        self.CR     = self.calcCR(self.star, self.rank)
        self.score  = self.CR * 1000000 + (self.star * 1000) +self.sig

    def details(self):
        # 4* Name 4/40 PI CR
        #return "{}{}  {} {}/{} [{:.0f}] ({:.0f}) - {}".format(self.star,self.starIcon(),self.name,
        #                                         self.rank,self.level,self.pi,self.CR, 
        #                                         self.owner)
        return "{}{} {} {}/{}s{} [{}] ({:.0f}) - {}".format(self.star,self.starIcon(),self.name,self.rank,self.level,self.sig,self.PI,self.CR,self.owner)
                
    

    def __repr__(self):
        
        #return str(self.star) + self.starIcon() +" "+ self.name 
        return self.details()

    def calcCR(self, star, rank):
        
        return (((star-1.5)*2)+rank)*10
# SORTING

    def __lt__(self,other):
        #print " Got self {} and {} :< {} ".format(self.fitness,other.fitness,self.fitness<other.fitness)
        return other.score < self.score

    def __eq__(self,other):
        try:
            return other.score==self.score
        except:
            return False


class rosterChamps:
##################################################
#
#   dict of champs holing all version of a
#   champ from a aRoster
#
##################################################

    def __init__(self):
        self.count  = 0
        self.unique = 0
        self.champ = collections.defaultdict(list)

    def add(self,tChamp):
        self.champ[tChamp.name].append(tChamp)
        self.count =+1
        self.unique = len(self.champ)

class rosterUsers:
##################################################
#
#   dict of users holing all champs
#   in there roster
#
##################################################

    def __init__(self):
        self.count  = 0
        self.unique = 0
        self.user = collections.defaultdict(list)

    def add(self,tChamp):
        self.user[tChamp.owner].append(tChamp)
        self.count =+1
        self.unique = len(self.user)





class rosterMatrix:
##################################################
#
#   holding champs per user and champs per unique champ
#   as two independent axis 
#
##################################################    

    def __init__(self):
        self.count = 0
        self.users = rosterUsers()
        self.champs = rosterChamps()

    def addChamp(self,tChamp):
        self.champs.add(tChamp)
        self.users.add(tChamp)
        self.count =+1
        
