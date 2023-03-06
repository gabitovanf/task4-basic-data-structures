import sys
import time
import random
import threading

sys.path.append('./queue')
sys.path.append('./array')

from PriorityMatrixQueue import PriorityMatrixQueue
from PriorityArrayQueue import PriorityArrayQueue


def getNewItem(numPriorities: int = 10):
    priority = random.randrange(numPriorities)
    obj = { 'priority': priority, 'random': random.randrange(100), 'message': f'This is an object with priority {priority}'  }

    return priority, obj


def generateItems(queue, period: float = 2):
    while True:
        queue.enqueue(*getNewItem())
        print('ENQUEUE', queue, '\n\n')
        time.sleep(period)

def readItems(queue, period: float = 1):
    while True:
        print('DEQUEUE', queue.dequeue(), '(', queue, ')\n\n')
        time.sleep(period)


# queueInstance = PriorityArrayQueue()
queueInstance = PriorityMatrixQueue()

threading.Thread(target=generateItems, args=(queueInstance, 0.3)).start()
threading.Thread(target=readItems, args=(queueInstance, 1)).start()


