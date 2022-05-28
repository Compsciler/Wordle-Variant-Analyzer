from enum import Enum
from collections import Counter
from numpy import base_repr

DIGIT_COUNT = 5
BASE_SYSTEM = 10
NUMBER_COUNT = BASE_SYSTEM**DIGIT_COUNT

# TODO: Add option to set probability of word being solution

def get_solutions():
  return get_valid_guesses()

def get_valid_guesses():
  return [f"{base_repr(n, BASE_SYSTEM).zfill(DIGIT_COUNT)}" for n in range(NUMBER_COUNT)]
  # return [f"{n:0{DIGIT_COUNT}d}" for n in range(NUMBER_COUNT)]

def get_valid_guesses_hard_mode():
  pass

class CellStatus(Enum):
  GREEN = 0
  YELLOW = 1
  GRAY = 2

class HigherLowerStatus(Enum):
  EQUAL = 0
  HIGHER = 1
  LOWER = 2

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
  
  word_num, sol_num = int(word), int(solution)
  higher_lower_status = HigherLowerStatus.EQUAL
  if word_num < sol_num:
    higher_lower_status = HigherLowerStatus.HIGHER
  elif word_num > sol_num:
    higher_lower_status = HigherLowerStatus.LOWER
  word_statuses.append(higher_lower_status)
  return tuple(word_statuses)
