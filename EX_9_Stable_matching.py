"""
    Stable Matching Problem Implementation

    Author: Ashuwin P <ashuwin2210335@ssn.edu.in>

    For UIT2402 Advanced Data Structures and Algorithms Course

    Updated on : 18 - 06- 2024
"""

class Stable_Matching:
    def __init__(self, menperf, womenpref):
        self.men_preference = menperf
        self.women_preference = womenpref

    def match(self):
        def better_choice(woman, man1, man2):
            choice1 = self.women_preference[woman].index(man1)
            choice2 = self.women_preference[woman].index(man2)
            return man1 if choice1 < choice2 else man2

        single_men = list(self.men_preference.keys())
        proposal = {man: 0 for man in single_men}
        pair = {}

        while single_men:
            man = single_men[0]
            woman = self.men_preference[man][proposal[man]]

            if woman not in pair:
                pair[woman] = man
                single_men.remove(man)

            else:
                paired_man = pair[woman]
                better_man = better_choice(woman, paired_man, man)
                if better_man == paired_man:
                    proposal[man] += 1
                    continue
                else:
                    pair[woman] = man
                    single_men.remove(man)
                    single_men.append(paired_man)

        return pair


if __name__ == "__main__":
    men_preference = {"m1": ["w1", "w2"], "m2": ["w1", "w2"]}

    women_preference = {"w1": ["m1", "m2"], "w2": ["m1", "m2"]}

    SM = Stable_Matching(men_preference, women_preference)
    print(SM.match())
