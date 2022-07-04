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
    # print(f"{guess}: {entropy}")
  guess_entropies.sort(key=lambda guess_entropy: guess_entropy[1], reverse=True)
  return guess_entropies

def get_entropy(word):
  word_status_freqs = get_word_status_freqs(word)
  solutions = get_solutions()
  
  entropy = 0
  for word_status, word_status_freq in word_status_freqs.items():
    prob_status = word_status_freq / len(solutions)
    bits_of_info = log2(1 / prob_status)
    entropy += prob_status * bits_of_info
  return entropy

def get_word_status_freqs(word):
  word_status_freqs = defaultdict(int)
  solutions = get_solutions()
  for solution in solutions:
    word_status = get_word_statuses(word, solution)
    word_status_freqs[word_status] += 1
  return word_status_freqs

def get_word_status_list(word):
  word_status_list = defaultdict(list[str])
  solutions = get_solutions()
  for solution in solutions:
    word_status = get_word_statuses(word, solution)
    word_status_list[word_status].append(solution)
  return word_status_list

def print_word_statuses(word_statuses, sort_by_status=True):
  if sort_by_status:
    sort_key = lambda kv: kv[0]
  else:
    sort_key = lambda kv: kv[1] if type(kv[1]) == int else len(kv[1])
  sorted_word_status_items = sorted(word_statuses.items(), key=sort_key, reverse=True)
  for word_status, word_status_val in sorted_word_status_items:
    print(''.join([str(status) for status in word_status]), ' ', word_status_val)

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

# guess_entropies = get_guess_entropies()
# guess_entropies_file = 'entropies.txt'
# with open(guess_entropies_file, 'w') as out:
#   print(*guess_entropies, sep='\n', file=out)

# print_word_statuses(get_word_status_freqs('50126'))
# print(get_entropy('50126'))
print_word_statuses(get_word_status_freqs('54623'), sort_by_status=False)
print(get_entropy('54623'))
print()
print_word_statuses(get_word_status_freqs('50123'), sort_by_status=False)
print(get_entropy('50123'))
# print(get_entropy('44556'))
# print(get_entropy('50000'))
# print(get_entropy('52346'))
# print(get_entropy('45678'))
# print(get_entropy('55555'))
# print(get_entropy('00000'))
# print(get_entropy('99999'))
