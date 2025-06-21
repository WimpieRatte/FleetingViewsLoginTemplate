# Description
This is a template that I want to use for my Flet projects that need a login screen and multiple pages in the application.
It was built while watching a video for the https://github.com/ArellanoBrunoc/FleetingExample repo.
(So, essentially, kudos to Arellano Brunoc for this!)

# How to run
- Have Python installed
- Have Git installed
- Have UV installed (in Windows, simply run `winget install --id=astral-sh.uv  -e` in your CMD, then restart your command prompts and IDE's.)
- Run `git clone https://github.com/WimpieRatte/FleetingViewsLoginTemplate.git` to create a folder for this project and download it.
- Open the above created folder in VS Code, or whatever IDE you use.
- Create a virtual environment (Via Terminal, run `uv venv`)
- Activate the virtual environment (Via Terminal, run `.\.venv\Scripts\activate`)
- Run the app (Via Terminal, run `uv run main.py`)
(Of course, this app can be published to Windows/Linux/whatever, because it's coded in Flet, but since this is just a template/skeleton for a new app, I'm assuming no one would need instructions for that.)

# Status
### Done
- Basic example built
- Changed color schemes (2025-06-21)
- Added regions for easier readability (2025-06-21)
- Changed to better font (2025-06-21)
### Todo
- Use this in other projects I want to do :).

# Technologies/Modules used
- UV
- Flet
- Fleeting Views

# Assets
- Font: Arial

# Basic Structure
- Create `__init__.py` file in all folders, so Python sees them as modules.
- Create an own folder for each page/view. (I'm placing those subfolders in the Views folder.)
    - In each folder, create a *_view.py file as additional design view file for each of your content pages/views.
    - in main.py, import these design view files, but for your login, only importing the `login_init` method is needed.
    - Remember, the views/pages already got created via "FleetingViews.create_views", so these are just for adding your additional page content via fv.append(...).
    - You'll need to build all these (call their *_init(fv) methods) before doing your first fv.view_go(...).
- Connection stuff in the "connection" folder.
    - session.py and credentials.py can be replaced/customised for whatever connection you need.
- Colors/themes
    - I specified a theme in main.py for the main page. (color_scheme_seed=ft.Colors.INDIGO)
    - Can also be customised for each view/page during "view_definitions" declaration (before instantiating the FleetViews manager).
- "assets/fonts" contain custom fonts.
    - I chose "Arial", because it's fully free and reads nicely.
- Tell FleetingViews which guard belong to every view (also addable during runtime)
- Have a snackbar (we're calling it "alert") to show the app's feedback to user.
- When declaring custom controls/containers in the views, use FleetingViews' append method to add to UI