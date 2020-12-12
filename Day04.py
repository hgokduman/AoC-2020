from AoC import Utils, Puzzle, Resource
import re

class Day04(Puzzle.Puzzle):
    passports = []
    PassportValidity = []

    def PrepareData(self):
        self.data = self.Resource.Get().replace("\n\n", ";").replace("\n", " ").split(";")
        self.passports = list(map(lambda p: {x[0]:x[1] for x in [f.split(":") for f in p.strip().split(" ")]}, self.data))   

    def SolvePartOne(self):
        RequiredFields = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
        self.PassportValidity = [sum([x in p for x in RequiredFields])==len(RequiredFields) for p in self.passports]
        return sum(self.PassportValidity)

    def SolvePartTwo(self):
        ValidPasswords = 0
        for p, v in zip(self.passports, self.PassportValidity):
            if v:
                p["byr"] = int(p["byr"]) in range(1920, 2003)
                p["iyr"] = int(p["iyr"]) in range(2010, 2021)
                p["eyr"] = int(p["eyr"]) in range(2020, 2031)
                p["ecl"] = p["ecl"] in ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
                p["pid"] = re.match("^[0-9]{9}$", p["pid"]) is not None
                p["hcl"] = re.match("^#[0-9a-f]{6}$", p["hcl"]) is not None
                p["hgt"] = False if re.match("([0-9]+)(in|cm)", p["hgt"]) is None else (int(p["hgt"][:-2]), p["hgt"][-2:])
                p["hgt"] = False if not p["hgt"] else (p["hgt"][1] == "cm" and 150 <= p["hgt"][0] <= 193) or (p["hgt"][1] == "in" and 59 <= p["hgt"][0] <= 76)
                ValidPasswords += 1 if list(p.values()).count(False) == 0 else 0

        return(ValidPasswords)

if __name__ == '__main__':
    Utils.ShowAnswers(Day04(Resource.Resource(4)))