# byteTheCorrectApple

This was a hackerrank challenge, the problem statement and link is provided below

The word "Apple" could generally refer to one of these two:
(a) Apple Inc., the great Computer giant.
(b) Apple, the fruit

You are provided a text file, with a number of lines. Each line contains either a sentence or a paragraph or a text snippet which could either be related to Apple, the computer company, or the apple, the fruit. Your task is to perform disambiguation between these two groups and identify which one is being referred to. It is possible that the plural or the possessive form of Apple might exist in some of the tests (apples, Apple's).

Training Data
You are provided with two text files, which contain near-complete text from the Wikipedia for Apple Inc. as well as apple the fruit. 

https://www.hackerrank.com/challenges/byte-the-correct-apple/problem



Sample Input

Apple already plans to buy back `$100 billion in shares, including $`16 billion worth last quarter. Icahn probably pounded the dinner table he and Cook shared recently for their much-reported bread-breaking at Icahn's New York apartment. Apple's cash stash currently sits at a whopping `$145 billion but only $`43 billion is in the U.S., which is why Icahn wants to float bonds to cover a buy back.

Fortunately, there are “low-chill” apple varieties for temperate climates. (Chilling hours are defined as nonconsecutive hours of winter temperatures below 45 degrees.) As a general guide, if you live on or near the coast, your garden gets only 100 to 200 chilling hours. Inland San Diego gardens get about 400 to 500 chilling hours — still considered “low chill.”

Sample Output

computer-company

fruit

Explanation

In the first chunk of text, Apple Inc. is being referred to.  
In the second chunk, Apple the fruit is being referred to.  

# My Approach:
simple data engenering steps then created TFIDF matrix and pass it through SVM and was able to achive 100% accuary
