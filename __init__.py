from .save_text import SimpleSaveText
from .show_text import SimpleShowText

NODE_CLASS_MAPPINGS = {
    "SaveText|SimpleText": SimpleSaveText,
    "ShowText|SimpleText": SimpleShowText,
}
NODE_DISPLAY_NAME_MAPPINGS = {
    "SaveText|SimpleText": "Save Text 💾",
    "ShowText|SimpleText": "Show Text 🐍",
}
WEB_DIRECTORY = "./js"
__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS", "WEB_DIRECTORY"]