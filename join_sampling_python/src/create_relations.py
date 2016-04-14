from random import randint

from src.relation import Relation
from src.row import Row


def create_2_relations(counts1, counts2):
  relation1 = create_relation(counts1)
  relation2 = create_relation(counts2)
  return [relation1, relation2]


def create_relation(counts):
  dict1 = dict()
  for key in counts:
    rows = create_random_rows(key, counts.get(key))
    dict1[key] = rows
  return Relation(dict1)


def create_random_rows(key, count):
  rows = []
  for _ in range(count):
    row = create_random_row(key)
    rows.append(row)
  return rows


def create_random_row(key):
  """
  Create a random row of LENGTH 3 with the first item key and the 2nd and
  3rd items ints from 1 to 100
  """
  row = [key]
  for _ in range(2):
    random_val = randint(1, 100)
    row.append(random_val)
  return Row(row[0], row[1:])
