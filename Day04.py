from AoC.Resource import Resource
from AoC import Display
from AoC import Puzzle
import numpy as np
import re

class Day04(Puzzle.Puzzle):
    passports = []
    PassportValidity = []

    def PrepareData(self):
        self.data = self.Resource.Get().replace("\n\n", ";").replace("\n", " ").replace(";", "\n").split("\n")
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
                try:
                    match1, match2 = re.compile("([0-9]+)(in|cm)").findall(p["hgt"])[0]
                    if ((match2 == "cm" and 150 <= int(match1) <= 193) or (match2 == "in" and 59 <= int(match1) <= 76)):
                        p["hgt"] = True
                    else:
                        p["hgt"] = False
                except Exception:
                    p["hgt"] = False
                ValidPasswords += 1 if list(p.values()).count(False) == 0 else 0

        return(ValidPasswords)

Display.DisplayAnswers(Day04(Resource(4)))