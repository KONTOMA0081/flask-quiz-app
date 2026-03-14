from datetime import datetime

class Question:
    def __init__(self, text, answer):
        self.text = text
        self.answer = answer
        self.created_at = datetime.now()

    def check_answer(self, user_answer):
        return user_answer == self.answer


class QuestionQueue:
    def __init__(self):
        self.queue = []

    def add_question(self, question):
        self.queue.append(question)

    def get_question(self):
        if len(self.queue) > 0:
            return self.queue.pop(0)
        return None