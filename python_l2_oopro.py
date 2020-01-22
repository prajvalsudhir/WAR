from random import shuffle

SUITE = 'H D S C'.split()
RANKS = '2 3 4 5 6 7 8 9 10 J Q K A'.split()

player1=[]
cpu=[]


class deck():
    def __init__(self):
        self.SUITE= SUITE
        self.RANKS= RANKS

    def deal(self):
        self.cards=[]
        for i in range(0,4,1):
            for j in range(0,13,1):
                self.cards.append(SUITE[i]+RANKS[j])


        shuffle(self.cards)
        for i in range(0,26,1):
            player1.append(self.cards[i])
        for i in range(26,52,1):
            cpu.append(self.cards[i])


        print("player1 has cards:",player1)
        print("cpu has cards:",cpu)


class hand(deck):
    def __init__(self):
        self.count=0
        deck.__init__(self)

    def rank(self):
        print(player1)
        print(cpu)
        for i in range(0,1,1):
            if(player1[i]>cpu[i]):
                print("player1 has higher card")
                player1.append(cpu[i])
                cpu.pop(i)
            elif(player1[i]<cpu[i]):
                print("cpu has higher card")
                cpu.append(player1[i])
                player1.pop(i)
            else:
                print("war has occurred\n")
                for j in range(i,i+3,1):
                    if(player1[j]>cpu[j]):
                        count=count +1

                if count >=2:
                    print("player1 has won the war\n")
                    for k in range(i,i+3,1):
                        player1.append(cpu[k])
                        cpu.pop(k)
                    print("player1 has cards:", player1)
                    print("cpu has cards:", cpu)
                else:
                    print("cpu has won the war\n")
                    for k in range(i, i + 3, 1):
                        cpu.append(player1[k])
                        player1.pop(k)
                    print("player1 has cards:", player1)
                    print("cpu has cards:", cpu)


        print("player1 has {} cards left".format(len(player1)))
        print("cpu has {} cards left".format(len(cpu)))


class player(hand):

    def __init__(self):
        deck.__init__(self)
        hand.__init__(self)

    def check(self):
        if len(player1)== 0:
            print("player1 has lost and cpu has won")
        elif len(cpu)== 0:
            print("player1 has won congratulations")





print("Welcome to War, let's begin...")
while(1):
    p=int(input("press 1 to start the game \n"
            "press 2 to battle \n"
            "press 3 to end the war\n"))

    if p==1:
        print("creating decks and shuffling")
        play = deck()
        play.deal()
    elif p==2:
        print("battle starting")
        while len(player1)!=0 or len(cpu!=0):
          play1 = hand()
          play1.rank()
          play2=player()
          play2.check()
    elif p==3:
        print("thank you playing war\n")
        exit()







