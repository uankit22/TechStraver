import tkinter as tk
from tkinter import messagebox
import time

class QuizApp:
    def __init__(self, master, questions):
        self.master = master
        self.questions = questions
        self.total_questions = len(questions)
        self.current_question_index = 0
        self.score = 0
        
        self.question_frame = tk.Frame(master, pady=10)
        self.question_frame.pack()
        
        self.question_label = tk.Label(self.question_frame, text="", font=("Helvetica", 14), wraplength=400)
        self.question_label.pack()
        
        self.answer_entry = tk.Entry(master, font=("Helvetica", 12))
        self.answer_entry.pack(pady=5)
        
        self.feedback_label = tk.Label(master, text="", font=("Helvetica", 12))
        self.feedback_label.pack()
        
        self.submit_button = tk.Button(master, text="Submit", font=("Helvetica", 12), command=self.submit_answer)
        self.submit_button.pack(pady=5)
        
        self.next_button = tk.Button(master, text="Next", font=("Helvetica", 12), command=self.next_question, state=tk.DISABLED)
        self.next_button.pack(pady=5)
        
        self.update_question()
        
    def update_question(self):
        if self.current_question_index < self.total_questions:
            self.question_label.config(text=self.questions[self.current_question_index]['question'])
            self.feedback_label.config(text="")
        else:
            self.quiz_complete()
    
    def submit_answer(self):
        user_answer = self.answer_entry.get().strip().lower()
        correct_answer = self.questions[self.current_question_index]['answer'].lower()
        
        if user_answer == correct_answer:
            self.score += 1
            self.feedback_label.config(text="Correct!", fg="green")
        else:
            self.feedback_label.config(text="Incorrect! Correct answer: {}".format(correct_answer), fg="red")
        
        self.current_question_index += 1
        self.answer_entry.delete(0, tk.END)
        
        if self.current_question_index == self.total_questions:
            self.next_button.config(text="Finish")
        
        self.submit_button.config(state=tk.DISABLED)
        self.master.after(1500, self.next_question)  # Move to next question after 1.5 seconds
    
    def next_question(self):
        if self.current_question_index == self.total_questions:
            self.quiz_complete()
        else:
            self.update_question()
            self.submit_button.config(state=tk.NORMAL)
        
    def quiz_complete(self):
        messagebox.showinfo("Quiz Complete", "Quiz complete! You scored {}/{}.".format(self.score, self.total_questions))
        self.master.quit()

if __name__ == "__main__":
    quiz_questions = [
        {"question": "What is the capital of France?", "answer": "Paris"},
        {"question": "What is 2 + 2?", "answer": "4"},
        {"question": "Who wrote 'Romeo and Juliet'?", "answer": "William Shakespeare"},
        {"question": "What is the largest mammal?", "answer": "Blue whale"},
        {"question": "What is the chemical symbol for water?", "answer": "H2O"},
        {"question": "What is the currency of Japan?", "answer": "Yen"},
        {"question": "What is the tallest mountain in the world?", "answer": "Mount Everest"},
        {"question": "What is the primary ingredient in guacamole?", "answer": "Avocado"},
        {"question": "Who painted the Mona Lisa?", "answer": "Leonardo da Vinci"},
        {"question": "What is the capital of Australia?", "answer": "Canberra"},
        {"question": "What is the square root of 144?", "answer": "12"},
        {"question": "Who is known as the father of computers?", "answer": "Charles Babbage"},
        {"question": "What is the chemical symbol for gold?", "answer": "Au"},
        {"question": "What year did World War II end?", "answer": "1945"}
    ]
    
    root = tk.Tk()
    root.title("Quiz App")
    app = QuizApp(root, quiz_questions)
    root.mainloop()
