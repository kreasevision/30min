from prompt_toolkit import Application, PromptSession
from prompt_toolkit.layout import Layout, HSplit, VSplit, Window, ScrollablePane
from prompt_toolkit.widgets import TextArea, Frame
from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.filters import has_focus
from multiprocessing import Process, shared_memory
import time
from prompt_toolkit.styles import Style
import random
from prompt_toolkit.application.current import get_app
from prompt_toolkit.history import InMemoryHistory
from prompt_toolkit.auto_suggest import AutoSuggestFromHistory
import asyncio
from prompt_toolkit.layout import Layout, Window
from prompt_toolkit.formatted_text import FormattedText
from PIL import Image
from threading import Thread
from prompt_toolkit.layout.controls import FormattedTextControl
import threading
from prompt_toolkit.auto_suggest import AutoSuggest, Suggestion
from prompt_toolkit.document import Document
import visuals


SHARED_MEMORY_SIZE = 1024
SHARED_MEMORY_NAME1 = "my_memory4"

# Open the existing shared memory
shm1 = shared_memory.SharedMemory(name=SHARED_MEMORY_NAME1)

def read_from_shared_memory():
    # Read the content from the shared memory
    content = bytes(shm1.buf).decode('utf-8').rstrip('\0')
    return content


# Define your qualifiers
 
def display_image():
    img = Image.open('path_to_your_image.jpg')
    img.show()

loading_content = FormattedTextControl(text="Loading...", show_cursor=False)
loading_window = Window(content=loading_content, height=3)


# Create a history object
history = InMemoryHistory()

style = Style.from_dict({
    'custom.red': '#ff0000',
    'frame.border': '#ff0000',
})

def generate_rain(width, height):
    return '\n'.join(''.join(random.choice('°.|') for _ in range(width)) for _ in range(height))


octo_art =""

def update_skull_art():
    current_time = time.time()
    index = int(current_time) % len(skull_art)  # Alternates between indices based on time
    return f"{skull_art[index]}\n\n❤️❤️❤️❤️\n\n{octo_art[0]}\n\n{menu()}\n   menu()"

def update_status():
    content = read_from_shared_memory()
 


skull_art = [r"""
         .
         ":"
       ___:____     |"\/"|
      /        `.    \  /
     |  n        \___/  |
  ~^~^~^~^~^~^~^~^~^~^~^~^~
~          ~
""",r"""
         0
        °°°
      ___°____    |"\/"|
     /        `.   \  /
    |  --        \_/  |
 ~^~^~^~^~^~^~^~^~^~^~^~^~
       ~          ~
"""
,r"""
          0
        °°°
      ___°____     |"\/"|
     /        `.    \  /
    |  O        \___/  |
~^~^~^~^~^~^~^~^~^~^~^~^~
            ~          ~
"""]


def generate_dot_grid(width=800, height=600):
    # Create a single row of dots
    row = '.' * width
    # Repeat the row for the specified height
    grid = '\n'.join([row for _ in range(height)])
    return grid


cloud=[




]


nashville_chord_progressions = [
    "1 5 6- 4",
    "1 4 6 4",
    "6- 4 5 1",
    "1 6- 4 5",
    "1 3- 4 5",
    "2- 5 1",
    "4 6- 2- 5",
    "1 4 6- 5",
    "3- 6- 2- 5",
    "1 5 6- 3-",
    "4 1 5 6-"
]






building =["""
   _______||__
  /\\\\\\\\\\\\
  | o      o  | 
  |     _      \
  |  0 | |  0   |
  +-------------+
 """,
"""
   _______||__
  /\\\\\\\\\\\\              
  | o      o  | 
  | o          _| 
  |    o      | 
  | o      o  |  
  |     _      \
  |  0 | |  0   |
  +-------------+
 """ 
 ,
"""
   _______||__
  /\\\\\\\\\\\\              
  | o      o  |                                                
  | o          _| 
  |    o      | 
  | o      o  |  
  |     _      \ \\\\\\\\
  |  0 | |  0   |        |
  +-------------+----------+ 
 """ 
   ]


