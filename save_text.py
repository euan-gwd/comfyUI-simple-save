import os
from datetime import datetime
import folder_paths

class SimpleSaveText:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "text": ("STRING", {"forceInput": True}),
                "filename_prefix": ("STRING", {"default": "Prompt_"}),
            },
            "optional": {
                "output_dir": ("STRING", {"default": ""}),
                "placeholder": "e.g. /documents/prompts (leave blank for default)"
            },
        }

    INPUT_IS_LIST = True
    RETURN_TYPES = ("STRING",)
    FUNCTION = "save_it"
    OUTPUT_NODE = True
    OUTPUT_IS_LIST = (True,)
    CATEGORY = "SimpleText"

    def save_it(self, text, filename_prefix, output_dir=""):
        if not output_dir:
            output_dir = folder_paths.get_output_directory()
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"{filename_prefix}_{timestamp}.txt"
        file_path = os.path.join(output_dir, filename)

        try:
            os.makedirs(output_dir, exist_ok=True)
            with open(file_path, "w", encoding="utf-8") as f:
                f.write(text)
            message = f"Text saved to: {file_path}"
            return (message,)
        except Exception as e:
            error_message = f"Failed to save text: {e}"
            return (error_message,)

NODE_CLASS_MAPPINGS = {
    "SaveText|SimpleText": SimpleSaveText,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "SaveText|SimpleText": "Save Text 💾",
}