import json
from flask import Flask, render_template, request
from mentor_mentee_object import find_best_mentor

app = Flask(__name__)

@app.route("/", methods=["GET"])
def main():
    return render_template("fakeform.html")

@app.route("/second-page", methods=["GET"])
def second_page():
    return render_template("formpage2.html")

@app.route("/mentor-match", methods=["GET"])
def mentor_match():
    return render_template("best-mentor.html")

@app.route("/best-mentor", methods=["GET"])
def best_match():
    return find_best_mentor()

@app.route("/next-page", methods=["POST"])
def next_page():
    req_data = request.form
    dictionary = req_data.to_dict()

    new_dict = {}
    full_name = dictionary["first"] + " " + dictionary["last"]
    new_dict["name"] = full_name

    with open('user.json', 'w') as current_user_file:
        json.dump(new_dict, current_user_file)

    return "done"

@app.route("/add-new-user", methods=["POST"])
def add_new_user():
    req_data = request.form
    dictionary = req_data.to_dict()

    name = ""

    # reads json file
    with open('user.json') as current_user_file:
        data = json.load(current_user_file)
        name = data["name"]

    new_dict = {}
    new_dict["name"] = name
    new_dict["bio"] = dictionary["bio"]
    new_dict["companies"] = dictionary["companies"].split("\n")

    # overwrites the entire json file
    with open('user.json', 'w') as current_user_file:
        json.dump(new_dict, current_user_file)

    return "done"

if __name__ == '__main__':
    app.run()
