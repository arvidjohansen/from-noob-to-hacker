def validate_email(email):
    if '@' in email:
        split_email = email.split('@')
        if len(split_email) == 2:
            domain_part = split_email[1]
            if '.' in domain_part:
                return True
    return False

# Test the function
print(validate_email("test@example.com"))  # Returns: True
print(validate_email("test@.com"))  # Returns: True
print(validate_email("test.com"))  # Returns: False