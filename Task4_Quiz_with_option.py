import tkinter as tk
from tkinter import messagebox

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
        
        self.options_frame = tk.Frame(master, pady=10)
        self.options_frame.pack()
        
        self.option_buttons = []
        for i in range(4):
            button = tk.Button(self.options_frame, text="", font=("Helvetica", 12), command=lambda idx=i: self.submit_answer(idx))
            button.pack(side=tk.LEFT, padx=5)
            self.option_buttons.append(button)
        
        self.feedback_label = tk.Label(master, text="", font=("Helvetica", 12))
        self.feedback_label.pack()
        
        self.next_button = tk.Button(master, text="Next", font=("Helvetica", 12), command=self.next_question, state=tk.DISABLED)
        self.next_button.pack(pady=5)
        
        self.update_question()
        
    def update_question(self):
        if self.current_question_index < self.total_questions:
            question_data = self.questions[self.current_question_index]
            self.question_label.config(text=question_data['question'])
            options = question_data['options']
            for i in range(min(len(options), 4)):
                self.option_buttons[i].config(text=options[i])
            for i in range(len(options), 4):
                self.option_buttons[i].config(text="")
            self.feedback_label.config(text="")
        else:
            self.quiz_complete()
    
    def submit_answer(self, idx):
        selected_option = self.option_buttons[idx]['text']
        correct_answer = self.questions[self.current_question_index]['answer']
        
        if selected_option == correct_answer:
            self.score += 1
            self.feedback_label.config(text="Correct!", fg="green")
        else:
            self.feedback_label.config(text="Incorrect! Correct answer: {}".format(correct_answer), fg="red")
        
        for button in self.option_buttons:
            button.config(state=tk.DISABLED)
        
        self.next_button.config(state=tk.NORMAL)
    
    def next_question(self):
        self.current_question_index += 1
        
        for button in self.option_buttons:
            button.config(state=tk.NORMAL)
        
        if self.current_question_index == self.total_questions:
            self.next_button.config(text="Finish")
        
        self.update_question()
        
    def quiz_complete(self):
        messagebox.showinfo("Quiz Complete", "Quiz complete! You scored {}/{}.".format(self.score, self.total_questions))
        self.master.quit()

if __name__ == "__main__":
    quiz_questions = [
        {"question": "What is the capital of France?", "options": ["Paris", "London", "Berlin", "Rome"], "answer": "Paris"},
        {"question": "What is 2 + 2?", "options": ["2", "3", "4", "5"], "answer": "4"},
        {"question": "Who wrote 'Romeo and Juliet'?", "options": ["William Shakespeare", "Jane Austen", "Charles Dickens", "Mark Twain"], "answer": "William Shakespeare"},
        {"question": "What is the largest mammal?", "options": ["Elephant", "Blue whale", "Giraffe", "Polar bear"], "answer": "Blue whale"}
    ]
    
    root = tk.Tk()
    root.title("Quiz App")
    app = QuizApp(root, quiz_questions)
    root.mainloop()
