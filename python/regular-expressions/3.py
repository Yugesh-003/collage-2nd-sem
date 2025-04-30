import re

def remove(ip):
    result = re.sub(r'\b0+(\d)', r'\1', ip)
    print("Updated IP:", result)

remove("192.168.001.001")


#pattern = "^[a-zA-Z0-9]*$"  re.search
#pattern = "^8"              re.match
#result = re.sub(r'\b0+(\d)', r'\1', ip)