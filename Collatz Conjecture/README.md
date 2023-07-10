# Collatz Conjecture Implementation


This is a python implementation of the known mathematical problem named
"The Collatz Conjecture", you might also know it as the "3n+1 Problem".

## Modes

### Detailed Mode

In Detailed Mode you can see additional data about intermediate results,
at the cost of a portion of the speed of the program.
These additional data consists of the biggest number and the length of each
iterated number as well as a general statistical overview at the end, giving
information about the largest integer, the longest iterated number and the
time the calculation took.

### Fast Mode

In Fast Mode data about intermediate results is mostly not available. The
only data you can see is all numbers in your chosen range with their
respective number of iterations and the number that took the most
iterations to calculation, with the count of iterations it took.
Using this mode will greatly and exponentially increase execution speed.

## Usage

To get started, open your terminal/console and enter "python3 your/path/main.py".
First, the program will ask you about which mode (explained under "Modes") you want to use.
Answer with "y" for yes or "n" for no.
Additionally an option will show up, asking you for an iteration-counting.
Again, answer with "y" or "n", depending on your choice.
Before the program starts calculating, you must define a start and stop point (both integers)
which will define the range of numbers being calculated.
