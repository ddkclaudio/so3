import sys
import MMU

with open(sys.argv[1]) as f:
    content = f.readlines()
content = [x.strip() for x in content]

print(content)
