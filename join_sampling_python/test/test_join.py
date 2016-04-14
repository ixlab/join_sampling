author = "Niranjan Kamat (kamatn@cse.osu.edu)"
copyright = "Copyright (C) 2014 The Ohio State University"
license = "BSD 3-Clause"
version = 0.1

import unittest
import src.create_relations as create_relations
import src.join as Join


# pylint: disable=R0904
class JoinTest(unittest.TestCase):
  def test_final_algo(self):
    """
    Final test for StratJoinOverall
    """
    counts1 = {1: 100, 2: 10, 3: 10}
    counts2 = {1: 100, 2: 10, 3: 1}

    [relation1, relation2] = create_relations.create_2_relations(counts1,
                                                                 counts2)

    join = Join.final_algo(relation1, relation2, 0.1)

    self.assertEqual(len(join.input_map.get(1)), 1000)
    self.assertEqual(len(join.input_map.get(2)), 10)
    self.assertEqual(len(join.input_map.get(3)), 1)
