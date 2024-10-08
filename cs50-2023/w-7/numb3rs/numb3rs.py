import re
import sys

def main():
    print(validate(input("IPv4 Address: ")))

def validate(ip):
    if valid := re.search(r"^(\d+)\.(\d+)\.(\d+)\.(\d+)$" , ip):
        for i in valid.groups():
            if not 0 <= int(i) <= 255:
                return False
        return True
    else:
        return False

if __name__ == "__main__":
    main()