from flask import Flask, render_template, request, redirect, url_for, jsonify

app = Flask(__name__)

projects = []
tasks = []
project_id_counter = 1
task_id_counter = 1


@app.route("/")
def index():
    return render_template("index.html", projects=projects)


@app.route("/add_project", methods=["POST"])
def add_project():
    global project_id_counter
    project_name = request.form.get("project")
    if project_name:
        projects.append({"id": project_id_counter, "name": project_name, "tasks": []})
        project_id_counter += 1
    return redirect(url_for("index"))


@app.route("/add_task/<int:project_id>", methods=["POST"])
def add_task(project_id):
    global task_id_counter
    task_name = request.form.get("task")
    if task_name:
        for project in projects:
            if project["id"] == project_id:
                project["tasks"].append(
                    {
                        "id": task_id_counter,
                        "name": task_name,
                        "state": "backlog",
                        "notes": "",
                    }
                )
                task_id_counter += 1
                break
    return redirect(url_for("index"))


@app.route("/update_task_state/<int:task_id>", methods=["POST"])
def update_task_state(task_id):
    new_state = request.json.get("state")
    for project in projects:
        for task in project["tasks"]:
            if task["id"] == task_id:
                task["state"] = new_state
                break
    return jsonify({"success": True})


@app.route("/update_task_notes/<int:task_id>", methods=["POST"])
def update_task_notes(task_id):
    new_notes = request.json.get("notes")
    for project in projects:
        for task in project["tasks"]:
            if task["id"] == task_id:
                task["notes"] = new_notes
                break
    return jsonify({"success": True})


@app.route("/delete_task/<int:task_id>", methods=["POST"])
def delete_task(task_id):
    for project in projects:
        project["tasks"] = [task for task in project["tasks"] if task["id"] != task_id]
    return jsonify({"success": True})


if __name__ == "__main__":
    app.run(debug=True)
