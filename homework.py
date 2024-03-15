#1
def set_helper(lst):
  return set(lst)


#2
def frozenset_helper(lst):
  return frozenset(lst)

#3
def merge_and_typeset(set1, set2):
  merged_set = set1 | set2
  return type(merged_set)


#4
import hashlib

def hash_password(name, password):
  hashed_password = hashlib.sha256(password.encode()).hexdigest()
  return (name, hashed_password)

