import re


class NameTooShortError(Exception):
    # raised when name in e-mail is less than 5 symbols
    pass


class MustContainAtSymbolError(Exception):
    # raised when "@" symbol missing in e-mail
    pass


class MoreThanOneAtSymbolError(Exception):
    # raised when more than one "@" symbol in e-mail
    pass


class InvalidNameError(Exception):
    # raised when email name contains anything beside letter, number, underscore or dot
    pass


class InvalidDomainError(Exception):
    # raised when domain is different from listed -> (valid domains are: .com, .bg, .net, .org)
    pass


MIN_LENGTH = 4  # minimum length of the email name
VALID_DOMAINS = (".com", ".bg", ".net", ".org")   # valid domains

pattern_name = r"[\w+\.]+"      # a pattern which checks if the entered email name is correct
pattern_domain = r"\.[a-z]+"    # a pattern that checks if a domain name is valid

email = input("Please enter a valid email: ")

while email != "End":
    try:
        if len(email.split("@")[0]) <= MIN_LENGTH:
            raise NameTooShortError("Name must be at least 5 or more characters!")

        elif "@" not in email:
            raise MustContainAtSymbolError("Email must contain '@' symbol!")

        elif email.count("@") > 1:
            raise MoreThanOneAtSymbolError("Email must contain only one '@' symbol!!")

        elif re.findall(pattern_name, email)[0] != email.split("@")[0]:    # john@social.com -> ["john", "social.com"]
            raise InvalidNameError("Name can only contain letters, numbers, underscores and dots!")

        elif re.findall(pattern_domain, email)[-1] not in VALID_DOMAINS:
            raise InvalidDomainError(f"Domain must be one of the following: {', '.join(VALID_DOMAINS)}")

    except IndexError:      # if no "@" in e-mail, after split only 1 element will be left. So index 1 won't exist
        print("Invalid email!")

    else:   # NOTE: the ELSE will engage, ONLY IF there is no error found in the TRY block
        print(f"Email \"{email}\" is valid!")

    email = input("Please enter a valid email: ")