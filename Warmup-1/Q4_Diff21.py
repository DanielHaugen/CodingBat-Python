"""
    Given an int n, return the absolute difference between n and 21, 
    except return double the absolute difference if n is over 21.

    diff21(19) → 2
    diff21(10) → 11
    diff21(21) → 0
"""

def diff21(n):
  return (21-n, (n-21)*2)[n>21] 
  #Ternary Operator (if_test_is_false, if_test_is_true)[test_condition]