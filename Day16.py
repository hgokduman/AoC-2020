from AoC import Utils, Puzzle, Resource
import operator
from functools import reduce

class Day16(Puzzle.Puzzle):
    rules = {}
    ticket = []
    nearby_tickets = []
    invalidated = []

    def PrepareData(self):
        def parseTicket(ticket):
            return tuple(int(x) for x in ticket.split(","))
        self.data = self.Resource.Get().split("\n\n")
        self.rules = {a:b for a,b in [x.split(": ") for x in self.data[0].split("\n")]}
        self.ticket = parseTicket(self.data[1].split("\n")[1])
        self.nearby_tickets = list(map(parseTicket, self.data[2].split("\n")[1:]))
        for x,y in self.rules.items():
            ranges = y.split(" or ")
            rule = []
            for r in ranges:
                low, high = r.split("-")
                rule += list(range(int(low), int(high)+1))
            self.rules[x] = rule

    def SolvePartOne(self):
        invalidNumbers = []
        for t in self.nearby_tickets:
            invalid = False
            for v in t:
                if sum([v in rule_range for rule_range in self.rules.values()]) == 0:
                    invalid = True
                    invalidNumbers.append(v)
                    self.invalidated.append(t)
                    break
        return sum(invalidNumbers)

    def SolvePartTwo(self):
        not_invalidated = [x for x in self.nearby_tickets if x not in self.invalidated]
        num_values = len(not_invalidated[0])
        col2rule = {x:[] for x in range(num_values)}
        cols = [[cp[c] for cp in not_invalidated] for c in range(num_values)]
        for pos, c in enumerate(cols):
            for rule,values in self.rules.items():
                if sum([x in values for x in c]) == len(not_invalidated):
                    col2rule[pos].append(rule)
        
        final_allocation = {}
        while len(col2rule) > 0:
            one = [(x,y[0]) for x,y in col2rule.items() if len(y) == 1]
            if len(one) > 0:
                for x,y in one:
                    final_allocation[y] = x
                    del col2rule[x]
                    for a,b in col2rule.items():
                        if y in b:
                            col2rule[a].remove(y)
       
        return reduce(operator.mul, [self.ticket[y] for x,y in final_allocation.items() if "departure" in x])
if __name__ == '__main__':
    Utils.ShowAnswers(Day16(Resource.Resource(16)))