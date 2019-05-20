"""
    Given a string, return a new string where "not " has been added to the front. 
    However, if the string already begins with "not", return the string unchanged.

    not_string('candy') → 'not candy'
    not_string('x') → 'not x'
    not_string('not bad') → 'not bad'
"""

def not_string(str):
  return ("not " + str, str)[len(str) >= 3 and str[:3] == "not"]
  
  #Ternary Operator (if_test_is_false, if_test_is_true)[test_condition]