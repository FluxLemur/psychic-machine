from numpy import *
import string

class TextLearner:
    def __init__(self, author):
        self.author = author
        self.word_mat = zeros((1,1))
        self.word_col = []
        self.word_row = []

    def learn(self, text):
      lastWord = r'\n'
      word = ''
      for w in text.lower().split(' '):
        punc = ''
        word = w.strip()
        if len(word) == 0:
          continue
        if word[-1] in string.punctuation:
          punc = word[-1]
          word = word[:-1]
          self._add_word(word, punc)
          if punc == '.' or punc == '!':
            self._add_word(punc, r'\n')
        self._add_word(lastWord, word)
        lastWord = punc if punc != '' else word

    def _add_word(self, word, nextWord):
      row = self._get_or_make_word(word, 0)
      col = self._get_or_make_word(nextWord, 1)
      self.word_mat[row][col] += 1

    def _get_or_make_word(self, word, ax):
      if ax == 0: #column
        if word not in self.word_col:
          self.word_mat = insert(self.word_mat, -1, 0, axis=0)
          self.word_col.append(word)
          return len(self.word_col)-1
        else:
          return self.word_col.index(word)
      elif ax == 1: #row
        if word not in self.word_row:
          self.word_mat = insert(self.word_mat, -1, 0, axis=1)
          self.word_row.append(word)
          return len(self.word_row)-1
        else:
          return self.word_row.index(word)
      else:
        return -1

    def print_mat(self):
      for i in xrange(len(self.word_mat)-1):
        print '\n"' + self.word_col[i] + '": ',
        for j in xrange(len(self.word_mat[i])):
          if self.word_mat[i][j] != 0:
            print self.word_row[j],

    def get_next(self, word):
      ''' Returns a random next word drawn from a distribution of the related row in word_mat '''
      row = self.word_mat[self.word_col.index(word)] 
      options = [self.word_row[i] for i in where(row > 0)[0]]
      return options[random.randint(len(options))]

    def write(self, length):
        ''' Create a text of given length, similar to the previous work of author '''
        work = ''
        last = r'\n'
        curr = ''
        words = 0
        while words < length:
          curr = self.get_next(last)
          if curr != r'\n':
            if curr not in string.punctuation and words > 0:
              work += ' '
            work += curr
          last = curr
          words += 1
        return work
