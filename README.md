Day 09: Bidding System in Python

Welcome to *Day 09* of my *100 Days of Python Challenge*!  
Today, I developed a **bidding system** that collects bids from multiple users and determines the highest bidder. This simple yet functional program leverages Python dictionaries and loops for dynamic interaction.


📝 Project Overview
The *Bidding System* is an interactive program that allows users to:
1. Enter their name and bidding amount.
2. Store the bids in a dictionary.
3. Determine the user with the highest bid.


💻 How It Works
1. Collecting Bids
- The program prompts each user to input:
  - *Name*: Acts as the key in the dictionary.
  - *Bidding Amount*: Acts as the value in the dictionary.
- The bids are stored dynamically in a dictionary:
2. Repeated Entry
- The program continues to accept bids until the user specifies that no more bidders are present.
3. Clearing the Console
- After each bid entry, the console is cleared by printing 100 newline characters.
4. Finding the Maximum Bidder
- The program identifies the maximum bidder using the max() function on the dictionary:


📚 Concepts Applied
  Dictionaries: Used to store and retrieve dynamic key-value pairs.
  Loops: Utilized a while loop for repeated entry until the user opts to stop.
  Conditional Logic: To handle the flow of the program based on user input.
  Functions: max() for determining the highest bid.
  Dictionary methods like items() for iteration.
