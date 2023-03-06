import math

from IArray import IArray


def testMethod(arrayInput, testingMethodNumFunc, maxNumCalls, step, minNumCalls: int = -1, suffix: str = ''):

    maxD = int(math.log10(maxNumCalls)) + 1
    stepD = int(math.log10(step))
    startD = 1

    if minNumCalls > 0:
        startD = int(math.log10(minNumCalls))

    num = int(math.pow(10, startD))
    for digits in range(startD, maxD, stepD):
        if callable(arrayInput):
            array = arrayInput()
        else:
            array = arrayInput

        timeElapsed, className, methodStr = testingMethodNumFunc(array, num)

        print(className, ':', methodStr.upper(), suffix, ':', num, '->', timeElapsed)

        num *= step
