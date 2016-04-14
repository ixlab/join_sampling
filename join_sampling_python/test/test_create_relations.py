import unittest
import src.create_relations as CreateRelations


# pylint: disable=R0904
class CreateRelationsTest(unittest.TestCase):
  def test_create_2_relations(self):
    counts1 = {1: 100, 2: 10, 3: 10}
    counts2 = {1: 100, 2: 10, 3: 1}

    [relation1, relation2] = CreateRelations.create_2_relations(counts1,
                                                                counts2)

    self.assertEqual(100, len(relation1.input_map.get(1)),
                     "relation1 key 1 should have 100 values")
    self.assertEqual(1, len(relation2.input_map.get(3)),
                     "relation1 key 1 should have 100 values")
