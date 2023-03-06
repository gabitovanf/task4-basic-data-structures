import sys
import time
import datetime
import inspect
import math
import random

sys.path.append('./array')
sys.path.append('./testers')

from ListArrayAdapter import ListArrayAdapter
from SingleArray import SingleArray
from VectorArray import VectorArray
from FactorArray import FactorArray
from MatrixArray import MatrixArray
from ArrayTests import fillArray, testPutMethod, testAddMethod, testGetMethod, testRemoveMethod, testSizeMethod
from testMethod import testMethod

# # instanceFunctions = [
    # lambda : 10,
    # lambda : 1000
    # lambda : 1000000000,
    # lambda : time.time(),
    # lambda : datetime.datetime.utcnow().strftime("%A, %d. %B %Y %I:%M%p")
# ]


# testMethod(
#     VectorArray(vector=5),
#     lambda array, num: testAddMethod(array, num, lambda : random.randrange(10)),
#     10,
#     10
# )

# array = MatrixArray(vector=3)
# array.put(0)
# array.put(1)
# array.put(2)
# array.put(3)
# array.put(4)
# array.put(5)
# array.put(6)
# print(array)
# array.add(10, 2)
# print(array, array.size())
# array.remove(3)
# print(array, array.size())
# array.remove(3)
# print(array, array.size())
# print(array.get(1), array.get(5))
# print(array.remove(0), array.remove(0), array.remove(0), array.remove(0), array)



# testMethod(
#     MatrixArray(),
#     lambda array, num: testPutMethod(array, num, lambda : 1000),
#     1000000,
#     # 1000000000,
#     10
# )

# testMethod(
#     MatrixArray(), 
#     lambda array, num: testAddMethod(array, num, lambda : 1000),
#     1000000,
#    # 1000000000,
#     10
# )

# GET
# testingArray = fillArray(MatrixArray(), 10000, lambda : random.randrange(100))
# # testingArray = fillArray(ListArrayAdapter(), 1000011, lambda : random.randrange(100))

# # print(testingArray)

# testMethod(
#     testingArray,
#     lambda array, num: testGetMethod(array, num, indexMode = 1),
#     10000000,
#    # 1000000000,
#     10,
#     suffix='(s 10000)'
#     # suffix='(s 1000011)'
# )


# REMOVE
# testingArray = fillArray(MatrixArray(), 10011, lambda : random.randrange(100))

# # print(testingArray)
# testMethod(
#     lambda: testingArray.copy(), 
#     lambda array, num: testRemoveMethod(array, num, indexMode = 0),
#     10000,
#     10,
#     # minNumCalls = 10000,
#     suffix='(s 10011)'
# )

# testingArray = fillArray(MatrixArray(), 100011, lambda : random.randrange(100))

# testMethod(
#     lambda: testingArray.copy(), 
#     lambda array, num: testRemoveMethod(array, num, indexMode = 0),
#     100000,
#     10,
#     # minNumCalls = 10000,
#     suffix='(s 100011)'
# )

# testingArray = fillArray(MatrixArray(), 1000011, lambda : random.randrange(100))

# testMethod(
#     lambda: testingArray.copy(), 
#     lambda array, num: testRemoveMethod(array, num, indexMode = 0),
#     1000000,
#     10
#     # minNumCalls = 10000,
#     suffix='(s 1000011)'
# )


# SIZE
# testingArray = fillArray(MatrixArray(), 10000, lambda : random.randrange(100))
testingArray = fillArray(MatrixArray(), 100011, lambda : random.randrange(100))

# # print(testingArray)

testMethod(
    testingArray,
    lambda array, num: testSizeMethod(array, num),
    1000000,
   # 1000000000,
    10,
    # suffix='(s 10000)'
    suffix='(s 100011)'
)
