import src.sample as Sample
from src.relation import Relation
from src.row import Row

import numpy.random
from random import shuffle
from random import randint


def final_algo(relation1, relation2, rate):
  """
  Samples and uses the Strat_Join_Overall
  """
  [is_sample1, sample1, is_sample2, sample2] = Sample.sample(relation1,
                                                             relation2,
                                                             rate)
  output = overall_join_new(sample1, sample2, is_sample1, is_sample2, rate)
  return output


def overall_join_new(sample1, sample2, is_sample_1, is_sample_2, rate):
  """
  Implementation of StratJoin_Overall. Based on whether the input is sampled or
   not it chooses the correct join strategy
  """
  output_map = dict()
  for key in sample1.input_map:
    if key in sample2.input_map:
      if is_sample_1.get(key) and is_sample_2.get(key):
        output_map[key] = mini_join(sample1.input_map.get(key),
                                    sample2.input_map.get(key))
      elif not is_sample_1.get(key) and not is_sample_2.get(key):
        output_map[key] = choose_randomly_and_join(
          sample1.input_map.get(key), sample2.input_map.get(key),
          rate)
      elif is_sample_1.get(key) and not is_sample_2.get(key):
        output_map[key] = stratnn(sample1.input_map.get(key),
                                  sample2.input_map.get(key))
      else:
        output_map[key] = stratnn(sample2.input_map.get(key),
                                  sample1.input_map.get(key))
  return Relation(output_map)


def mini_join(stratum1, stratum2):
  shuffle(stratum1)
  shuffle(stratum2)
  joined_stratum = join_strata(stratum1, stratum2)
  return joined_stratum


def join_strata(shuffled_stratum_1, shuffled_stratum_2):
  rows = []
  for i in range(len(shuffled_stratum_1)):
    row = join_tuple(shuffled_stratum_1[i], shuffled_stratum_2[i])
    rows.append(row)
  return rows


def join_tuple(tuple1, tuple2):
  values = tuple1.values
  values.append(tuple2.values)
  row = Row(tuple1.key, values)
  return row


def choose_randomly_and_join(stratum1, stratum2, rate):
  rows = []
  output_size = int(round(len(stratum1) * len(stratum1) * rate))
  for _ in range(output_size):
    rows.append(join_tuple(stratum1[randint(0, len(stratum1) - 1)],
                           stratum2[randint(0, len(stratum2) - 1)]))
  return rows


def stratnn(stratum1, stratum2):
  rows = []
  for i in range(len(stratum1)):
    rows.append(
      join_tuple(stratum1[i], stratum2[randint(0, len(stratum2) - 1)]))
  return rows


def overall_join(sample1, sample2, is_sample_1, is_sample_2, rate):
  final_sample_1 = build_join_time_sample(sample1, sample2, is_sample_1,
                                          is_sample_2, rate)
  final_sample_2 = build_join_time_sample(sample2, sample1, is_sample_2,
                                          is_sample_1, rate)
  output = join(final_sample_1, final_sample_2)
  return output


def build_join_time_sample(sample1, sample2, is_sample_1, is_sample_2, rate):
  output = dict()
  for key in sample1.input_map:
    if key in sample2.input_map:
      sample_stratum1 = sample1.input_map.get(key)
      if not is_sample_1.get(key):
        sample_size = None
        if is_sample_2.get(key):
          sample_size = len(sample2.input_map.get(key))
        else:
          sample_size = len(sample1.input_map.get(key)) * len(
            sample2.input_map.get(key)) * rate
          # pylint: disable=E1101
        sample_stratum1 = numpy.random.choice(sample_stratum1,
                                              sample_size, True)
      output[key] = sample_stratum1
  return Relation(output)


def join(final_sample_1, final_sample_2):
  output_map = dict()
  for key in final_sample_1.input_map:
    stratum1 = final_sample_1.input_map.get(key)
    stratum2 = final_sample_2.input_map.get(key)

    output_map[key] = mini_join(stratum1, stratum2)

  return Relation(output_map)
