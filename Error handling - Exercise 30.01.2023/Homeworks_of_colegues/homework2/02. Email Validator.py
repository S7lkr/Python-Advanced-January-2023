import re

# 1. Defined classes for different types of exceptions in user email


class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


class MoreThanOneAtSymbolsError(Exception):
    pass


class InvalidNameError(Exception):
    pass


# 2. Defined regex and main constants for user email validation

regex_pattern_name = r'[\w+\.]+'            # Regex output: [name,host]
regex_pattern_domain = r'\.[a-z]+$'         # Regex output: ['.domain']
MIN_CHAR_LENGTH = 4
VALID_DOMAINS = [".com", ".bg", ".net", ".org"]


# 4. While-loop for different email inputs and output for email validity

email = input()                             # Initial user input of email
while email != "End":

    try:                                    # Tries email for valid format
        if email.count("@") > 1:                                                    # Check for multiple '@' symbols
            raise MoreThanOneAtSymbolsError("Email should contain only one @!")

        if len(email.split("@")[0]) <= MIN_CHAR_LENGTH:                             # Check for email length validity
            raise NameTooShortError(f"Name must be more than {MIN_CHAR_LENGTH} characters")

        if len(re.findall(regex_pattern_name, email)[0]) != len(email.split("@")[0]):  # Check for any unwanted symbols
            raise InvalidNameError("Name can only contain numbers, letters, underscores and dots")

        if "@" not in email:                                                        # Check for presense of '@'
            raise MustContainAtSymbolError("Email must contain '@'")

        if re.findall(regex_pattern_domain, email)[-1] not in VALID_DOMAINS:        # Check for valid email domain
            raise InvalidDomainError(f"Domain must be one of the following: {', '.join(VALID_DOMAINS)}")

    except IndexError:                      # Returns error when "try"-clause reached an invalid index from input email
        print("Invalid email")

    else:
        print("Email is valid")

    email = input()                         # User input of email (until "End"-command)
