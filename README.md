# ahk-shiny-counter
This is a very simple web app + AutoHotkey combo I threw together that lets you increment a counter with a keybind without having to keep the webpage open.
I use it so I can keep track of my shiny hunt encounters while multitasking so I don't have to keep a counter open 24/7.

### Setup
You'll need to install Flask (`pip install Flask`) and AutoHotkey. 

### Usage
To use it, run the web app using `python run.py` while in the `counter` directory, and then execute the `counter.ahk` file. Open the web app with `http://localhost:5000/` and update the counter using `alt + c`. You can change this hotkey if you wish by editing `counter.ahk`.

Like most of my projects on here, this is likely of little use to most people and just something I cooked up to solve something that was bugging me. 