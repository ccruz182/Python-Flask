def addition_simplified(*args):
  return sum(args)

addition_simplified(1, 2, 3, 4, 5)

def what_are_kwargs(**kwargs):
    print(kwargs)

what_are_kwargs(name="Cesar", age=21)
