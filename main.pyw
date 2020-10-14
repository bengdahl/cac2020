import tkinter as tk
from datetime import datetime
import json

# Minimum number of points needed to order the user to stay home
REJECT_POINTS = 3
# Symptoms and weights
QUESTIONS = {
    'Fever or chills' : 3,
    'Persistent cough' : 3,
    'Shortness of breath' : 2,
    'Fatigue' : 1,
    'Muscle or body aches' : 2,
    'Headaches' : 1,
    'Recent loss of taste or smell' : 3,
    'Sore throat' : 2,
    'Nasal congestion or running nose' : 2,
    'Nausea or vomiting' : 3,
    'Diarrhea' : 3,
}

def ask_for_name(w):
    tk.Label(w, text="Please input your full name.").grid(row=0, pady=5, padx=5)
    name = tk.StringVar()
    tk.Entry(w, textvariable=name).grid(row=1, pady=5, padx=5)
    def submit():
        if len(name.get()) > 0:
            w.destroy()
        else:
            pass
    button = tk.Button(w, text='Submit', command=submit, state=tk.DISABLED)
    button.grid(row=2, pady=5, padx=5)

    def onupdate(*_args):
        if len(name.get())>0:
            button.configure(state=tk.NORMAL) 
        else:
            button.configure(state=tk.DISABLED)
    name.trace_add(['write','unset'], onupdate)

    w.mainloop()

    return name.get()

def get_symptoms(w):
    tk.Label(w, text="Select all of the symptoms you are currently experiencing").grid(row=0, pady=5, padx=5)

    checkvars = []
    for i, (question, weight) in enumerate(QUESTIONS.items()):
        selected = tk.IntVar()
        box = tk.Checkbutton(w, text=question, variable=selected)
        box.grid(row = i+1, sticky='w', padx=10)
        checkvars.append((selected, weight, question))

    r = {}
    def submit():
        r.update({ q:w if s.get()>0 else 0 for (s,w,q) in checkvars })
        w.destroy()

    tk.Button(w, text="Submit", command=submit).grid(row=len(QUESTIONS)+1, pady=10)

    w.mainloop()

    return r

def give_feedback(w, symptoms):
    points = sum(w for w in symptoms.values())
    if points >= REJECT_POINTS:
        msg = "You are showing symptoms associated with COVID-19. \nThis information has been recorded, Please go home."
    else:
        msg = "Thank you for taking the time to complete this. \nYou are safe to come in to work today."
    tk.Label(w, text=msg).grid(row=0, pady=10, padx=10)

    w.mainloop()

a = tk.Tk()
name = ask_for_name(a)
b = tk.Tk()
symptoms = get_symptoms(b)

logobj = {"name": name}
logobj.update(symptoms)

from pathlib import Path
path = Path(__file__).parent.joinpath("results_log.txt")
with path.open("a") as f:
    f.write(str(datetime.utcnow().replace(microsecond=0).isoformat()) + ' ' + json.dumps(logobj) + "\n")

c = tk.Tk()
give_feedback(c, symptoms)