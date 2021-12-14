#object oriented programming
#from filename import classname

class Player:

    # set attribute
    allplayer = []
    feetransfer = 0.1

    # automate run function
    def __init__(self, name: str, age: int, club :str, position = 'not found'): #set default

        print('__init__ is automate run when use Class')

        # set validation / error raised
        assert age >= 15 and age <= 50, 'Player must age at least 15, and not more than 50'

        # assign to self object / class know about object
        #self.__name > when use __ (dunder) mean this is private
        #also must set private in property
        self.__name = name.strip().title()
        self.age = age
        self.club = club.strip().capitalize()
        self.position = position.upper()

        # action to execute / for use later, if we want
        Player.allplayer.append(self)

    #basic function
    def playerdata(self):
        return f'name {self.__name:10} {self.position}'

    #use any thing in class must call self.anything
    def feefromsalary(self, salary) :
        return salary * self.feetransfer

    #private methode use dunder / user can't use this
    def __connectstaff(self):
        return 1.2 * self.feetransfer

    #method in method
    def total(self, cash: int):
        return cash + self.__connectstaff()
        

    #when fuction is't relate with anything in Class
    @staticmethod 
    def shout(something):
        return f'someone call {something}'

    #when function don't use any self object in class    
    #pretend like  new class for support main class
    @classmethod 
    def playerage(cls,name, club, birthday, now) :
        age = now-birthday
        return cls(name, age,club) #paremeter same as maiin class


    #can read only ,can't change name // like player.name = any
    #AttributeError: can't set attribute 'name'
    @property
    def name(self):
        return self.__name

    #if want to change but have some condition
    #value is something that  gonna change
    @name.setter
    def name(self, value):
        if len(value) > 20 :
            raise Exception('Player name is too long!')
        else :
            self.__name = value

    # set Class/obj to String // like str(Class)
    # self.__class__.__name__ -> name of class   > show when print(Player)
    def __str__(self):
        return f'{self.__class__.__name__:5} > {self.__name}[{self.position}] {self.club}'

    #order __str__ > __repr__ (for dev read) > show when print(Player.allplayer)
    def __repr__(self):
        return f'Class.{self.__class__.__name__} p1.{self.__name}  p2.{self.age} p3.{self.club} p.4{self.position}'




#create some class
class Tesla :
    def __init__(self) :
        self.model = 'Tesla Model S 2021'

    def cardriving(self, person):
        return f'automincar Tesla is running by {person.name}'

    def __str__(self):
        return f' {self.model}'



# inherit class  -> 'child class' like we copy every thing from Parent class
class Staff(Player) :

    # change attribute
    feetransfer = 0.05

    def __init__(self, name: str, age: int, club: str, staffposition = 'coach'):
        super().__init__(name, age, club)  #call parent class ,like we code > self.name = name
 
        #change assert
        assert age >= 30 and age <= 70, 'Player must age at least 30, and not more than 70'

        #assign new
        self.staffposition = staffposition

        #create new attribute by calling class
        self.car = Tesla()

    def staffcard(self):
        return f'{self.staffposition} | {self.name} in {self.club}'

    #change medthod
    def __str__(self):
        return f'{self.name} | {self.staffposition}'

#for run only this file
if __name__ == '__main__' :
    player1 = Player('chana', 26, 'osaka', 'amf')
    print(player1.name)
    print(player1)
    print(player1.feefromsalary(100))


    #before add plyer
    print(f'before --> {Player.allplayer}')
    allplayer = [['ronaldo', 36, 'united', 'cf'], ['messi', 34, 'paris', 'ss']]
    for person in allplayer :
        Player(person[0],person[1],person[2],person[3])

    print(f'after --> {Player.allplayer}')
   

    #for debug : show every single medthod
    print(Player.__dict__)

    staff1 = Staff('nichino',40,'japan','line coach')
    # print(staff1.total(10))

    #child class can use every thing from parent
    print(staff1.total(10))

    #but parent can't use every sigle thing in child
    print(staff1.staffcard())
    print(player1.playerage('chana','osaka',2000,2021))

    #call function in other class
    print(staff1.car.cardriving(staff1))
