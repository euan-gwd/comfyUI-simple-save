# ComfyUI Simple Save & Show Text

A lightweight, high-performance custom node set for ComfyUI that allows you to preview, copy, and save text outputs (like prompts, lyrics, or logs) directly to your output folder.

## Features
- **Persistent Preview**: The Show Text node retains the text inside the UI even when you switch browser tabs or windows.
- **Selectable & Copyable**: The Show Text node allows you to highlight and copy text directly from the ComfyUI interface.
- **Save to Disk**: The Save Text node writes a `.txt` file to your `ComfyUI/output` folder.
- **Auto-Timestamping**: Saved files are automatically named with a timestamp to prevent overwriting previous runs.
- **Simple Status Output**: The Save Text node returns a message indicating success or failure.
- **Preview Saved Text**: The Save Text node displays a non-interactive preview of the text that was saved, directly on the node in the UI.

## Installation

### Manual Installation
1. Navigate to your ComfyUI custom nodes directory:
   `ComfyUI/custom_nodes/`
2. Create a folder named `comfyUI-simple-save`.
3. Place the following files inside that folder:
   - `__init__.py`
   - `save_text.py`
   - `show_text.py`
   - `js/saveText.js`
   - `js/showText.js`
4. Restart ComfyUI and refresh your browser.

## How to Use

### Show Text Node
1. Right-click the canvas and search for **"Show Text 🐍"**.
2. Connect any **STRING** output to the `text` input.
3. The text will be displayed in the UI and can be copied.

### Save Text Node
1. Right-click the canvas and search for **"Save Text 💾"**.
2. Connect any **STRING** output to the `text` input.
3. Set `filename_prefix` to customize the beginning of the saved filename.
4. The node will save the text to a file in your output folder and return a status message.
5. After execution, a non-interactive preview of the saved text will appear on the node for quick reference.

## License
MIT