1. When an empty string in given, returns 0
2. When 0 is given, returns 0
3. When a single number is given, returns the number itself
4. When two numbers seperated by comma is given, returns the sum of the numbers.
5. When two numbers by \n separated are given, returns the sum of the numbers.
6. When the numbers are given with custom delimiters, should be handled carefully.
7. When a negative number is given, throws an exception.
8. When a number greater than 1000 is given, the number should be considered as 0
Given below are the few inputs and expected results.........

Input                  Result
""                      0
0                       0
2                       2
1,2                     3
1\n2                    3
1\n2,3                  6
//;\n1;2                3
1,-2                    Exception
2,1001                  2
