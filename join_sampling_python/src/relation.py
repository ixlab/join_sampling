class Relation(object):
  def __init__(self, input_map):
    self.input_map = input_map

  def is_present_key(self, row):
    return row.key in self.input_map

  def add_row(self, row):
    rows = []
    if row.key in self.input_map:
      rows = self.input_map.get(row.key)
    rows.append(row)
    self.input_map[row.key] = rows
