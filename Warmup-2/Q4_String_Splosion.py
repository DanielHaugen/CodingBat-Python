"""
    Given a non-empty string like "Code" return a string like "CCoCodCode".

    string_splosion('Code') → 'CCoCodCode'
    string_splosion('abc') → 'aababc'
    string_splosion('ab') → 'aab'
"""

def string_splosion(str):
  newStr = ""
  
  for k in range(len(str)):
    newStr += str[:k+1]
  
  return newStr