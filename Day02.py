import AoC

entries = AoC.GetListFromInput(2)

def Day02(part=1):
    validPasswords = 0
    for line in entries:
        policy, password = line.split(": ")
        policyNumbers, letter = policy.split(" ")
        policyDigits = [int(x) for x in policyNumbers.split("-")]
        if part == 1:
            policyMin, policyMax = policyDigits
            if policyMin <= password.count(letter) <= policyMax:
                validPasswords += 1
        elif part == 2:
            PositionOne, PositionTwo = [int(x)-1 for x in policyDigits]
            if (password[PositionOne] == letter) ^ (password[PositionTwo] == letter):
                validPasswords += 1
    return(validPasswords)

AoC.ShowAnswers(Day02, [1, 2])