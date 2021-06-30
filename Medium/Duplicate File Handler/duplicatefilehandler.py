import sys
import os

if len(sys.argv) == 1:
    print("Directory is not specified")
else:
    for root, dirs, files in os.walk(sys.argv[1]):
        for name in files:
            print(os.path.join(root, name))
