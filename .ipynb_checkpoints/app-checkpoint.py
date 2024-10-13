from flask import Flask , render_template , request
import pickle

app = Flask(__name__)

priority = {}
with open('priority.pkl' , 'rb') as f:
    priority = pickle.load(f)

students = {}
with open('students.pkl' , 'rb') as f:
    students = pickle.load(f)

# subjects = {}
# with open('subjects.pkl' , 'rb') as f:
#     subjects = pickle.load(f)
code_to_name = {}
with open('code_to_name.pkl' , 'rb') as f:
    code_to_name = pickle.load(f)
@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict" , methods = ['POST' , 'GET']) 
def predict():
    usn = request.form.get("usn").upper()
    # print(subjects)
    # usn = f"\"{usn}\""
    # print(type(usn))
    # subject = subjects[usn]
    student = students.get(usn , -1)
    priority_list = -1
    sub_name = -1
    copy_list = -1
    # for key , value in priority.items():
    #     value += " " + code_to_name[priority[key]]

    if(student != -1):
        priority_list = priority[usn]
        copy_list = priority_list.copy()
        for key , value in priority_list.items():
            copy_list[key] += " ( " + code_to_name[priority_list[key]] + " )"

        sub_name = code_to_name[student]
    return render_template("result.html"  , student = student , sub_name = sub_name , priority_list = copy_list)

if __name__ == "__main__":
    print("Running Elective Predictor server")
    app.run(debug = True)
    

