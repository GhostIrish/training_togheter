# property
# com ele é possível criar atributos gerenciados em suas classes
# é uma forma de criar um atributo que pode ser acessado de maneira mais simples
# ex:
class Foo:
  def __init__(self, x=None):
    self._x = x

  @property
  def x(self):
    return self._x or 0

  @x.setter
  def x(self, value):
    _x = self._x or 0
    _value = value or 0
    self._x = _x + _value

  @x.deleter
  def x(self):
    self._x = -1

# ex de uso:
foo = Foo(10)
print(foo.x)
foo.x = 5
print(foo.x)
del foo.x
print(foo.x)
