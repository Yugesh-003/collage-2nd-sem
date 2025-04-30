#Where string will start with a specific number (For eg: 8)

import re
def check(s):
    pattern = "^8"
    if re.match(pattern, s):
        print("Valid")
    else:
        print("Invalid")
check("8yugg")
check("yugg8")
