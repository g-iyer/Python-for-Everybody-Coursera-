import re
test_file_name='regex_sum_42.txt'
real_file_name='regex_sum_309884.txt'
file_name = test_file_name
fh = open(file_name)
for line in fh:
    if line == '':continue
    else:
    nums_in_line = re.findall('[0-9]+',line)
    print nums_in_line
                   