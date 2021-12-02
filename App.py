from flask import Flask, render_template, redirect, request, url_for
from models import db, Project, app
import random
import datetime


@app.route("/")
def index():
    projects = Project.query.all()
    return render_template("index.html", projects=projects)


@app.route("/about")
def about():
    projects = Project.query.all()
    return render_template("about.html", projects=projects)


@app.route("/projects/new", methods=['GET', 'POST'])
def new_project():
    projects = Project.query.all()
    if request.form:
        year = request.form["date"][0:4]
        month = request.form["date"][5:7]
        new_project = Project(
          title=request.form["title"],
          date=request.form["date"],
          description=request.form.get["description"],
          skills=request.form["skills"],
          url=request.form["github"])
        db.session.add(new_project)
        db.session.commit()
        return redirect(url_for("index"))
    return render_template("projectform.html", projects=projects)


@app.route("/projects/<id>")
def projects_detail(id):
    projects = Project.query.all()
    project = Project.query.get_or_404(id)
    return render_template("detail.html", project=project, projects=projects)


@app.route("/projects/<id>/edit", methods=['GET', 'POST'])
def edit_project(id):
    projects = Project.query.all()
    project = Project.query.get_or_404(id)
    if request.form:
        project.title = request.form["title"]
        year = request.form["date"][0:4]
        month = request.form["date"][5:7]
        project.date = request.form["date"]
        project.description = request.form.get["description"]
        project.skills = request.form["skills"]
        project.url = request.form["github"]
        db.session.commit()
        return redirect(url_for("index"))
    return render_template("edit.html", project=project, projects=projects)


@app.route("/projects/<id>/delete")
def delete_project(id):
    projects = Project.query.all()
    project = Project.query.get_or_404(id)
    db.session.delete(project)
    db.session.commit()
    return redirect(url_for("index"))
  
  

@app.errorhandler(404)
def not_found(error):
    projects = Project.query.all()
    return render_template("404.html", msg=error, projects=projects), 404


if __name__ == "__main__":
    db.create_all()
    app.run(debug=True, port=8000, host="127.0.0.1")
