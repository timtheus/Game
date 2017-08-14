import random
inf=-5
sup=5
flag_ant=1
class Sprite:
    def __init__(self,gm,point=0):
        self.gm=gm
        self.step=0
        self.dice = [-6,-5,-4,-3,-2,-1,1, 2, 3, 4, 5, 6]
        self.flag=0
        if point==0:
            self.point=random.randint(inf,sup)
        else:
            self.point=self.dice_gen()
    def dice_gen(self):
        return random.choice(self.dice)
    def jump(self):
        if inf<=self.point+self.step<=sup:
            self.point+=self.step
        elif self.point+self.step<inf:
            self.point=inf
            self.flag+=1
            if self.flag>=flag_ant:
                print("Game Over!\nAnt wins!")
                exit(0)
        elif self.point+self.step>sup:
            self.point=sup
            self.flag+=1
            if self.flag>=flag_ant:
                print("Game Over!\nAnt wins!")
                exit(0)
    def choice(self):
        ch=input()
        if ch=='y':
            self.step=self.dice_gen()
            self.jump()
        elif ch=='n':
            self.step=0
            self.jump()
class Ant(Sprite):
    def __init__(self,gm,point=0):
        super().__init__(gm,point)
        print("The ant\'s initial position is:", self.point)
        self.gm.set_point("The ant\'s position is:",self.point)
    def choice(self):
        print("The ant\'s position is:", self.point,"do you want to throw the dice:")
        super().choice()
        self.gm.set_point("The ant\'s position is:", self.point)
class Worm(Sprite):
    def __init__(self,gm,point=0):
        super().__init__(gm,point)
        print("The worm\'s initial position is:", self.point)
        self.gm.set_point("The worm\'s position is:", self.point)
    def choice(self):
        print("The worm\'s position is:", self.point,"do you want to throw the dice:")
        super().choice()
        self.gm.set_point("The worm\'s position is:", self.point)
class Gamemap:
    def __init__(self):
        self.ant_point=0
        self.worm_point=0
    def judge(self,sp):
        if self.ant_point==self.worm_point and self.worm_point!=0 and self.ant_point!=0:
            print("Game Over!\nWorm wins!")
            exit(0)
    def set_point(self,str,point):
        if str=="The ant\'s position is:":
            self.ant_point=point
        else:
            self.worm_point=point
        print("His position is %d now" % point)
gm=Gamemap()
ant=Ant(gm)
worm=Worm(gm)
sp=Sprite(gm)
print("Press return  to start...")
input()
i=1
while True:
    gm.judge(sp)
    print("Round ",i)
    ant.choice()
    print("Worm\'s turn")
    worm.choice()
    print("Ant\'s turn")
    print(sp.flag)
    i+=1