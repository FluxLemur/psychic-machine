import os
from textLearner import TextLearner

DATA_DIR = '../data/'

dat = open(os.path.join(DATA_DIR, 'lewis_carroll.txt'))
simpleLearner = TextLearner('carroll')
long_line = ''
for line in dat:
    long_line += line

simpleLearner.learn(long_line)

print simpleLearner.write(10)
