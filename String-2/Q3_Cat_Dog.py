"""
    Return True if the string "cat" and "dog" appear the same number of times in the given string.

    cat_dog('catdog') → True
    cat_dog('catcat') → False
    cat_dog('1cat1cadodog') → True
"""

def cat_dog(str):
  cat = 0
  dog = 0
  
  for k in range(len(str)):
    if str[k:k+3] == "dog": dog += 1
    if str[k:k+3] == "cat": cat += 1
  
  return cat==dog