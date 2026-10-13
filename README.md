# Adrian Roxas | Flask Portfolio (Python OOP + MySQL)

A dark neon portfolio built with Flask. Projects and skills are stored in MySQL and managed from a simple `/admin` page.

## OOP concepts

| Concept | Where |
|---|---|
| **Encapsulation** | `models.py`: `Project` and `Skill` keep their data private (`__title`, `__name` ...). It is read through properties, and the setters validate it (no empty title, links must start with `http://` or `https://`). |
| **Inheritance** | `WebProject` and `AppProject` extend `Project`. `PortfolioManager` extends `Database`. |
| **Polymorphism** | `get_type()`, `get_label()` and `get_summary()` are overridden in each project subclass. `index.html` calls `project.get_summary()` and each project type answers differently. |

## Files
- `database.py` - parent class, MySQL connection
- `models.py` - `Skill`, `Project`, `WebProject`, `AppProject`
- `manager.py` - all SQL (extends `Database`)
- `app.py` - Flask routes and your profile text (edit `PROFILE` to change it)
- `templates/` - HTML pages (Jinja2)
- `static/` - CSS and your photo
- `database/portfolio_flask.sql` - creates the database and tables

## Setup
1. Start MySQL.
2. Run `database/portfolio_flask.sql` in MySQL Workbench or phpMyAdmin.
3. Install the requirements:
   ```
   pip install -r requirements.txt
   ```
4. Run:
   ```
   python app.py
   ```
5. Open http://127.0.0.1:5000 for the portfolio and http://127.0.0.1:5000/admin to add projects and skills.

Default database login: `root` with an empty password, database `portfolio_flask`.
To change it, set the environment variables `PORTFOLIO_DB_HOST`, `PORTFOLIO_DB_USER`, `PORTFOLIO_DB_PASSWORD`, `PORTFOLIO_DB_NAME`.

## Note
The `/admin` page has no login, so run this on your own computer only. Do not put it on the public internet as is.
