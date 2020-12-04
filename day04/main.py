import re

with open('input.txt', 'r') as reader:
    in_data = [x for x in reader.read().split('\n\n')]


def valid_byd(passport):

    res = re.search(r'byr:(\d{4})', passport)
    return res is not None and 1920 <= int(res.group(1)) <= 2002


def valid_iyr(passport):

    res = re.search(r'iyr:(\d{4})', passport)
    return res is not None and 2010 <= int(res.group(1)) <= 2020


def valid_eyr(passport):

    res = re.search(r'eyr:(\d{4})', passport)
    return res is not None and 2020 <= int(res.group(1)) <= 2030


def valid_hgt(passport):

    res = re.search(r'hgt:(\d+)(cm|in)', passport)
    return res is not None \
           and (150 <= int(res.group(1)) <= 193 and res.group(2) == 'cm'
                or 59 <= int(res.group(1)) <= 76 and res.group(2) == 'in')


def valid_hcl(passport):

    res = re.search(r'hcl:#([\d|a-f]{6})', passport)
    return res is not None


def valid_ecl(passport):

    res = re.search(r'ecl:(amb|blu|brn|gry|grn|hzl|oth)', passport)
    return res is not None


def valid_pid(passport):

    res = re.search(r'pid:\d{9}', passport)
    return res is not None


def valid(passport):

    return valid_byd(passport) \
           and valid_iyr(passport) \
           and valid_eyr(passport) \
           and valid_hgt(passport) \
           and valid_hcl(passport) \
           and valid_ecl(passport) \
           and valid_pid(passport)


ans = [x.replace('\n', ' ') for x in in_data if valid(x)]
print(len(ans))
