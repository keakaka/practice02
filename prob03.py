# 다음 문자열을 모든 소문자를 대문자로 변환하고, 문자 ',', '.', '\n' 을 없앤 후에 중복 없이 각 단어 출력
# s = """We encourage everyone to contribute to Python. If you still have questions after reviewing the material
# in this guide, then the Python Mentors group is available to help guide new contributors through the process."""

import re

s = """We encourage everyone to contribute to Python. If you still have questions after reviewing the material
in this guide, then the Python Mentors group is available to help guide new contributors through the process."""

s = set(re.sub('[,.\n]', '', s, 0).upper().split(' '))
l = list(s)
l.sort()
for i in l:
    print(i)
