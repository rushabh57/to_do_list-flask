from flask import Flask, render_template ,request,redirect
app = Flask(__name__)

# request : Gets Data sent by user(like form input)
# redirect : Sends user to another Page
# render_templates: Load Html

# --simple app
# @app.route("/")
# def home():
#     return " this is Home !"

tasks = []
@app.route("/")
def index():
    return render_template('index.html' , tasks=tasks)
@app.route('/add' , methods=['POST'])

def add():
    task = request.form.get('task')
    if task:
        tasks.append(task)
    return redirect('/')

@app.route('/delete/<int:task_id>')
def delete(task_id):
    if 0 <= task_id < len(tasks):
        tasks.pop(task_id)
    return redirect('/')

if __name__ == '__main__':
    app.run(debug = True)