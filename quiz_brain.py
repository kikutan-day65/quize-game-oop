class QuizBrain:
    def __init__(self, q_list):
        self.question_num = 0
        self.question_list = q_list
    
    def next_q(self):
        cur_q = self.question_list[self.question_num]
        self.question_num += 1
        input(f"Q{self.question_num}: {cur_q.text} (True/False)")