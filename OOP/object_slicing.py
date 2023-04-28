# non-changeable sequence
class Group:
  def __init__(self, group_name, company_name, staff):
    self.group_name = group_name
    self.company_name = company_name
    self.staff = staff
    
  def __reversed__(self):
    pass
    #self.staff.reverse()
  
  def __getitem__(self, item):
    pass
    # return self.staff[item]
    """
    cls = type(self)
    if isinstance(item, slice):
      return cls(group_name = self.group_name, company_name = self.company_name, staff = self.staff[item])
     elif isintance(item, numbers.Integral):
      return clas(group_name = self.group_name, company_name = self.company_name, staff = self.staff[item])
      
    """
  
  def __len__(self):
    pass
  
  def __iter__(self):
    pass
  
  def __contains__(self, item):
    pass
    """
    if item in self.staff:
      return True
     else:
      return False
     """
  
  
# changeable sequence
# add change methods
