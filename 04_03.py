import re

# Allows [firstname].[lastname]@[e-mail_provider].[top-level domain] or [name]@[e-mail_provider].[top-level domain] formats. 
# Emails can end in 2-4 characters like "fi", "com" ,"info"
patern = "(\w{1,})@(\w{1,}).(\w{2,4})|(\w{1,}).(\w{1,})@(\w{1,}).(\w{2,4})"

user_input = input("Give your email address\n")

is_valid = bool(re.match(patern, user_input))

if is_valid:
    print(user_input + " is a valid email")
else:
    print(user_input + " is not a valid email")