class Person:
    def __init__(self, bmr_mj) -> None:
        self.bmr = bmr_mj
        self.input = 1
        self.decision = "Stay"

    def threshold(self):
        return self.bmr

        # Productivity of your land. Net energy return?

    def should_i_move(self, productivity):
        if productivity >= self.threshold():
            self.decision = "Stay"
        else:
            self.decision = "Leave"


class Land:
    def __init__(self, productivity) -> None:
        self.productivity = productivity

    def build(self, person):
        self.productivity = self.productivity + person.input

    def extract(self, person):
        if (self.productivity - person.bmr) > 0:
            self.productivity = self.productivity - person.bmr
        else:
            self.productivity = 0


def run_simulation():
    land = Land(90)
    people = [Person(10) for _ in range(10)]
    # make a decision for the next iteration to stay or leave
    for p in people:
        p.should_i_move(land.productivity)
        land.extract(p)

    for p in people:
        land.build(p)

    return len([1 for p in people if p.decision == "Stay"])


for n in range(100):
    print(run_simulation())

"""
Smil's inspiration is that of

> Boserup (1965, 1976) conceptualized the link between food energy and the evolution of peasant
> societies as a matter of choices.

These choices are once an agricultural system (land, community, no of workers etc.) reaches the
limits of its productivity, people can:

* Migrate.
* Stay (and stabilize numbers).
* Stay (and let their numbers decline).
* Adopt more productive form of farming.

The last option seems like a no brainer but required large energy inputs.

> Increased productivity will support larger populations by cultivating the same (or even smaller)
> areas, but the net energy return of intensified cropping may not increase and may actually decline

To get more out the land, you had to put more in (work). This might not pay off.

According to Smil, everywhere in the world was slow to advance productivity of the land they had.
> everywhere, it took millennia to shift from regular, extensive fallowing to annual cropping and
> then to multicropping.

> Carolingian Europe were overpopulated and their grain supplies were chronically inadequate, but
> only in parts of Germany and Flanders were new fields created in less easily cultivable areas

**Where the marginal cost to cut cropland was high, farming intensification increased.**

"""
