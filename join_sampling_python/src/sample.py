from src.relation import Relation
import numpy.random


def sample(relation1, relation2, rate):
  """
  Based on whether a stratum should be sampled or not, it performs sampling
  """
  is_sample1 = dict()
  is_sample2 = dict()

  sample_map1 = dict()
  sample_map2 = dict()

  for key in relation1.input_map:
    if key in relation2.input_map:
      stratum1 = relation1.input_map.get(key)
      stratum2 = relation2.input_map.get(key)

      should_sample1 = len(stratum2) * rate < 1
      sample_stratum_1 = None
      if should_sample1:
        #pylint: disable=E1101
        sample_stratum_1 = numpy.random.choice(stratum1,
                                               len(stratum1) *
                                               len(stratum2) *
                                               rate, True)
      else:
        sample_stratum_1 = stratum1

      should_sample2 = len(stratum1) * rate < 1
      sample_stratum_2 = None
      if should_sample2:
        #pylint: disable=E1101
        sample_stratum_2 = numpy.random.choice(stratum2,
                                               len(stratum1) *
                                               len(stratum2) *
                                               rate, True)
      else:
        sample_stratum_2 = stratum2

      is_sample1[key] = should_sample1
      is_sample2[key] = should_sample2
      sample_map1[key] = sample_stratum_1
      sample_map2[key] = sample_stratum_2

  return [is_sample1, Relation(sample_map1), is_sample2,
          Relation(sample_map2)]
