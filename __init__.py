# In __init__.py
from .save_text_node import SimpleSaveText

NODE_CLASS_MAPPINGS = {"SimpleSaveText": SimpleSaveText}
NODE_DISPLAY_NAME_MAPPINGS = {"SimpleSaveText": "💾 Save & Copy Text"}
WEB_DIRECTORY = "./js"
__all__ = ["NODE_CLASS_MAPPINGS", "NODE_DISPLAY_NAME_MAPPINGS", "WEB_DIRECTORY"]