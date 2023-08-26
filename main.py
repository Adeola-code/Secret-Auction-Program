from replit import clear
import art
#Import logo
logo=art.logo
print(logo)
#Create a list with all_bids
all_bid=[]
#Create function to add a dictionary with the bidders name and price
def add_new_bid(name, bid):
    bid_info={}
    bid_info["name"]=name
    bid_info["bid"]=bid
    all_bid.append(bid_info)
#To keep the program runnig
no_bid=False
while not no_bid:
    name=input("What is your name?: ")
    bid=int(input("What's your bid price?: $"))
    
    add_new_bid(name, bid)
    
    #Ask if anyone still wants to bid
    restart=input("Are there still any other users who want to bid?. Type 'yes' or 'no' ").lower()
    if restart=="yes":
        no_bid=False
        clear()
    elif restart=="no":
        no_bid=True
        max_bid_dict = max(all_bid, key=lambda x: x['bid'])
        max_bid = max_bid_dict['bid']
        name_with_max=max_bid_dict["name"]

        print(f"The winner is {name_with_max} with a bid of ${max_bid}")        





#  My console doesn't clear!

# This will happen if you’re using an IDE other than replit
#  (e.g., VSCode, PyCharm etc). 
#  The `clear()` function is available here via the replit module without any extra configuration. 