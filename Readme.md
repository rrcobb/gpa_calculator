# GPA Calculator
GPA doesn't matter too much for software engineering jobs, but your  friends might want to go to grad school or med school. Let's help them out with a little GPA calculator.

Once you've downloaded the files, try running the tests with `$python gpa_test.py`. You should get a failure message. Write your solution in gpa.py, and run the tests again to see if you pass!

##Round 1
In gpa.py, write a function `calculate()` that will take an array of dictionaries of grade data as input and output the correct GPA. GPA is an average of the GPA-value of the grade in each class. An 'A' is a 4.0, a 'B' is a 3.0, etc.

If a student had grades of A, A, B, and C, they would have a GPA of (4 + 4 + 3 + 2) / 4 = 3.25.
If they had grades of B, C, D, and F, they would have a GPA of (3 + 2 + 1 + 0) / 4 = 1.5

Input will look like this:
```python
[
 {
   'course' : 'Intro to Computer Science',
   'grade' : 'A'
 },
 {
   'course' : 'Freshman Writing Seminar',
   'grade' : 'A'
 },
 {
   'course' : 'Calculus I',
   'grade' : 'B'
 },
 {
   'course' : 'Physics I',
   'grade' : 'C'
 }
]
```
And your function should return a float:
```python
3.25
```

## Round 2
Your med school friends tell you that med schools often include the pluses and minuses in the GPA calculation. You get a sudden urge to update your calculator program!

The new possible grades, and the corresponding effect on GPA:

|Grade  | Value |
|------ |-------|
|A+ or A|  4.0  |
|   A-  |  3.7  |
|   B+  |  3.3  |
|   B   |  3.0  |
|   B-  |  2.7  |
|   C+  |  2.3  |
|   C   |  2.0  |
|   C-  |  1.7  |
|   D+  |  1.3  |
|   D   |  1.0  |
|   D-  |  .7   |
|   F   |   0   |

Modify your GPA calculator so that it can handle pluses and minuses, and calculate the score appropriately!

Round 2 Sample input:
```python
[
 {
   'course' : 'Intro to Philosophy',
   'grade' : 'B-'
 },
 {
   'course' : 'Great Works of American Literature',
   'grade' : 'A-'
 },
 {
   'course' : 'Calculus II',
   'grade' : 'B+'
 },
 {
   'course' : 'Native American History I',
   'grade' : 'A+'
 }
]
```
With that input, your function should return:
```python
3.425
```
## Round 3
Some courses are worth more credits than others. Those courses should count more in your GPA!

Instead of a simple average, modify the calculator so that it outputs a weighted average, based on how many credits a course was worth.

Sample input:
```python
[
 {
   'course' : 'Welcome to the University',
   'grade' : 'A',
   'credits': 1
 },
 {
   'course' : 'Introduction to Sociology',
   'grade' : 'A-',
   'credits': 3
 },
 {
   'course' : 'Film Art in a Global Society',
   'grade' : 'B+',
   'credits': 4
 },
 {
   'course' : 'International Government',
   'grade' : 'C',
   'credits': 3
 }
]
```
And you should return:
```python
3.118118
```
### Bonus Challenges:
- Your friends need to interact with your calculator! Turn the calculator into a command line program. Or better yet, a website!
- Add a function to the calculator to tell you how much impact a particular assignment will have on your GPA. Will missing this homework assignment impact your chances of going to grad school???
