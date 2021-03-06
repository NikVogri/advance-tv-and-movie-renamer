# -----------------------------------------------------------
# Render initial application using tkinter
# Author Nik Vogrinec - https://github.com/nikvogri
# -----------------------------------------------------------

from tkinter import *
from lib.functions import *
from lib.UI.Text import Text

root = Tk()
root.title("Advance Movie & TV Show renamer")
root.resizable(False, False)


def render_ui():
    files = []

    canvas = tk.Canvas(root, height=700, width=1200)
    canvas.pack()

    selector_frame = tk.Frame(
        root, bg="#fefefe", highlightbackground="#f0f0f0", highlightthickness=0.5)

    selector_frame.place(relwidth=0.5, relheight=0.75)

    result_frame = tk.Frame(
        root, bg="#fefefe", highlightbackground="#f0f0f0", highlightthickness=0.5)
    result_frame.place(relwidth=0.5, relheight=0.75, relx=0.5)

    upload_file_button = tk.Button(
        selector_frame, text="Select file/files", command=lambda: add_files_to_rename(selector_frame, files))
    upload_file_button.pack(side=tk.BOTTOM)

    upload_dir_button = tk.Button(
        selector_frame, text="Select folder", command=lambda: search_dir_files(selector_frame, files))
    upload_dir_button.pack(side=tk.BOTTOM)

    configuration_frame = tk.Frame(
        root, highlightbackground="#f0f0f0", highlightthickness=0.5, bg="#fefefe")
    configuration_frame.place(relwidth=1, relheight=0.25, rely=1)

    configuration_frame_labels = tk.Frame(
        configuration_frame, width=400, height=173).place(x=0)
    tk.Frame(
        configuration_frame, width=600, height=173).place(x=200)
    tk.Frame(
        configuration_frame, width=400, height=173).place(x=400)

    tk.Label(configuration_frame_labels,
             text="Desired format: ").place(x=10, y=570)

    tk.Label(configuration_frame_labels,
             text="Title - #title# - Game of Thones \n Year - #year# - 2011 \n Season - #season - 1 \n Episode - #episode# - 1 \n Episode title - #episodeTitle# - Winter is coming \n Prefix episode - #pEpisode# - 01 \n Prefix season - #pSeason# - 01").place(
        x=700, y=570)

    format_input = Text(configuration_frame_labels,
                        width=100).position(x=10, y=590)

    tk.Button(configuration_frame_labels, text="Preview", height=3,
              width=11, command=lambda: preview_file_names(result_frame, format_input, files)).place(x=1100, y=550)

    tk.Button(configuration_frame_labels, text="Rename", height=3, width=11,
              command=lambda: convert_file_names(root, [selector_frame, result_frame], files)).place(
        x=1100, y=620)

    tk.Button(configuration_frame_labels, text="Save format", height=1,
              width=10, command=lambda: save_format(format_input)).place(x=10, y=615)

    tk.Button(configuration_frame_labels, text="Select path", height=1,
              width=10, command=lambda: select_path_directory(format_input)).place(x=100, y=615)

    format_input.set_cached_value()
    root.protocol("WM_DELETE_WINDOW", lambda: handle_graceful_close(root))
    root.mainloop()
