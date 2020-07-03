import pytest
from exercises import beginnerExercises

# assignment
# assert beginnerExercises.helloWorld() == "Hello World!"


# assignment
# assert beginnerExercises.assignments() == "Hello World!"


# parameters
# assert beginnerExercises.parameters() == "Hello David"
# assert beginnerExercises.parameters() == "Hello 0"
# assert beginnerExercises.parameters() == "Hello "

# parametersOperators
# assert beginnerExercises.parametersOperators(5, 6) == "5 + 6 = 11"

# Conditionals
# assert beginnerExercises.conditionals(5, 6, "False") == "5 * 6 = 30"
# assert beginnerExercises.conditionals(5, 6, "True") == "5 + 6 = 11"

# Conditionals 2
# assert beginnerExercises.conditionals2(5, 6, "False") == "5 * 6 = 30"
# assert beginnerExercises.conditionals2(5, 6, "True") == "5 + 6 = 11"
# assert beginnerExercises.conditionals2(-5, 6, "True") == "-5 + 6 = 1"
# assert beginnerExercises.conditionals2(5, 0, "True") == "5"
# assert beginnerExercises.conditionals2(0, 6, "False") == "6"
# assert beginnerExercises.conditionals2(0, 0, "False") == "0"

# Recusrion
# assert beginnerExercises.recusion(5, 6, "False") == "5 * 6 = 305 * 6 = 305 * 6 = 305 * 6 = 305 * 6 = 305 * 6 = 305 * 6 = 305 * 6 = 305 * 6 = 305 * 6 = 30"
# assert beginnerExercises.recusion(5, 6, "True") == "5 + 6 = 115 + 6 = 115 + 6 = 115 + 6 = 115 + 6 = 115 + 6 = 115 + 6 = 115 + 6 = 115 + 6 = 115 + 6 = 11"
# assert beginnerExercises.recusion(-5, 6, "True") == "-5 + 6 = 1-5 + 6 = 1-5 + 6 = 1-5 + 6 = 1-5 + 6 = 1-5 + 6 = 1-5 + 6 = 1-5 + 6 = 1-5 + 6 = 1-5 + 6 = 1"
# assert beginnerExercises.recusion(5, 0, "True") == "5555555555"
# assert beginnerExercises.recusion(0, 6, "False") == "6666666666"
# assert beginnerExercises.recusion(0, 0, "False") == "0000000000"


# # lists
# assert beginnerExercises.lists(1, 2, 3, 4, 5, 10, 9, 8, 7, 6) == 1
# assert beginnerExercises.lists(-9, 2, 3, 4, 5, 10, 9, 8, 7, 6) == -9

# recursionlists
# assert beginnerExercises.recursionLists(1, 2, 3, 4, 5, 10, 9, 8, 7, 6) == "1, 2, 3, 4, 5, 10, 9, 8, 7, 6"
# assert beginnerExercises.recursionLists(-9, 2, 3, 4, 5, 10, 9, 8, 7, 6) == "-9, 2, 3, 4, 5, 10, 9, 8, 7, 6"

# recursionlists
assert beginnerExercises.recursionLists1() == [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 100]
#assert beginnerExercises.recursionLists1(-9, 2, 3, 4, 5, 10, 9, 8, 7, 6) == "-9, 2, 3, 4, 5, 10, 9, 8, 7, 6"
