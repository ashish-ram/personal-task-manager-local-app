from flask import Flask, render_template, request, redirect, url_for, jsonify
import pandas as pd

app = Flask(__name__)

EXCEL_FILE = "data.xlsx"


def load_data():
    try:
        df_projects = pd.read_excel(EXCEL_FILE, sheet_name="Projects")
        df_tasks = pd.read_excel(EXCEL_FILE, sheet_name="Tasks")
        projects = df_projects.to_dict(orient="records")
        tasks = df_tasks.to_dict(orient="records")
        for project in projects:
            project["tasks"] = [
                task for task in tasks if task["project_id"] == project["id"]
            ]
        return projects
    except FileNotFoundError:
        return []


def save_data(projects):
    df_projects = pd.DataFrame([{"id": p["id"], "name": p["name"]} for p in projects])
    df_tasks = pd.DataFrame(
        [
            {
                "id": t["id"],
                "name": t["name"],
                "state": t["state"],
                "notes": t["notes"],
                "project_id": p["id"],
            }
            for p in projects
            for t in p["tasks"]
        ]
    )
    with pd.ExcelWriter(EXCEL_FILE) as writer:
        df_projects.to_excel(writer, sheet_name="Projects", index=False)
        df_tasks.to_excel(writer, sheet_name="Tasks", index=False)


projects = load_data()
project_id_counter = max([p["id"] for p in projects], default=0) + 1
task_id_counter = max([t["id"] for p in projects for t in p["tasks"]], default=0) + 1


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
        save_data(projects)
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
                        "project_id": project_id,
                    }
                )
                task_id_counter += 1
                save_data(projects)
                break
    return redirect(url_for("index"))


@app.route("/update_task_state/<int:task_id>", methods=["POST"])
def update_task_state(task_id):
    new_state = request.json.get("state")
    for project in projects:
        for task in project["tasks"]:
            if task["id"] == task_id:
                task["state"] = new_state
                save_data(projects)
                break
    return jsonify({"success": True})


@app.route("/update_task_notes/<int:task_id>", methods=["POST"])
def update_task_notes(task_id):
    new_notes = request.json.get("notes")
    for project in projects:
        for task in project["tasks"]:
            if task["id"] == task_id:
                task["notes"] = new_notes
                save_data(projects)
                break
    return jsonify({"success": True})


@app.route("/update_task_name/<int:task_id>", methods=["POST"])
def update_task_name(task_id):
    new_name = request.json.get("name")
    for project in projects:
        for task in project["tasks"]:
            if task["id"] == task_id:
                task["name"] = new_name
                save_data(projects)
                break
    return jsonify({"success": True})


@app.route("/delete_task/<int:task_id>", methods=["POST"])
def delete_task(task_id):
    for project in projects:
        project["tasks"] = [task for task in project["tasks"] if task["id"] != task_id]
    save_data(projects)
    return jsonify({"success": True})


@app.route("/delete_project/<int:project_id>", methods=["POST"])
def delete_project(project_id):
    global projects
    projects = [project for project in projects if project["id"] != project_id]
    save_data(projects)
    return jsonify({"success": True})


if __name__ == "__main__":
    app.run(debug=True)
