
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

if __name__ == "__main__":
    exceptions()