dragon_art = [r"""                                            
    .-')          _
   (`_^ (    .----`/
    ` )  \_/`   __/     __,
    __{   |`  __/      /_/
   / _{    \__/ '--.  //
   \_> \_\  >__/    \((
        _/ /` _\_   |))
  jgs  /__(  /______/`

"""]

data_sample ="....................... "
tape_art = [  f"""
 ___________________________________________
|  _______________________________________  |
| / .-----------------------------------. \ |
| | | /\ :                        90 min| | |
| | |/--\:{data_sample           }NR [ ]| | |
| | `-----------------------------------' | |
| |      //- \   |         |   //-\       | |
| |     ||( )||  |_________|  ||( )||     | |
| |       \-//   :....:....:   \ -//      | |
| |       _ _ ._  _ _ .__|_ _.._  _       | |
| |      (_(_)| |(_(/_|  |_(_||_)(/_      | |
| |               low noise   |           | |
| `______ ____________________ ____ ______' |
|        /    []             []    \        |
|       /  ()                   ()  \       |
!______/_____________________________\______!
Simon Williams
""" ]

octo_art = [r"""
     C +------+C
   B+/          \+D
    |            |
    |   ?        |
   A+\          /+E
      G+------+F
""" ]

def menu(info=""):
    menu_ui = [f"""
[x][][][][][][][][] drums
[x][][][][][][][][] bass
[x][][][][][][][][] pad
[x][][][][][][][][] fx
[x][][][][][][][][] bass2
[x][][][][][][][][] melo 1
[x][][][][][][][][] melo 2
""" ] 
    return menu_ui[0]

screen2= "."# generate_dot_grid()

# Size of the shared memory buffer
SHARED_MEMORY_SIZE = 1024
SHARED_MEMORY_NAME = "my_memory"
 
# Create shared memory
shm = shared_memory.SharedMemory(name=SHARED_MEMORY_NAME, create=True, size=SHARED_MEMORY_SIZE)



class QualifierAutoSuggest(AutoSuggest):
    def get_suggestion(self, buffer, document):
        word_before_cursor = document.get_word_before_cursor()
        if word_before_cursor.startswith('@'):
            prefix = word_before_cursor[1:]  # Get the part after '@'
            suggestions = [q for q in qualifiers if q.startswith(prefix)]
            if suggestions:
                return Suggestion(suggestions[0][len(prefix):])  # Suggest the first match
        return None

qualifier_auto_suggest = QualifierAutoSuggest()

kb = KeyBindings()

historysize=0
historyselector=0

@kb.add('up')
def _(event):
    buffer = event.current_buffer
    global history_index,historyselector
    if buffer.history:
        historyselector+=1
        buffer.text = buffer.history.get_strings()[-(historyselector%historysize)]
        buffer.cursor_position = len(buffer.text)

@kb.add('down')
def _(event):
    buffer = event.current_buffer
    global history_index,historyselector
    if buffer.history:
        historyselector-=1
        buffer.text = buffer.history.get_strings()[-(historyselector%historysize)]
        buffer.cursor_position = len(buffer.text)


 
@kb.add('c-c')
def _(event):
    event.app.exit()


@kb.add('tab')
def _(event):
    buffer = event.current_buffer
    suggestion = buffer.suggestion
    if suggestion:
        buffer.insert_text(suggestion.text)

# Remove this key binding
@kb.add('[')
def _(event):
    event.app.current_buffer.insert_text('[]')
    event.app.current_buffer.cursor_left()



# Remove this key binding
@kb.add('<')
def _(event):
    event.app.current_buffer.insert_text('[C1 ]+[[1][5][4][1]]!!32')
    event.app.current_buffer.cursor_left()

# Remove this key binding
@kb.add('>')
def _(event):
    event.app.current_buffer.insert_text('[C1 C1]+[[1][6][5][4]]!!32')
    event.app.current_buffer.cursor_left()

