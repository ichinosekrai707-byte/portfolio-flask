from database import Database
from models import AppProject, Project, Skill, WebProject


class PortfolioManager(Database):
    """INHERITANCE: extends Database, so it can call get_connection().
    All SQL for projects and skills lives here."""

    # ---------- projects ----------
    def get_projects(self):
        rows = self._fetch("SELECT * FROM project ORDER BY ID DESC")
        return [self._create_project(row) for row in rows]

    def get_project(self, project_id):
        rows = self._fetch("SELECT * FROM project WHERE ID = %s", (project_id,))
        return self._create_project(rows[0]) if rows else None

    def add_project(self, project):
        self._execute(
            "INSERT INTO project (Title, Description, Type, TechStack, Link) "
            "VALUES (%s, %s, %s, %s, %s)",
            (project.title, project.description, project.get_type(),
             project.tech_stack, project.link),
        )

    def update_project(self, project):
        self._execute(
            "UPDATE project SET Title = %s, Description = %s, Type = %s, "
            "TechStack = %s, Link = %s WHERE ID = %s",
            (project.title, project.description, project.get_type(),
             project.tech_stack, project.link, project.id),
        )

    def delete_project(self, project_id):
        self._execute("DELETE FROM project WHERE ID = %s", (project_id,))

    # ---------- skills ----------
    def get_skills(self):
        rows = self._fetch("SELECT * FROM skill ORDER BY ID")
        return [Skill(row["ID"], row["Name"]) for row in rows]

    def add_skill(self, skill):
        self._execute("INSERT INTO skill (Name) VALUES (%s)", (skill.name,))

    def delete_skill(self, skill_id):
        self._execute("DELETE FROM skill WHERE ID = %s", (skill_id,))

    # ---------- helpers ----------
    @staticmethod
    def new_project(project_type, project_id, title, description, tech_stack="", link=""):
        """Returns the right subclass for the chosen type."""
        if project_type == "WEB":
            return WebProject(project_id, title, description, tech_stack, link)
        if project_type == "APP":
            return AppProject(project_id, title, description, tech_stack, link)
        return Project(project_id, title, description, tech_stack, link)

    def _create_project(self, row):
        return self.new_project(row["Type"], row["ID"], row["Title"],
                                row["Description"], row["TechStack"] or "", row["Link"] or "")

    def _fetch(self, sql, params=()):
        conn = self.get_connection()
        try:
            cursor = conn.cursor(dictionary=True)
            cursor.execute(sql, params)
            return cursor.fetchall()
        finally:
            conn.close()

    def _execute(self, sql, params=()):
        conn = self.get_connection()
        try:
            cursor = conn.cursor()
            cursor.execute(sql, params)
            conn.commit()
        finally:
            conn.close()
