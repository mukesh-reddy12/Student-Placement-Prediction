C:\Users\hp\OneDrive\Desktop\Student-Placement-Prediction
import pickle

model = pickle.load(open("placement_model.pkl", "rb"))

print("Enter Student Details:")

cgpa = float(input("CGPA: "))
internships = int(input("Internships: "))
projects = int(input("Projects: "))
communication = int(input("Communication (1-10): "))
technical = int(input("Technical Skills (1-10): "))
aptitude = int(input("Aptitude Score: "))
backlogs = int(input("Backlogs: "))

result = model.predict([[cgpa, internships, projects, communication, technical, aptitude, backlogs]])

if result[0] == 1:
    print("High Chances of Placement 🎉")
else:
    print("Low Chances of Placement")