#[F FFCCC F1FF0F4 FF [0F1F]!!4 F1FF FF  F F ]-24 


# Create the main display area
display_area_up = TextArea(
    read_only=True,
    scrollbar=True,
    wrap_lines=True )



history_auto_suggest = AutoSuggestFromHistory()


qualifiers = ["pop", "kk", "rock", "jazz", "classical"]  # Add more as needed

display_area_down = TextArea(read_only=True)
 
class CombinedAutoSuggest(AutoSuggest):
    def __init__(self, history, qualifiers):
        self.history_suggest = AutoSuggestFromHistory()
        self.qualifiers = qualifiers

    def get_suggestion(self, buffer, document):
        word_before_cursor = document.get_word_before_cursor()
        
        if word_before_cursor == '[':
            return Suggestion(']')
        
        if word_before_cursor.startswith('@'):
            prefix = word_before_cursor[1:]
            matching_qualifiers = [q for q in self.qualifiers if q.startswith(prefix)]
            if matching_qualifiers:
                return Suggestion(matching_qualifiers[0][len(prefix):])
        
        return self.history_suggest.get_suggestion(buffer, document)

    def get_matching_qualifiers(self, prefix):
        return [q for q in self.qualifiers if q.startswith(prefix)]

@kb.add('c-space')  # Ctrl+Space to show all matching qualifiers
def _(event):
    buffer = event.current_buffer
    word_before_cursor = buffer.document.get_word_before_cursor()
    if word_before_cursor.startswith('@'):
        prefix = word_before_cursor[1:]
        matching_qualifiers = event.app.auto_suggest.get_matching_qualifiers(prefix)
        if matching_qualifiers:
            display_area_up.text += f"\nMatching qualifiers: {', '.join(matching_qualifiers)}"
            display_area_up.buffer.cursor_position = len(display_area_up.text)


combined_auto_suggest = CombinedAutoSuggest(history,qualifiers)

# Create the input area with AutoSuggestFromHistory
input_area = TextArea(
    height=1,
    prompt='> ',
    history=history,
    auto_suggest=combined_auto_suggest,
)

# Create the side window areas
side_window_top = TextArea(read_only=True)
info_area = TextArea(text=building[0], read_only=True)
side_window_bottom = TextArea(text=skull_art[1], read_only=True, style="class:custom.red")
sample_fx_auto = TextArea(text= screen2, read_only=True, style="class:custom.red")
status_area =  TextArea(text=read_from_shared_memory(), read_only=True, style="class:custom.red") 
logo_area =  TextArea(text=dragon_art[0], read_only=True, style="class:custom.red") 

# Function to handle input submission
def accept_input(buff):
    global historysize
    text = input_area.text 
    display_area_up.text += f"\n{text}"   
    cursor_position = len(display_area_up.text)
    historysize+=1

    # Write to shared memory
    encoded_text = text.encode('utf-8')
    shm.buf[:len(encoded_text)] = encoded_text
    shm.buf[len(encoded_text)] = 0  # Null terminator
    shm.buf[len(encoded_text)+1:] = b'\0' * (len(shm.buf) - len(encoded_text) - 1)

    # Add to history
    history.append_string(text)

    input_area.text = ""
    display_area_up.buffer.cursor_position = len(display_area_up.text)

# Bind Enter key to accept_input when input_area is focused
@kb.add('enter', filter=has_focus(input_area))
def _(event):
    accept_input(event.app.current_buffer)

# Create the layout with ScrollablePane and ScrollbarMargin
scrollable_pane = ScrollablePane(
    content=display_area_up,
    show_scrollbar=True,
)    
 
