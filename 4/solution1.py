f = open('input.txt', 'r')

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
    passportValid = True
    for section in mandatorySections:
        if (section + ':') not in passport:
            passportValid = False
    if passportValid:
        validPassports += 1
    
print(validPassports)