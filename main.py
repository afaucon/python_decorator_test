
# def greet(name):
#     return "hello "+name
#
# greet_someone = greet
# print(greet_someone("John"))


# def greet(name):
#     def get_message():
#         return "Hello "
#     result = get_message()+name
#     return result
#
# print(greet("John"))


# def greet(name):
#     return "Hello " + name
#
# def call_func(func):
#     other_name = "John"
#     return func(other_name)
#
# print(call_func(greet))


# def compose_greet_func():
#     def get_message():
#         return "Hello John"
#     return get_message
#
# greet = compose_greet_func()
# print(greet())


# def compose_greet_func(name):
#     def get_message():
#         return "Hello "+name
#     return get_message
#
# greet = compose_greet_func("John")
# print(greet())


# def get_text(name):
#     return "lorem ipsum, {0} dolor sit amet".format(name)
#
# def p_decorate(func):
#     def func_wrapper(name):
#         return "<p>{0}</p>".format(func(name))
#     return func_wrapper
#
# my_get_text = p_decorate(get_text)
#
# print(my_get_text("John"))






def p_decorate(func):
    def func_wrapper(name):
        return "<p>{0}</p>".format(func(name))
    return func_wrapper

# Use this:
@p_decorate
def get_text(name):
    return "lorem ipsum, {0} dolor sit amet".format(name)

# Or this:
# def get_text(name):
#     return "lorem ipsum, {0} dolor sit amet".format(name)
# get_text = p_decorate(get_text)

print(get_text("John"))



