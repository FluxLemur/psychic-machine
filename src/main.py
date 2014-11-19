import os
from textLearner import TextLearner

DATA_DIR = '../data/'

dat = open(os.path.join(DATA_DIR, 'simple.txt'))
simpleLearner = TextLearner('test data')
long_line = ''
for line in dat:
    long_line += line

simpleLearner.learn(long_line)

#simpleLearner.print_mat()
print simpleLearner.write(50)
