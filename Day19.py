from AoC import Utils, Puzzle, Resource
import re

class Day19(Puzzle.Puzzle):
    rules = {}
    messages = None

    def ParseRule(self, body):
        body = body.strip('"')
        if "|" in body:
            ruleBody, ruleType = (list(map(lambda x: x.split(" "),body.split(" | "))), "OR")
        elif body in "ab":
            ruleBody, ruleType = (body, "BASE")
        else:
            ruleBody, ruleType = (body.split(" "), "FOLLOW")

        return {"type": ruleType, "v": ruleBody}

    def PrepareData(self):
        rules, messages = self.Resource.Get().split("\n\n")
        self.messages = [x.strip() for x in messages.split("\n")]
        for rule in rules.split("\n"):
            key, body = rule.split(": ")
            self.rules[key] = self.ParseRule(body)

    def CreateRegEx(self, key, part=1, elevenDepth = 0, eightDepth = 0):
        return "^" + self.CreateRegExInner(key, part, elevenDepth, eightDepth) + "$"

    def CreateRegExInner(self, key, part=1, elevenDepth = 0, eightDepth = 0):
        rule = self.rules[key]

        if part == 2 and key in ["11", "8"]:
            elevenDepth += 1 if key == "11" else 0
            eightDepth += 1 if key == "8" else 0
            if key == "11" and elevenDepth > 10:
                rule = self.ParseRule("42 31")
            elif key == "8" and eightDepth > 10:
                rule = self.ParseRule("42")
            print(elevenDepth, eightDepth)

        if rule["type"] == "BASE":
            return rule["v"]
        elif rule["type"] == "FOLLOW":
            return "".join(list(map(lambda k: self.CreateRegExInner(k, part, elevenDepth, eightDepth), rule["v"])))
        elif rule["type"] == "OR":
            l = "".join(list(map(lambda k: self.CreateRegExInner(k, part, elevenDepth, eightDepth), rule["v"][0])))
            r = "".join(list(map(lambda k: self.CreateRegExInner(k, part, elevenDepth, eightDepth), rule["v"][1])))
            return f"(?:{l}|{r})"


    def SolvePartOne(self):
        regex = re.compile(self.CreateRegEx("0"))
        return sum([regex.match(x) is not None for x in self.messages])

    def SolvePartTwo(self):
        self.rules["8"] = self.ParseRule("42 | 42 8")
        self.rules["11"] = self.ParseRule("42 31 | 42 11 31")
        regex = re.compile(self.CreateRegEx("0", 2))
        return sum([regex.match(x) is not None for x in self.messages])

if __name__ == '__main__':
    Utils.ShowAnswers(Day19(Resource.Resource(19)))