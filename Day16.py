from AoC import Utils, Puzzle, Resource
import operator
from functools import reduce
import itertools


class Day16(Puzzle.Puzzle):
    rules = {}
    ticket = []
    nearby_tickets = []
    invalidated = []
    ticket_length = 0

    def PrepareData(self):
        parseTicket = lambda ticket: tuple(int(x) for x in ticket.split(","))
        self.data = self.Resource.Get().split("\n\n")
        self.rules = {a:b for a,b in [x.split(": ") for x in self.data[0].split("\n")]}
        self.ticket = parseTicket(self.data[1].split("\n")[1])
        self.ticket_length = len(self.ticket)
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
        validValues = list(itertools.chain.from_iterable([x for x in self.rules.values()]))

        for t in self.nearby_tickets:
            invalid = False
            if any([v not in validValues for v in t]):
                self.invalidated.append(t)
                invalidNumbers += [v for v in t if v not in validValues]
        
        return sum(invalidNumbers)

    def SolvePartTwo(self):
        not_invalidated = [x for x in self.nearby_tickets if x not in self.invalidated]
        Position2Field = {x:[] for x in range(self.ticket_length)}
        ValuesByPosition = [[cp[c] for cp in not_invalidated] for c in range(self.ticket_length)]
        FinalAllocation = {}        
        
        for pos, c in enumerate(ValuesByPosition):
            for rule,values in self.rules.items():
                if all([x in values for x in c]):
                    Position2Field[pos].append(rule)
        
        while Position2Field != {}:
            pos,field = [(x,y[0]) for x,y in Position2Field.items() if len(y) == 1][0]
            FinalAllocation[field] = pos
            del Position2Field[pos]
            removeElements = [x for x,y in Position2Field.items() if field in y]
            for x in removeElements:
                Position2Field[x].remove(field)
       
        return reduce(operator.mul, [self.ticket[y] for x,y in FinalAllocation.items() if "departure" in x])

if __name__ == '__main__':
    Utils.ShowAnswers(Day16(Resource.Resource(16)))