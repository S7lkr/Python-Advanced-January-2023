# 1) *ARGS -> Arguments:

# ARGS are used when the quantity of parameters is UNKNOWN -> "heyy", [1, 20], 4, "sonny",.....
# Use "*args" to work with RANDOM NUMBER of arguments, packed together. They are commonly used as function parameters.
# REMEMBER: The "*" symbol can PACK and also UNPACK elements!

# def test_func(*args):        # REMEMBER: PACK ALL ELEMENTS into ONE tuple!
#     # print(args)                 # args -> packed into tuple
#     # print(*args, sep=", ")      # *args -> UNPACKED tuple of elements
#     return args
#
#
# # TYPE of elements doesn't matter:
# print(test_func(6, 2, "l", ["a", "b", "c"], {2, 3}, True, (5, 8)))     # -> 7 parameters
# #        int,   str,      list,         set,  bool,  tuple


# lst = ["John", 2, 8, "id"]
# some_name, *info, id_n = lst
# # John,   [2, 8], "id"  -> INFO is a small list of PACKED elements with "*". Here we PACK!
# print(info)     # it will stay packed, and we can work with it as a sub-list of "lst"
# print(*info, sep=", ")  # Here we UNPACK!


# PASSING A FUNC AS A PARAMETER TO ANOTHER FUNC:
# def nums(*numbers):     # PACKED RANDOM NUMBER of parameters -> *args
#     a, b = numbers  # a, b = (1, 2)
#     return a, b     # returns a TUPLE -> (a, b)
#
#
# def show_result(value):             # value = (1, 2);        *value = ((1, 2), ) -> PACKING a tuple into a TUPLE
#     print(*value, sep="; ")         # UNPACKED tuple -> 1; 2
#     print(value)                    # TUPLE -> (1, 2)
#
#
# result_from_nums = nums(1, 2)     # store the result into a variable "result_from_nums"
# print(result_from_nums)
# show_result(result_from_nums)     # "show_result" will receive 1 parameter: the result from "nums" -> a tuple: (1, 2)


# 2) **KWARGS -> Key-worded Arguments:
# We use "**kwargs" to get random number of NAMED elements -> tom=15, NY=city, etc.
# NOTE: NEVER use quotes ("") in values of kwargs: "a"=5 (incorrect), a=5 (correct)

# def func_2(**kwargs):
#     print(kwargs)                                   # returns **kwargs, packed into a DICTIONARY
#     print(*kwargs)   # print(*kwargs.keys())        # returns KEYS
#     print(*kwargs.values())                         # returns VALUES
#     print(*kwargs.items())                          # key, value pairs (tuples)
#     # REMEMBER: You cannot return "**kwargs"
#
#
# func_2(John=33, Olivia=20)