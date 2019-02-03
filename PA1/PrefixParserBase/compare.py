import sys
import os
os.chdir(os.path.dirname(sys.argv[0]))

with open("expected_output.txt", encoding='utf8') as fpt1:
    with open("comparison.txt", encoding='utf16') as fpt2:
        file2 = list()
        for line in fpt2:
            file2.append(line)
        for i, line in enumerate(fpt1):
            other_line = file2[i]
            assert line.strip() == other_line.strip()
