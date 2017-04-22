nums = "1234567890"
letters = "abcdefghijklmnopqrstuvwxyz"
caps = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
chars = ".?!&#,;:-_*"

def pwchk(pw):
    hasLows = (len([x for x in pw if x in letters])!=0)
    hasCaps = (len([x for x in pw if x in caps])!=0)
    hasNums = (len([x for x in pw if x in nums])!=0)
    return hasLows and hasCaps and hasNums

print pwchk("Abc123")
print pwchk("abc1")
print pwchk("aBc")

def strength(pw):
    lows = len([x for x in pw if x in letters])
    uppers = len([x for x in pw if x in caps])
    digits = len([x for x in pw if x in nums])
    misc = len([x for x in pw if x in chars])
    sum = 0
    if (len(pw) > 8):
        sum = 6
    else:
        sum = len(pw)*0.75
    if (lows >= 3):
        sum += 1
    if (uppers >= 3):
        sum += 1
    if (digits >= 3):
        sum += 1
    if (misc >= 3):
        sum += 1
    return int(float(sum))

print strength("Abc123")
print strength("PASSword123!#&")
