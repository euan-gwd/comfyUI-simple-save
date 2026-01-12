import os
from datetime import datetime
import folder_paths

class SimpleSaveText:
    def __init__(self):
        self.output_dir = folder_paths.get_output_directory()

    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "text": ("STRING", {"forceInput": True}),
                "save_to_disk": ("BOOLEAN", {"default": False}),
                "filename_prefix": ("STRING", {"default": "Prompt_"}),
                "save_location": ("STRING", {"default": ""}),
            }
        }

    RETURN_TYPES = ("STRING",)
    FUNCTION = "save_it"
    OUTPUT_NODE = True
    CATEGORY = "CustomNodes"

    def save_it(self, text, save_to_disk, filename_prefix, save_location):
        # Only save to file if the toggle is enabled
        if save_to_disk:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            filename = f"{filename_prefix}_{timestamp}.txt"
            # Use save_location if provided and valid, else default output_dir
            target_dir = save_location.strip() if save_location.strip() else self.output_dir
            if not os.path.isabs(target_dir):
                target_dir = os.path.join(self.output_dir, target_dir)
            os.makedirs(target_dir, exist_ok=True)
            file_path = os.path.join(target_dir, filename)

            with open(file_path, "w", encoding="utf-8") as f:
                f.write(text)
            print(f"Text saved to: {file_path}")
        else:
            print("Save to disk disabled. Text only displayed in UI.")

        # Always return to UI so the box updates
        return {
            "ui": {
                "text": [text],
                "default_save_location": self.output_dir
            },
            "result": (text,)
        }
