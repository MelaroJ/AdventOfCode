"""AOC Day 5

Part 1: Determine which page update runs are in correct order based on the 
        page-ordering rules preceding them. Then, sum the middle elements
        from each list of runs.
Part 2: Take the page update runs in incorrect order, rearrange them into the
        correct order, and sum the middle elements.

Example:

The first page-ordering rule signifies pg 47 must be updated before pg 53,
the next that pg 97 must be updated before pg 13, and so on.

The first 3 updates below the page-ordering rules (separated by a blank line)
are in correct order, while the final 3 are NOT. the runs may also not include
every page number, and so only some of the ordering rules apply - within each
update, the ordering rules that involve missing page numbers are not used.
    
47|53
97|13
97|61
97|47
75|29
61|13
75|53
29|13
97|29
53|29
61|53
97|53
61|29
47|13
75|47
97|75
47|61
75|61
47|29
75|13
53|13

75,47,61,53,29
97,61,53,29,13
75,29,13
75,97,47,61,53
61,13,29
97,13,75,29,47
"""
import time

class aoc5:

    def __init__(self) -> None:
        """Initialize list of page-order rules as tuples and page update runs
        as list of lists.
        """
        self.start = time.time()
        self.rules = []
        self.page_runs = []
        with open('2024/05.in', 'r') as f:
            for line in f.readlines():
                if '|' in line:
                    self.rules.append(
                            tuple(
                                map(
                                    int,
                                    line.strip().split('|')
                                )
                            )
                        )
                elif ',' in line:
                    self.page_runs.append(
                            list(
                                map(
                                    int,
                                    line.strip().split(',')
                                )
                            )
                        )

    def solve_elf_problems(self):
        """run em both"""
        self.check_runs()
        self.sum_middle_nums()

    def check_runs(self):
        """Validate the page runs against the page-ordering rules, filter out
        bad runs from self.page_runs"""
        self.rules_dict = {}
        self.good_runs = []
        self.bad_runs = []
        self.fixed_runs = []
        
        for A, B in self.rules:
            if A not in self.rules_dict:
                self.rules_dict[A] = []
            self.rules_dict[A].append(B)

 
        for run in self.page_runs:
            run_set = set(run) #faster lookup

            relevant_rules = [
                (A, B) for A in run_set if A in self.rules_dict
                for B in self.rules_dict[A] if B in run_set
                ]

            is_good = all(
                run.index(rule[0]) < run.index(rule[1])
                for rule in relevant_rules
                )

            if is_good:
                self.good_runs.append(run)
            else:
                self.bad_runs.append(run)

                fixed_run = run
                
                index_cache = {
                        value: idx
                        for idx, value in enumerate(fixed_run)
                        }
                while not all(
                        index_cache[rule[0]] < index_cache[rule[1]]
                        for rule in relevant_rules
                ):

                    for rule in relevant_rules:
                        A, B = rule
                        if index_cache[A] > index_cache[B]:
                            fixed_run.remove(A)
                            fixed_run.insert(index_cache[B], A)
                            index_cache = {
                                    value: idx
                                    for idx, value in enumerate(fixed_run)
                                    }

                self.fixed_runs.append(fixed_run)
        

    def sum_middle_nums(self):
        """Calculate the separate sums of middle elements for good and bad runs."""
        
        # Helper function to calculate the sum of middle elements for a list of runs
        def middle_sum(runs):
            return sum(
                run[len(run) // 2]
                for run in runs
            )
        
        # Calculate sums for good and bad runs
        p1 = middle_sum(self.good_runs)
        p2 = middle_sum(self.fixed_runs)
        
        print(f"p1: \n{p1}")
        print(f"p2: \n{p2}")


if __name__ == '__main__':
    day5 = aoc5()
    day5.solve_elf_problems()
    print(f"Time elapsed: {(time.time()-day5.start):.3f} seconds")

   
