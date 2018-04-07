## Code:
All of the code was written by me in SageMath, saved in .py files. SageMath is an open source Math oriented software system based off of Python 2. All of my code was stored in files and functions. To use the code, in my current Sage workbook I would use the command load() to load one of the files into that workbook and then call whatever functions I needed.

Most of this code is just Python list operations, and lots of comparisons using SageMath's isIsomorphic() function.

All the code in the folder Array Hardcodes is simply hardcodings of several different arrays generated by these programs, so that when testing I wouldn't have to regenerate them each time. However, for all of the final data sets all of the data was completely regenerated from the original 19 graphs.

G10.0-G10.18.py is a hardcoding of the original 19 cubic graphs, used to generate all of the other data.

BD_Decks.py is code to generate all of the decks from all of the Kocay graphs from one cubic graph.

AllCards.py is code for making all of the cards, and checking for isomorphisms. It uses BD_Decks.py and G10.0-G10.18.py.

AppearanceChart.py is code for generating the appearance charts.

SortIsoList.py is code for sorting the isomorphism lists by degree sequence.

KocaySharing.py is code for generating the Kocay card sharing chart and lists of Kocay graphs that share cards.

The biggest operation in this code was checking for isomorphisms in the cards. Worst case, you had to compare 2850 cards against 2850 cards which is 8,122,500 comparisons. However, it is unneccessary to compare a card to itself, saving you 2850 comparisons. It is also unneccesary to compare cards both directions. Basically, if you compare y to x, you don't need to later compare x to y, so that saves you a great deal of comparisons. You also don't need to compare cards with cards that you know are isomorphic with cards you've already compared them to, saving many comparisons. I don't know exactly how many comparisons it took, I should record that number sometime.