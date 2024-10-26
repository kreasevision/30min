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



def update_skull_art():
    current_time = time.time()
    index = int(current_time) % len(skull_art)  # Alternates between indices based on time
    return skull_art[index]+"   ❤️❤️❤️❤️❤️❤️❤️ "


skull_art = [r"""
         .
         ":"
       ___:____     |"\/"|
     ,'        `.    \  /
     |  n        \___/  |
  ~^~^~^~^~^~^~^~^~^~^~^~^~
~          ~
""",r"""
         0
        °°°
      ___°____    |"\/"|
    ,'        `.   \  /
    |  --        \_/  |
 ~^~^~^~^~^~^~^~^~^~^~^~^~
       ~          ~
"""
,r"""
          0
        °°°
      ___°____     |"\/"|
    ,'        `.    \  /
    |  O        \___/  |
~^~^~^~^~^~^~^~^~^~^~^~^~
            ~          ~
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
       +------+
    +/          \+
    |            |
    |            |
    +\          /+
       +------+
""" ]


# Size of the shared memory buffer
SHARED_MEMORY_SIZE = 1024
SHARED_MEMORY_NAME = "my_memory"
 
# Create shared memory
shm = shared_memory.SharedMemory(name=SHARED_MEMORY_NAME, create=True, size=SHARED_MEMORY_SIZE)


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

@kb.add('c-c')
def _(event):
    event.app.exit()



# Create the main display area
display_area_up = TextArea(
    read_only=True,
    scrollbar=True,
    wrap_lines=True )



display_area_down = TextArea(read_only=True)

# Create the input area with AutoSuggestFromHistory
input_area = TextArea(
    height=1,
    prompt='> ',
    history=history,
    auto_suggest=AutoSuggestFromHistory(),
)

# Create the side window areas
side_window_top = TextArea(read_only=True)
side_window_bottom = TextArea(text=skull_art[1], read_only=True, style="class:custom.red")
sample_fx_auto = TextArea(text=tape_art[0], read_only=True, style="class:custom.red")



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
            Frame(side_window_top, title="Infos", width=30),
            Frame(side_window_bottom, title="fish tank", style="class:custom.red", width=30)
        ]),
        HSplit([
            Frame(display_area_up, title="Sardine pilot compagnon ", style="class:custom.red"),
            Frame(sample_fx_auto, title="Sample fx auto", style="class:custom.red")
        ])
    ]),
    VSplit([
        Frame(TextArea(height=1), width=30),  # Empty area to align with side windows
        Frame(input_area, title="Input")
    ])
])

layout = Layout(root_container)
layout.focus(input_area)



# Create and run the application
app = Application(layout=Layout(loading_window), full_screen=True, key_bindings=kb, style=style)

def switch_to_main_layout(app):
    def switch_layout():
        time.sleep(3)  # Wait for 3 seconds before switching.
        app.layout = Layout(root_container)
        app.layout.focus(input_area)  # Set focus to input_area
        app.invalidate()  # Force a redraw of the application
    # Start a separate thread for switching layouts.
    thread = threading.Thread(target=switch_layout)
    thread.daemon = True  # Ensure thread exits when main program exits.
    thread.start()



async def update_display():
    while True:
        side_window_bottom.text = update_skull_art()
        await asyncio.sleep(0.5)  # Update every 0.5 seconds

async def animate():
    while True:
        side_window_top.text = generate_rain(28, 5)
        side_window_bottom.text = update_skull_art()
        await asyncio.sleep(0.5)


async def run_app():
    # Switch to main layout after a delay.
    switch_to_main_layout(app)

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