from auction import logo

print(logo)
print("*************Welcome to the Python Auction*************")

def find_highest_bidder(bidder_record):
    winner = ""
    highest_bid = 0

    for bidder in bidder_record:
        bid_amount = bidder_record[bidder]
        if bid_amount > highest_bid:
            highest_bid = bid_amount
            winner = bidder
    print(f"The Auction winner is {winner} with a bid of ${highest_bid}")



bids = {}
auction_condition = True

while auction_condition:
    name = input("Please enter your name: ")
    price = int(input("Please enter your bidding:  $"))
    bids[name] = price

    continue_bid = input("Are there any other bidders?  type 'yes' to continue or 'no' to pass: ")
    if continue_bid == "no":
        auction_condition = False
        find_highest_bidder(bids)
    elif continue_bid == "yes":
        print("\n" *20)


# TODO-1: Ask the user for input
# TODO-2: Save data into dictionary {name: price}
# TODO-3: Whether if new bids need to be added
# TODO-4: Compare bids in dictionary