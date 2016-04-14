import unittest
from src.row import Row
from src.relation import Relation


# pylint: disable=R0904
class RowTests(unittest.TestCase):
  def test_is_present(self):
    relation = self.get_standard_relation()

    self.assertTrue(relation.is_present_key(Row(1, ['1', 2, 'a'])),
                    "key 1 is not present in map")
    self.assertTrue(relation.is_present_key(Row('a', [123])),
                    "key a is not present in map")
    self.assertFalse(relation.is_present_key(Row(3, [123])),
                     "key 3 should not be present in map")

  def test_add_row(self):
    relation = self.get_standard_relation()
    relation.add_row(Row(1, ['1', 2, 'a']))
    self.assertEquals(3, len(relation.input_map.get(1)),
                      "size of values having key 1 should be 3")

  def get_standard_relation(self):
    tmp = dict()
    relation = Relation(tmp)

    row1 = Row(2, ['1', 2, 'a'])
    row2 = Row(1, ['1', 2, 'a'])
    row3 = Row(1, ['1', 'a', 'b'])
    row4 = Row('a', [123])

    relation.add_row(row1)
    relation.add_row(row2)
    relation.add_row(row3)
    relation.add_row(row4)
    return relation