# Create the layout
root_container = HSplit([
    VSplit([
        HSplit([
            Frame(side_window_top,  title="Infos", width=30),
            Frame(side_window_bottom, title="fish tank", style="class:custom.red", width=30),
            Frame(info_area, title="Additional Info", style="class:custom.blue", width=30)
        ]),
        HSplit([
            Frame(display_area_up, title="Sardine pilot compagnon ", style="class:custom.red"),
            Frame(sample_fx_auto, title="Sample fx auto", style="class:custom.red")
        ])
    ]),
    VSplit([
        Frame(status_area , width=30, title=" status "),  # Empty area to align with side windows
        Frame(input_area, title="Input")
    ])
])

layout = Layout(root_container)
layout.focus(input_area)


loading_frames = ["Loading   ", "Loading.  ", "Loading.. ", "Loading..."]
loading_content = FormattedTextControl(text=loading_frames[0], show_cursor=False)
loading_window = Window(content=loading_content, height=14)

# Create a formatted text for the title
title = FormattedText([('class:loading-title', "Welcome to Sardine Pilot Companion")])

# Create a window for the title
title_window = Window(content=FormattedTextControl(title), height=3)


text_window = Window(FormattedTextControl("Your text here"), height=1)




# Create a layout with a frame
loading_layout = Frame(
    HSplit([
        title_window,
        logo_area,  # Add the new text window here
        loading_window,
    ]),
    title="Loading...",
    style="class:loading-frame"
)
 

loading_layout1 = Layout(loading_layout)


async def switch_to_main_layout(app):
    app.layout = Layout(root_container)
    loading_frames = ["Loading   ", "Loading.  ", "Loading.. ", "Loading..."]
    frame = 0
    start_time = time.time()
    duration = 30  # Duration in seconds

    while time.time() - start_time < duration:
        loading_content.text = loading_frames[frame % len(loading_frames)]
        frame += 1
        await asyncio.sleep(0.5)  # Update every 0.5 seconds

    app.layout = Layout(root_container)
    app.layout.focus(input_area)  # Set focus to input_area
    app.invalidate()  # Force a redraw of the application



# Create and run the application
app = Application(layout=loading_layout1, full_screen=True, key_bindings=kb, style=style)

# def switch_to_main_layout(app):
#     def switch_layout():

#         time.sleep(30)  # Wait for 3 seconds before switching.
#         app.layout = Layout(root_container)
#         app.layout.focus(input_area)  # Set focus to input_area
#         app.invalidate()  # Force a redraw of the application
#     # Start a separate thread for switching layouts.
#     thread = threading.Thread(target=switch_layout)
#     thread.daemon = True  # Ensure thread exits when main program exits.
#     thread.start()


async def animate_loading():
    frame = 0
    duration = 30  # Duration in seconds
    start_time = time.time()

    while time.time() - start_time < duration:
        loading_content.text = loading_frames[frame % len(loading_frames)]+read_from_shared_memory()
        frame += 1
        app.invalidate()  # Force a redraw of the application
        await asyncio.sleep(0.1)  # Update every 0.5 seconds

    # Switch to main layout after loading duration
    switch_to_main_layout()

async def switch_to_main_layout(app):
    await asyncio.sleep(30)  # Wait for 30 seconds
    app.layout = Layout(root_container)
    app.layout.focus(input_area)  # Set focus to input_area
    app.invalidate()  # Force a redraw of the application
 


async def animate():
    while True:
        side_window_top.text = generate_rain(28, 5)
        side_window_bottom.text = update_skull_art()
        status_area.text = read_from_shared_memory()
        if ',' in user_input:
                info = read_from_shared_memory().split(',')
               # info_area.text = read_from_shared_memory()
        await asyncio.sleep(0.2)


async def run_app():
    # Switch to main layout after a delay.
    loading_task = asyncio.create_task(animate_loading())
    switch_layout_task = asyncio.create_task(switch_to_main_layout(app))
    animation_task = asyncio.create_task(animate())
    
    try:
        await app.run_async()
    finally:
        animation_task.cancel()
        try:
            await animation_task
        except asyncio.CancelledError:
            pass

if __name__ == "__main__":
    try:
        asyncio.run(run_app())
    finally:
        # Cleanup shared memory
        shm.close()
        shm.unlink()