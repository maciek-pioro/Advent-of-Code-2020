import re

f = open('input.txt', 'r')

def byrOK(byr: str):
    if not re.search('^[0-9]{4}$', byr):
        return False
    if 1920 <= int(byr) <= 2002:
        return True
    return False


def iyrOK(iyr: str):
    if not re.search('^[0-9]{4}$', iyr):
        return False
    if 2010 <= int(iyr) <= 2020:
        return True
    return False

def eyrOK(eyr: str):
    if not re.search('^[0-9]{4}$', eyr):
        return False
    if 2020 <= int(eyr) <= 2030:
        return True
    return False

def hgtOK(hgt: str):
    search = re.search('^([0-9]+)(cm|in)$', hgt)
    if not search:
        return False
    if search.group(2) == 'cm' and 150 <= int(search.group(1)) <= 193:
            return True
    if search.group(2) == 'in' and 59 <= int(search.group(1)) <= 76:
            return True
    return False

def hclOK(eyr: str):
    if re.search('^#[0-9a-f]{6}$', hcl):
        return True
    return False

def eclOK(ecl: str):
    m = re.search('^(amb|blu|brn|gry|grn|hzl|oth)$', ecl)
    if m:
        return True
    return False

def pidOK(pid: str):
    m = re.search('^[0-9]{9}$', pid)
    if m:
        return True
    return False



section: str = ''
l: str
passports: [str] = []
for l in f:
    if l.strip() == '':
        passports += [section.replace('\n', ' ')]
        section = ''
    section += l
passports += [section.replace('\n', ' ')]
print(passports)
mandatorySections: [str] = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']

validPassports: int = 0
passport: str
for passport in passports:
    print(passport)
    passportValid = False

    byr = None
    iyr = None
    eyr = None
    hgt = None
    hcl = None
    ecl = None
    pid = None


    byrM = re.search(r'byr:(\S+)', passport)
    print(byrM)
    iyrM = re.search(r'iyr:(\S+)', passport)
    eyrM = re.search(r'eyr:(\S+)', passport)
    hgtM = re.search(r'hgt:(\S+)', passport)
    hclM = re.search(r'hcl:(\S+)', passport)
    eclM = re.search(r'ecl:(\S+)', passport)
    pidM = re.search(r'pid:(\S+)', passport)

    if(byrM):
        byr = byrM.group(1)
    if(iyrM):
        iyr = iyrM.group(1)
    if(eyrM):
        eyr = eyrM.group(1)
    if(hgtM):
        hgt = hgtM.group(1)
    if(hclM):
        hcl = hclM.group(1)
    if(eclM):
        ecl = eclM.group(1)
    if(pidM):
        pid = pidM.group(1)

        print(pid)
    if eyr and eyrOK(eyr) and\
        byr and byrOK(byr) and\
        hgt and hgtOK(hgt) and\
        hcl and hclOK(hcl) and\
        iyr and iyrOK(iyr) and\
        ecl and eclOK(ecl) and\
        pid and pidOK(pid):
            passportValid = True

    if passportValid:
        validPassports += 1

print(validPassports)
