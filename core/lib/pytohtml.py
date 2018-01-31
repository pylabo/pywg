class pytohtml():
  def __init__(self,theme):
    self.theme = theme
    self.tree = {}
    self.source = ''
  def new(self,*oid**kwargs):
    self.tree[oid[0]][oid[1]][oid[2]][oid] = {}
    workdict = self.tree[oid[0]][oid[1]][oid[2]][oid]
    workdict['type'] = kwargs['type']
    # WIP
