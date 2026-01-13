# In __init__.py
from .save_text_node import SimpleSaveText
from .show_text import ShowText

NODE_CLASS_MAPPINGS = {"SimpleSaveText": SimpleSaveText, "ShowText|pysssss": ShowText,}
NODE_DISPLAY_NAME_MAPPINGS = {"SimpleSaveText": "💾 View & Save Text", "ShowText|pysssss": "Show Text 🐍",}
WEB_DIRECTORY = "./js"
__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS", "WEB_DIRECTORY"]