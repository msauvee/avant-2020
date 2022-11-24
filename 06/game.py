class GrooupAnswer:
    def __init__(self):
        self._yes_answers = []
        self._yes_in_common = None

    def add_yes_answers(self, line):
        if self._yes_in_common is None:
            self._yes_in_common = []
            for answer in line:
                self._yes_in_common.append(answer)
        else:
            keep = []
            for yes in self._yes_in_common:
                if yes in line:
                    keep.append(yes)
            self._yes_in_common = keep

        for answer in line:
            if not answer in self._yes_answers:
                self._yes_answers.append(answer)
            

    def number_of_different_yes(self):
        return len(self._yes_answers)

    def number_of_yes_in_common(self):
        return 0 if self._yes_in_common is None else len(self._yes_in_common)

def parse(lines):
    group_answers = []
    current_group = None
    for line in lines:
        if current_group is None or len(line) == 0:
            current_group = GrooupAnswer()
            group_answers.append(current_group)
        if len(line) > 0:
            current_group.add_yes_answers(line)
                
    return group_answers

def compute_puzzle1(group_answers):
    sum = 0
    for group_answer in group_answers:
        sum += group_answer.number_of_different_yes()
    return sum

def compute_puzzle2(group_answers):
    sum = 0
    for group_answer in group_answers:
        sum += group_answer.number_of_yes_in_common()
    return sum