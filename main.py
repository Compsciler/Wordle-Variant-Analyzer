from enum import Enum
from collections import Counter, defaultdict
from math import log2
from numerle import get_solutions, get_valid_guesses, get_word_statuses

def get_guess_entropies():
  guess_entropies = []
  valid_guesses = get_valid_guesses()
  for guess in valid_guesses:
    entropy = get_entropy(guess)
    guess_entropies.append((guess, entropy))
  guess_entropies.sort(key=lambda guess_entropy: guess_entropy[1], reverse=True)
  return guess_entropies

def get_entropy(word):
  word_statuses = defaultdict(int)
  solutions = get_solutions()
  for solution in solutions:
    word_status = get_word_statuses(word, solution)
    word_statuses[word_status] += 1
  
  entropy = 0
  for word_status, word_status_freq in word_statuses.items():
    prob_status = word_status_freq / len(solutions)
    bits_of_info = log2(1 / prob_status)
    entropy += prob_status * bits_of_info
  return entropy

"""
class CellStatus(Enum):
  GREEN = 0
  YELLOW = 1
  GRAY = 2

# TODO: Allow to override in subclass
def get_word_statuses(word, solution):
  word_statuses = [CellStatus.GRAY] * len(word)
  word_letter_freq = Counter(word)
  for i, c_word in enumerate(word):
    c_sol = solution[i]
    if c_word == c_sol:
      word_statuses[i] = CellStatus.GREEN
      word_letter_freq[c_word] -= 1
  for i, c_word in enumerate(word):
    if word_letter_freq[c_word] > 0:
      word_statuses[i] = CellStatus.YELLOW
      word_letter_freq[c_word] -= 1
  return tuple(word_statuses)
"""

guess_entropies = get_guess_entropies()
print(guess_entropies[0])
