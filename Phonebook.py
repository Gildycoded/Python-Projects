#! python3
import pyperclip, re

# Creaet a regex for phone numbers
phoneRegex = re.compile(r'''
# 415-555-0000, 555-0000, (415) 555-0000, 555-000 ext 12345, ext. 12345, x12345

(
((\d\d\d)|(\(\d\d\d\)))?        # area code (optional)
(\s|-|\.)        #first separator
\d\d\d      # first 3 digits
-            # separator
\d\d\d\d        # last four digits
(((ext(\.)?\s)|x)    
(\d{2,5}))?       #extension (optional)        
)

''', re.VERBOSE)

#: Create a regex for email addresses
emailRegex = re.compile(r'''
[a-zA-Z0-9_.+]+                # name part

@                #@ symbole

[a-zA-Z0-9_.+]+                #domain name part

''', re.VERBOSE)

#TODO: Get the text off the clipboard
text = pyperclip.paste()

#TODO: Extract the email/phone from this text
extractedPhone = phoneRegex.findall(text)
extractedEmail = emailRegex.findall(text)

allPhoneNumbers = []
for phoneNumber in extractedPhone:
    allPhoneNumbers.append(phoneNumber[0])

print(extractedPhone)
print(extractedEmail)
#TODO: Copy the extracted email/phone to clipboard
results = '\n'.join(allPhoneNumbers) + '\n' + '\n'.join(extractedEmail)
pyperclip.copy(results)
