import tkinter as tk

w = tk.Tk()

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

tk.Label(w, text="Select all of the symptoms you are currently experiencing").grid(row=0, pady=5, padx=5)

checkvars = []
for i, (question, weight) in enumerate(QUESTIONS.items()):
    selected = tk.IntVar()
    box = tk.Checkbutton(w, text=question, variable=selected)
    box.grid(row = i+1, sticky='w', padx=10)
    checkvars.append((selected, weight))

def submit():
    points = sum(w for (v, w) in checkvars if v.get() > 0)
    # Placeholder for now
    # TODO: Add pdf report printout
    if points >= REJECT_POINTS:
        print("Stay home")
    else:
        print("Safe to go to work")

tk.Button(w, text="Submit", command=submit).grid(row=len(QUESTIONS)+1, pady=10)

w.mainloop()