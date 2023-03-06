import time

from IArray import IArray

def fillArray(array: IArray, numCalls: int, instanceFunc):
    countdown = numCalls

    while countdown > 0:
        array.put(instanceFunc())
        countdown -= 1

    return array


def testSizeMethod(array: IArray, numCalls: int) -> float:
    start = time.time()

    countdown = numCalls

    while countdown > 0:
        array.size()
        countdown -= 1

    return time.time() - start, array.__class__.__name__, 'A.size()'


def testPutMethod(array: IArray, numCalls: int, instanceFunc) -> float:
    start = time.time()

    countdown = numCalls

    while countdown > 0:
        array.put(instanceFunc())
        countdown -= 1

    return time.time() - start, array.__class__.__name__, 'A.put(item)'


def testAddMethod(array: IArray, numCalls: int, instanceFunc) -> float:
    start = time.time()

    array.add(instanceFunc(), 0)

    count = 1
    j = 1

    while count < numCalls:
        array.add(instanceFunc(), count - int(j))
        count += 1
        j += 0.5

    return time.time() - start, array.__class__.__name__, 'A.add(item, i)'


def _testGetMethod_static(array: IArray, numCalls: int, index: int = 10) -> float:
    start = time.time()

    countdown = numCalls

    while countdown > 0:
        array.get(index)
        countdown -= 1

    return time.time() - start, array.__class__.__name__, 'A.get({i})'.format(i=index)


def _testGetMethod_stepcicle(array: IArray, numCalls: int) -> float:
    size1 = array.size() - 1
    index = int(size1 * 0.15)
    step = int(size1 * 0.22)

    start = time.time()

    countdown = numCalls

    while countdown > 0:
        array.get(index)
        
        index += step
        if index > size1: index -= size1

        countdown -= 1

    return time.time() - start, array.__class__.__name__, 'A.get(i) STEPCICLE'


def testGetMethod(array: IArray, numCalls: int, indexMode: int = 0) -> float:

    if indexMode == 0:
        return _testGetMethod_static(array, numCalls)

    if indexMode == 1:
        return _testGetMethod_stepcicle(array, numCalls)


def _testRemoveMethod_static(array: IArray, numCalls: int, index: int = 9) -> float:
    start = time.time()

    countdown = numCalls

    while countdown > 0:
        array.remove(index)
        countdown -= 1

    return time.time() - start, array.__class__.__name__, 'A.remove(i)'


def testRemoveMethod(array: IArray, numCalls: int, indexMode: int = 0) -> float:

    #if indexMode == 0:
    return _testRemoveMethod_static(array, numCalls)

    # if indexMode == 1:
        # return _testRemoveMethod_stepcicle(array, numCalls)


