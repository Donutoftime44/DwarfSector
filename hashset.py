class HashSetB():
  def __init__(self):
    self.array = []
  def add(self, key, value):
    t = Single(key)
    t.value = value
    self.array.append(t)
  def remove(self, key):
    for single in self.array:
      if key == single.key:
        del single
  def get(self, key):
    for single in self.array:
      if key == single.key:
        return single.value
  def set(self, key, val):
    for single in self.array:
      if key == single.key:
        single.value = val


class HashSet():
  def __init__(self):
    self.arrayone = []
    self.arraytwo = []
  def add(self, key, value):
    self.arrayone.append(key)
    self.arraytwo.append(value)
  def remove(self, key, value):
    self.arrayone.remove(key)
    self.arraytwo.remove(value)
  def get(self, key):
    for i in range(0, len(self.arrayone)):
      if key == self.arrayone[i]:
        return self.arraytwo[i]
  def addSingle(self, single):
    self.arrayone.append(single.key)
    self.arraytwo.append(single.value)
  def getAllKeys(self):
    return self.arrayone
  def getAllValues(self):
    return self.arraytwo
  def length(self):
    if len(self.arrayone) == len(self.arraytwo):
      return len(self.arrayone)
    else:
      return 0
  def reverse(self):
    self.arrayone = self.arrayone[::-1]
  def valuesort():
    self.arraytwo = sorted(self.arraytwo)
  def keysort():
    self.arrayone = sorted(self.arrayone)
  
class Single():
  def __init__(self, key):
    self.key = key
    self.value = "null"
  def setvalue(self, value):
    self.value = value
  def toString(self):
    return "" + str(self.key) + ":" + str(self.value)
  def getValue(self):
    return self.value
