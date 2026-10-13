from flask import Flask, flash, redirect, render_template, request, url_for

from manager import PortfolioManager
from models import Skill

app = Flask(__name__)
app.secret_key = "change-this-secret-key"  # needed for flash messages

manager = PortfolioManager()

# Edit these to change what shows on the home page.
PROFILE = {
    "name": "Adrian Roxas",
    "tagline": "Just a regular dude with something on his mind.",
    "course": "Bachelor of Science in Information Technology",
    "school": "PHINMAED University of Iloilo",
    "intro": ("Hi, I'm Adrian. I'm an Information Technology student who is learning "
              "to turn ideas into working programs, one project at a time."),
    "email": "adca.roxas.ui@phinmaed.com",
}


@app.errorhandler(Exception)
def handle_error(error):
    # Let Flask handle normal HTTP errors such as 404.
    if hasattr(error, "code") and error.code:
        return error
    return render_template("error.html", message=str(error)), 500


# ---------- public page ----------
@app.route("/")
def home():
    return render_template("index.html", profile=PROFILE,
                           projects=manager.get_projects(), skills=manager.get_skills())


# ---------- admin: manage projects and skills ----------
@app.route("/admin")
def admin():
    return render_template("admin.html", projects=manager.get_projects(),
                           skills=manager.get_skills())


@app.route("/admin/project/new", methods=["GET", "POST"])
def new_project():
    if request.method == "POST":
        try:
            project = manager.new_project(
                request.form.get("type"), 0, request.form.get("title"),
                request.form.get("description"), request.form.get("tech_stack"),
                request.form.get("link"))
            manager.add_project(project)
            flash("Project added.", "ok")
            return redirect(url_for("admin"))
        except ValueError as e:
            flash(str(e), "error")
    return render_template("project_form.html", project=None, form=request.form)


@app.route("/admin/project/<int:project_id>/edit", methods=["GET", "POST"])
def edit_project(project_id):
    project = manager.get_project(project_id)
    if project is None:
        flash("Project not found.", "error")
        return redirect(url_for("admin"))
    if request.method == "POST":
        try:
            updated = manager.new_project(
                request.form.get("type"), project_id, request.form.get("title"),
                request.form.get("description"), request.form.get("tech_stack"),
                request.form.get("link"))
            manager.update_project(updated)
            flash("Project updated.", "ok")
            return redirect(url_for("admin"))
        except ValueError as e:
            flash(str(e), "error")
    return render_template("project_form.html", project=project, form=request.form)


@app.route("/admin/project/<int:project_id>/delete", methods=["POST"])
def delete_project(project_id):
    manager.delete_project(project_id)
    flash("Project deleted.", "ok")
    return redirect(url_for("admin"))


@app.route("/admin/skill/add", methods=["POST"])
def add_skill():
    try:
        manager.add_skill(Skill(0, request.form.get("name")))
        flash("Skill added.", "ok")
    except ValueError as e:
        flash(str(e), "error")
    return redirect(url_for("admin"))


@app.route("/admin/skill/<int:skill_id>/delete", methods=["POST"])
def delete_skill(skill_id):
    manager.delete_skill(skill_id)
    flash("Skill deleted.", "ok")
    return redirect(url_for("admin"))


if __name__ == "__main__":
    app.run(debug=True)
