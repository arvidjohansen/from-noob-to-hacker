---
marp: true
---


# Regular Expressions in Python: Email Validation

## Introduction

Regular expressions (regex) are a powerful tool for pattern matching and manipulation in strings. In Python, the `re` module provides support for regular expressions. 

## Step 1: Import the `re` Module

Before we can use regular expressions in Python, we need to import the `re` module. This is done with the following line of code:

```python
import re
```

---

## Step 2: Understand the Basics of Regex

A regular expression is a sequence of characters that forms a search pattern. This pattern can be used with various functions to search, edit, or manipulate text.

Here are some basic regex symbols:

- `.`: Matches any character except newline
- `^`: Matches the start of the string
- `$`: Matches the end of the string
- `*`: Matches 0 or more repetitions
- `+`: Matches 1 or more repetitions
- `{n}`: Matches exactly n repetitions
- `[abc]`: Matches either a, b or c
- `\`: Used to escape special characters


---


## Step 3: Write a Regex for Email Validation

A basic regex pattern for email validation could look like this:

```python
pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
```

---


Here's what this pattern means:

- `^`: Start of the string
- `[a-zA-Z0-9_.+-]+`: Matches 1 or more alphanumeric characters including ., _, +, and -
- `@`: Matches the @ symbol
- `[a-zA-Z0-9-]+`: Matches 1 or more alphanumeric characters including -
- `\.`: Matches the . symbol
- `[a-zA-Z0-9-.]+`: Matches 1 or more alphanumeric characters including . and -
- `$`: End of the string


---


## Step 4: Use the Regex Pattern to Validate an Email Address

We can use the `re.match()` function to check if our regex pattern matches a given string. If the pattern matches, `re.match()` returns a match object. If not, it returns `None`.

Here's an example:


---


```python
import re

def validate_email(email):
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    if re.match(pattern, email):
        return True
    else:
        return False

# Test the function
print(validate_email("test@example.com"))  # Returns: True
print(validate_email("test@.com"))  # Returns: False
```

In this example, `validate_email()` is a function that takes an email address as input and returns `True` if the email address is valid and `False` otherwise.

---

## Common uses (examples)

1. **Alphanumeric Characters**: `^[a-zA-Z0-9]+$` - This pattern matches a string that contains only alphanumeric characters (letters and numbers).

2. **Digits**: `^\d+$` - This pattern matches a string that contains only digits.

3. **Whitespace**: `^\s+$` - This pattern matches a string that contains only whitespace characters.

---


4. **Phone Number**: `^\+?\d{1,4}?[-. ]?\(?(?:\d{1,3}?)\)?[-. ]?\d{1,4}[-. ]?\d{1,9}$` - This pattern matches a string that is a phone number with an optional international dialing code included and allows for spaces, dashes, and dots as separators.

5. **IP Address**: `^(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$` - This pattern matches a string that is a valid IP address.

6. **URL**: `^(http|https|ftp)://[a-zA-Z0-9-]+(\.[a-zA-Z0-9-]+)*(/[a-zA-Z0-9- .?,'/\+&%$#=~_-]*)?$` - This pattern matches a string that is a valid URL.

---


7. **Date in YYYY-MM-DD format**: `^(19|20)\d\d[- /.](0[1-9]|1[012])[- /.](0[1-9]|[12][0-9]|3[01])$` - This pattern matches a string that is a date in the format YYYY-MM-DD.

Remember, these are just basic patterns and might not cover all possible cases. For example, the email regex does not cover all valid email addresses. Always tailor your regex to your specific needs.