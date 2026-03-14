from flask import Flask, render_template, request
from models import Question, QuestionQueue
from datetime import datetime

app = Flask(__name__)

questions = QuestionQueue()

questions.add_question(Question("What is 2 + 2?", "4"))
questions.add_question(Question("What is 3 + 3?", "6"))
questions.add_question(Question("What is 5 + 5?", "10"))

score = 0

@app.route("/")
def home():
    q = questions.get_question()
    if q:
        return render_template("index.html", question=q.text)
    else:
        return render_template("result.html", score=score, time=datetime.now())

@app.route("/result", methods=["POST"])
def result():
    global score
    user_answer = request.form["answer"]

    if user_answer in ["4","6","10"]:
        score += 1

    q = questions.get_question()

    if q:
        return render_template("index.html", question=q.text)
    else:
        return render_template("result.html", score=score, time=datetime.now())

if __name__ == "__main__":
    app.run(debug=True)