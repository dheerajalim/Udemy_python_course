from import_modules_tut.addition import Addition
# You don't need to change the import statement
# now you can use Addition.add() function from the addition module like this:
# res = Addition.add(100, 150)
# the Addition.add() function takes in two parameters `num1` and `num2` and return the sum of `num1` and `num2`


# Please create and implement a Calculator class, which makes use of the `addition` module.
# Your Calculator should achieve these goals:
# - It should implement `Addition.add()`, `subtract()`, `multiply()` and `divide()` methods.
# - It cannot use addition, subtraction, multiplication and division operators (`+`, `-`, `*` and `/`) directly.
#   Instead, it should be only based on the `Addition.add()` function from the `addition` module.
# - To simplify the problem, you may expect input for the multiply() and divide() methods are all non-integers,
#   and will always be valid, i.e. all non-negative integers and no 0 as divisor.

# the class definition and a sample class method `Addition.add()` is provided below
class Calculator:

    # a sample add() method in our calculator is shown below
    # you may learn from it and implement the other methods
    @classmethod
    def add(cls, num1, num2):
        return Addition.add(num1, num2)  # make use of add() from addition module

    # implement a class method `subtract()` that takes in num1 and num2 and return num1 - num2
    # your `subtract()` method cannot use the + - * / calculation operators, but can use - as a negative sign operator

    @classmethod
    def subtract(cls,num1,num2):

        if num2 > 0:
            num2 = Addition.add('-', str(num2))

        elif num2 < 0:
            num2 = str(num2).strip('-')

        return Addition.add(num1, int(num2))
        # else:
        #     num2 = '-'+str(num2)
        #     return Addition.add(num1, int(num2))


    # implement a class method `multiply()` that takes in num1 and num2 and return num1 * num2
    # your `multiply()` method cannot use the + - * / calculation operators, but can use - as a negative sign operator
    # you may assume num1 and num2 are always non-negative integers

    @classmethod
    def multiply(cls,num1,num2):
        if num1 == 0 or num2 ==0:
            return 0
        else:
            looper = num1
            for i in range(0,num2-1):

                looper = Addition.add(looper,num1)

        return looper

    # implement a class method `divide()` that takes in num1 and num2 and return num1 // num2
    # your `divide()` method cannot use the + - * / calculation operators, but can use - as a negative sign operator
    # you may assume num1 is always a non-negative integer, and num2 is always a positive integer

    @classmethod
    def divide(cls, num1, num2):

        if num2 > num1:
            return 0;

        else:
            ans = 1
            value = num2
            while 1:

                value = Addition.add(value, num2)
                if value < num1:
                    ans = Addition.add(ans, 1)
                    continue

                elif value == num1:
                    ans = Addition.add(ans, 1)
                    break

                elif value > num1:
                    break
        return ans


result = Calculator()
print(result.divide(11,2))