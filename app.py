from flask import Flask, render_template, request, session

app = Flask(__name__)
app.secret_key = "your_secret_key"  # Set a secret key for session management

@app.route('/', methods=["GET","POST"])
def index():
    if request.method=="POST":
        note = request.form.get("note")
        session.setdefault("notes",[]).append(note)  # Store notes in the session
        
    return render_template("home.html", notes= session.get("notes", []))


if __name__ == '__main__':
    app.run(debug=True)
