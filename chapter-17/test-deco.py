
def p_decorate(func):
   def func_wrapper(*args, **kwargs):
       return "<p>{0}</p>".format(func(*args, **kwargs))
   return func_wrapper

class Person(object):
    def __init__(self):
        self.name = "John"
        self.family = "Doe"

    @p_decorate
    def get_fullname(self):
        return self.name+" "+self.family

my_person = Person()

print my_person.get_fullname()



def tags(tag_name, count):
    def tags_decorator(func):
        def func_wrapper(name):
            return "<{0}>{1}</{0}>".format(tag_name, func(name, str(count)))
        return func_wrapper
    return tags_decorator

@tags("h1", 20)
def get_text(name, freq):
    freq_str = str(freq)
    added_str = "count: " + freq_str
    return "Hello " + name + "\n" +added_str

print get_text("John")