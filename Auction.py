logo = '''
                         _____
                         \         /
                          )___(
                          |"""""""|.-.,.---------.,.-.
                          |       | | |               | | ''-.
                          |       || |             | |..-'
                          |___| '-' '---------' '-'
                          )"""""""(
                         /___\\
                       .-------------.
                      /_____\\
'''
import os
def clear():
    os.system('cls')

print(logo)
bid={}
bid_finished=False
def highest_bid(bidding_record):
    max=0
    winner=""
    for bidder in bidding_record:
        bid_amount=bidding_record[bidder]
        if bid_amount>max:
            max=bid_amount    
            winner=bidder
    print(f"the winner of the bid is : {winner} with a bid of {max}$")

while not bid_finished:
    name=input("please enter your name: ")
    bid_amount=int(input("please enter your bid: "))
    bid[name]=bid_amount
    decision=input("Is there any bidder left: type yes or no: ")

    if decision=="no":
        bid_finished=True
        highest_bid(bid)
    elif decision=="yes":
        clear()