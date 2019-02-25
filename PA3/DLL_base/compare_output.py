
f1 = open("out.txt", encoding="utf8")
f2 = open("expected_out.txt", encoding="utf8")
f3 = open("out_diff.txt", "w+")

no_difference = True
line_number = 1
for line1, line2 in zip(f1, f2):
    if line1.strip() != line2.strip():
        print("Difference in line " + str(line_number))
        f3.write("Difference in line " + str(line_number) + "\n")
        no_difference = False
    line_number += 1

if no_difference:
    print("Files are the same!")

f1.close()
f2.close()
f3.close()
