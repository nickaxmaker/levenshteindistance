# Levenshtein Distance Calculator
Implementation of [Wagner-Fischer algorithm](https://en.wikipedia.org/wiki/Levenshtein_distance#Iterative_with_full_matrix) to calculate the Levenshtein distance. When running the program, the last entry in the list is the Levenshtein distance. 

Examples used in testing: 
1. saturday / sunday = Levenshtein distance of 3
2. kitten / sitting = Levenshtein distance of 3

My variant doesn't care about capital letters, only comparing the actual letters themselves. This may or may not be what others do, but if you don't like it, it's easy to edit the code to remove the lower casing. If one does that, it will calculate the difference in capitalization as well. 

## Learning Goals

1. Using psuedocode for a known algorithm as a base to write a program. 
2. Higher familiarity with two-dimensional lists with no additional libraries.

I've never referenced someone else's psuedocode algorithm to write my own code before and wanted to give it a try, since it seems like a useful thing to know how to do if there has already been work in the field that you're doing at this point. It's good practice, especially when you're spending time learning new algorithms all the time.  