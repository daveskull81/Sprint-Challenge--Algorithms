#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a)

O(n^3)
The code starts by setting a variable a with the value of 0. There is a while loop that looks at a and compares it to n times n times n or n^3. This comparison is done on every iteration of the loop and the multiplcation has to be performed each time. Instead if one created a variable outside of the loop and setting its value to n^3 for comparison it could be a constant time lookup for the value of that variable.
There is also a not so simple math operation happening on each iteration. With the need to perform the calculation of n^3 on each iteration I think this gets exponentially difficult with larger inputs.


b)

O(n^2)
There are two loops in the code with one nested beneath the other. The first loop is going over every item for the input n. If the input n was 10 it would be iterating 10 times.
On each iteration of the outer loop the inner loop decalres a variable of j and sets it to the value of 1. This then goes while the value is less than the input n. Inside this loop it multiplies j by 2 and will do a number of iterations that is half the value of n.
Considering this is a nested loop within a loop and there are multiple iterations happening for each item in n it looks to be quadratic.



c)

O(n)
There isn't any value of n in this question, but there is an input of the number of bunnies. Based on the number of bunnies the recursive function will be called for every bunny down to 0 bunnies. So, if the number 5 is input the function will be called 6 times. Once for each bunny and once for 0. It has to be called for every single bunny in the input.

## Exercise II

The sentence "Devise a strategy to determine the value of f such that the number of dropped + broken eggs is minimized." seems to infer ther return value should be a total of two numbers. The total number of dropped eggs and the total number of broken eggs. The goal is that this number is as small as possible.

To determine the value of f for the floor where eggs break I would start at the first floor and drop one egg off of it and see if it breaks or not. If the egg breaks then I know the first floor is the value of f and would only have dropped 1 egg with that 1 breaking. So it would be a total of 2 returned.
If the egg did not break this process could be repeated on the next floor.

Essentially, I would go to each floor starting at the first and drop off one egg from it.
I would check to see if the egg broke and if it did not I would go up to the next floor and drop one egg from that floor. I would repeat this process until I dropped an egg and it broke. The floor I would be on at that point would be the value of f and I would have dropped one egg for every floor I visited and only have one broken egg.
Worse case scenario is that the last floor is the one where they break. This would give me a total of n dropped eggs plus one broken egg.

That looks to be a runtime of n + 1, so it would be a O(n) runtime.

Another strategy would be to start at the middle floor and drop an egg to see if it breaks. If it does the floor f is in the first half of the floors. If it does not the floor f is in the second half of the floors.
Next you can go the middle point of the half of floors where we know the floor f to be. Then we drop an egg from there and see if it breaks. Continuing this process of dropping an egg at the middle point we can break the list of floors in half each time to determine where the floor f is that will make eggs break.

In the worse case scenario this would be an O(log(n)) runtime.

