# Description
This is a template that I want to use for my Flet projects that need a login screen and multiple pages in the application.
It was built while watching a video for the https://github.com/ArellanoBrunoc/FleetingExample repo.
(So, essentially, kudos to Arellano Brunoc for this!)

# Status
### Done
- Basic example built
### Todo
- Change color schemes
- Add regions for easier readability
- Check for more readable font

# Technologies/Modules used
- UV (Ran `uv init` command to setup the basics at first.)
- Flet
- Fleeting Views

# Assets
## Fonts
- Oblata Display: https://www.fontspace.com/oblata-display-font-f140482 (free for commercial use)

# Basic Structure
- Create `__init__.py` file in all folders, so Python sees them as modules.
- Create an own folder for each page/view. (I'm placing those subfolders in the Views folder.)
- Create *_view.py as a design view file for each page/view.
    - Import the entire home and settings views, but only the login's `login_init` method.
- Connection stuff in the "connection" folder.
    - session.py and credentials.py can be replaced/customised for whatever connection you need.
- colors.py: Colors module to keep UI style central.
    - Import them to main for easy reference.
- "assets/fonts" contain custom fonts.
    - I chose "Oblata Display", because it's fully free.
- Tell FleetingViews which guard belong to every view (also addable during runtime)
- Have a snackbar (we're calling it "alert") to show the app's feedback to user.
- When declaring custom controls/containers in the views, use FleetingViews' append method to add to UI