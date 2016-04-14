import unittest
import src.create_relations as create_relations
import src.sample as Sample


# pylint: disable=R0904
class SampleTest(unittest.TestCase):
  def test_sample(self):
    counts1 = {1: 100, 2: 10, 3: 10}
    counts2 = {1: 100, 2: 10, 3: 1}

    [relation1, relation2] = create_relations.create_2_relations(counts1,
                                                                 counts2)

    # sample = Sample()
    [is_sample1, sample1, is_sample2, sample2] = Sample.sample(relation1,
                                                               relation2,
                                                               0.1)

    self.assertFalse(is_sample1.get(1),
                     "relation1 key1 should not be sampled")
    self.assertFalse(is_sample1.get(2),
                     "relation1 key 2 should not be sampled")
    self.assertTrue(is_sample1.get(3), "relation1 key 3 should be sampled")

    self.assertFalse(is_sample2.get(1),
                     "relation2 key1 should not be sampled")
    self.assertFalse(is_sample2.get(2),
                     "relation2 key2 should not be sampled")
    self.assertFalse(is_sample2.get(3),
                     "relation2 key3 should not be sampled")

    self.assertEqual(len(sample1.input_map.get(1)), 100)
    self.assertEqual(len(sample1.input_map.get(2)), 10)
    self.assertEqual(len(sample1.input_map.get(3)), 1)

    self.assertEqual(len(sample2.input_map.get(1)), 100)
    self.assertEqual(len(sample2.input_map.get(2)), 10)
    self.assertEqual(len(sample2.input_map.get(3)), 1)
