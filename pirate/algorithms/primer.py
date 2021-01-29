
def variables():
    t = 4
    s = t
    t = 10
    print(s)
    print(t)

    i = ['a', 'c', 'b', 'g']
    print(sorted(i))
    print(max(i))
    print(min(i))

    print(abs(-4))

    print(max([2,3,4,5,6, 5000]))   # array
    print(max(2, 3, 4, 5, 6, 5000)) # tuple
    print(max(i))

    for j in range(1,10):
      print(j)

def parameters():

    def changeme(d):
        d[0] = 3
        d[1] = 3
        d[2] = 3

    d = [1,2,3]
    print(d)
    changeme(d)
    print(d)

def builtins():
    """
    abs
    max
    range

     print
     input
     open

     ord
     chr

     abs
     divmod
     pow
     round
     sum

     max
     min
     range

     len

     sorted

     reversed
     all
     any

     iter
     next




    """

    print(1,2,3,sep=":")

def exceptions():
    i = [1,2]
    try:
      i[3] = 4
    except Exception as e:
        print("oops!")
    """
    Class	Description
    Exception	A base class for most error types
    AttributeError	Raised by syntax obj.foo, if obj has no member named foo
    EOFError	Raised if “end of file” reached for console or file input
    IOError	Raised upon failure of I/O operation (e.g., opening file)
    IndexError	Raised if index to sequence is out of bounds
    KeyError	Raised if nonexistent key requested for set or dictionary
    KeyboardInterrupt	Raised if user types ctrl-C while program is executing
    NameError	Raised if nonexistent identifier used
    Stoplteration	Raised by next(iterator) if no element; see Section 1.8
    TypeError	Raised when wrong type of parameter is sent to a function
    ValueError	Raised when parameter has invalid value (e.g., sqrt(−5))
    ZeroDivisionError	Raised when any division operator used with 0 as divisor

    """

def iterators():
    data  = [1,2,3]
    i = iter(data)
    while True:
        try:
          print(next(i))
        except StopIteration:
            return
def dictionaries():
    i = {"name": "Joe", "age":32, "height": 32}
    print(type(i))
    print(i)
    i.keys()
    i.values()

    t = tuple(i.keys())
    print(t)
    t = list(i.values())
    print(t)
    t = set(i.values())
    print(t)

    name = "charles david harris"
    name = name.replace(' ','')
    print(sorted(set(list(name))))
    # how can I reverse this?

def generators():
    def factors(n):
        results = []
        for k in range(1, n+1):
            if n % k == 0:
              results.append(k)
        return results

    def yeild_factors(n):
        for k in range(1,n+1):
            if n % k == 0:
                yield k

    def isprime(n):
        return len(factors(n)) == 2

    #print(factors(16))
   # print(isprime(11))
    f = yeild_factors(32)
    for i in f:
        print(i)
    pass

def yeilding():
    def a():
        for i in range(1,11):
            yield(i)
    ayield = a()

    # one time use
    #print(list(ayield))

    #print(next(ayield))
    #print(next(ayield))

    #for i in ayield:
    #  print(i)
    def even_numbers(n):
        for x in range(n):
            if (x % 2 == 0):
                yield x

    num = even_numbers(10)
    print(type(num))
    #print(list(num))

def comprehension():
  """
   [ expression for value in iterable if condition ]

   result = []
   for value in iterable:
     if condition:
       result.append(expression)
  """
  squares = []
  for k in range(1, 17):
    squares.append(k*k)

  # list comprehension
  squares = [ k * k for k in range(1, 17)]

  def factors(n):
    return [k for k in range(1, n + 1) if n % k == 0]

  def isprime(n):
      return len(factors(n)) == 2

  # print(factors(16))
  # print(isprime(17))

  """
  [ k*k for k in range(l, n+1) ] 	list comprehension
  { k*k for k in range(l, n+1) } 	set comprehension
  ( k*k for k in range(l, n+1) ) 	generator comprehension  ( like yield )
  { k : k*k for k in range(l, n+1) } 	dictionary comprehension
  """
  kgen = ( k for k in "onceuponatimethereweretwobears")
  # print(set(list(kgen)))
  import string

  letters = [ k for k in string.ascii_lowercase ]
  print(letters)


  box = [[x,y] for x in range(1,11) for y in range(1,11)]
  print(len(box))

if __name__ == "__main__":
    comprehension()