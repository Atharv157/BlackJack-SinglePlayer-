import random
wallet = 1000
deck=[]
temp=[]
hit=False
bet=0
br=False
#1- Hearts
#2- Spades
#3-Diamond
#4-Club
def make_deck():
    SUITE = "Hearts Diamond Spades Clubs".split()
    RANKS = "1 2 3 4 5 6 7 8 9 10 J Q K".split()
    global deck
    #for x in range(10):
        #RANKS[x]=int(RANKS[x])
    deck = [(r,s) for  s in SUITE for r in RANKS]
    #temp = [(i,j) for i in SUITE for j in face_cards]

class Individual:
    def __init__(self):
        print("Fresh hand")
        self.hand=[]
        self.total=0
    def hit(self):
        global hit
        global br
        deal(self)
        update(self)
        print("your cards are : ")
        print(self.hand)
        print("Total : "+ str(self.total))
        hit = True
        if self.total>21:
            print("You Lost  !!!")
            end = True
            br=True
    def double_down(self):
        global wallet
        global bet
        global hit
        global br
        if hit :
            print("cannot double down now as you have opted for hit before")
        elif [9,10,11].count(self.total):
            print("bet amount doubled !!!")
            deal(self)
            update(self)
            print("your cards are : ")
            print(self.hand)
            print("Total : "+ str(self.total))

            wallet -= bet
            bet = bet *2
            hit = True
            br=True
        else :
            print("total does not equals 9/10/11")


def deal(indiv):
    indiv.hand.append(deck.pop(deck.index(random.choice(deck))))
def update(indiv):
    face_cards = "J Q K".split()
    if len(set(face_cards)&set(indiv.hand[-1][0]))>0:
        indiv.total +=10
    else:
        indiv.total = indiv.total + int(indiv.hand[-1][0])

#main
quit=1
make_deck()
#print(deck)
while(quit):
    br=False
    player=Individual()
    dealer=Individual()
    #print(deck)
    #player = []
    #player_total = 0
    #dealer_total = 0
    #dealer = []
    #pcount  = 0
    #dcount = 0
    hit = False
    end = False
    print("Currently you have a wallet amount of "+ str(wallet))
    bet = int(input("Enter bet amount : "))
    wallet = wallet - bet
    for i in [player,dealer]:
        deal(i)
        update(i)
        deal(i)
        update(i)

    print("your cards are :")
    print(player.hand)


    print("Total : ", player.total)
    print("dealer's cards are : "+str(dealer.hand[0])+" second card is closed")
    while(1):
        choice = int(input("1 : Hit \n 2 : Stay \n 3 : Double Down "))
        if choice ==1 :
            player.hit()
            if br:
                break
        elif choice == 2 :
            break
        elif choice == 3:
            player.double_down()
            if br:
                break

    if not end:
        while(1):
            if dealer.total >=17:
                break
            elif dealer.total < 17:
                print("dealer is hittingyeyey")
                deal(dealer)
                update(dealer)
                print("dealers cards are ")
                print(dealer.hand)
        if dealer.total > 21 or player.total > dealer.total:
            print("You Win  !!!")
            if player.total ==21:
                wallet = wallet + (2.5*bet)
            else:
                wallet = wallet + (2*bet)
        elif player.total == dealer.total:
            print("draw")
        else:
            print("You Lost !!!")
    quit = int(input("do you want to play another game ?.. 1 for yes...0 for no"))
