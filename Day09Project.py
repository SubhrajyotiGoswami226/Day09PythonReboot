userDictionary = {}  

choice = "y"  

while choice.lower() == "y":
    userKeyInput = input("What is your name? \n")
    userValueInput = int(input("What is your bidding amount? \n"))  
    userDictionary[userKeyInput] = userValueInput
    choice = input("Is there a next bidder? (y/n) \n")
    print("\n" * 100)  

print("\nFinal Bidding Records:")

for key, value in userDictionary.items():
    print(f"{key}: {value}")


maxBidder = max(userDictionary, key=userDictionary.get)
print(f"\nThe maximum bidder is: {maxBidder} with a bid of {userDictionary[maxBidder]}")
