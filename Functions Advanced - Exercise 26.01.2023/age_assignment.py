def age_assignment(*args, **kwargs):
    result = []
    for name in args:
        value = kwargs[name[0]]
        result.append(f"{name} is {value} years old.")
    return "\n".join(sorted(result))


print(age_assignment("Amy", "Bill", "Willy", W=36, A=22, B=61))