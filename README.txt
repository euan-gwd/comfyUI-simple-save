# ComfyUI Simple Save & Copy Text

A lightweight, high-performance custom node for ComfyUI that allows you to preview, copy, and optionally save text outputs (like prompts, lyrics, or logs) directly to your output folder.

## Features
- **Persistent Preview**: Unlike standard text previews, this node retains the text inside the UI even when you switch browser tabs or windows.
- **Selectable & Copyable**: The text box is specifically styled to allow you to highlight and copy text directly from the ComfyUI interface.
- **Optional Save to Disk**: A toggle allows you to choose whether to write a `.txt` file to your `ComfyUI/output` folder or just view it in the UI.
- **Auto-Timestamping**: When saving is enabled, files are automatically named with a timestamp to prevent overwriting previous runs.

## Installation

### Manual Installation
1. Navigate to your ComfyUI custom nodes directory:
   `ComfyUI/custom_nodes/`
2. Create a folder named `ComfyUI_SimpleSaveText`.
3. Place the following files inside that folder:
   - `__init__.py`
   - `save_text_node.py`
   - `js/save_show.js`
4. Restart ComfyUI and refresh your browser.

## How to Use
1. Right-click the canvas and search for **"💾 Save & Copy Text"**.
2. Connect any **STRING** output to the `text` input.
3. **save_to_disk**: Set to `True` to create a file in your output folder, or `False` to use it as a simple clipboard tool.
4. **filename_prefix**: Customize the beginning of the saved filename.

## License
MIT