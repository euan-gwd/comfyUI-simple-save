class SimpleShowText:
    @classmethod
    def INPUT_TYPES(s):
        return {
            "required": {
                "text": ("STRING", {"forceInput": True}),
            },
            "hidden": {
                "unique_id": "UNIQUE_ID",
                "extra_pnginfo": "EXTRA_PNGINFO",
            },
        }

    INPUT_IS_LIST = True
    RETURN_TYPES = ("STRING",)
    FUNCTION = "notify"
    OUTPUT_NODE = True
    OUTPUT_IS_LIST = (True,)

    CATEGORY = "SimpleText"

    def notify(self, text, unique_id=None, extra_pnginfo=None):
        # Default to the input text if no unique_id or extra_pnginfo is available
        # or if there's an issue parsing workflow info.
        text_to_display = text[0] if text and isinstance(text, list) else "" # Assume text is a list, take the first element

        if unique_id is not None and extra_pnginfo is not None:
            # Error handling for extra_pnginfo structure
            if not isinstance(extra_pnginfo, list) or not extra_pnginfo:
                print("Error: extra_pnginfo is not a list or is empty")
            elif not isinstance(extra_pnginfo[0], dict) or "workflow" not in extra_pnginfo[0]:
                print("Error: extra_pnginfo[0] is not a dict or missing 'workflow' key")
            else:
                workflow = extra_pnginfo[0]["workflow"]
                node_id_str = str(unique_id[0]) # unique_id is a list
                node = next(
                    (x for x in workflow["nodes"] if str(x["id"]) == node_id_str),
                    None,
                )
                if node:
                    # If widgets_values exist and are not empty, use the first one (edited text)
                    # Note: widgets_values stores the edited text from the frontend
                    if "widgets_values" in node and node["widgets_values"]:
                        # Ensure widgets_values is a list before accessing index 0
                        if isinstance(node["widgets_values"], list) and node["widgets_values"]:
                            text_to_display = node["widgets_values"][0]
                        else:
                            # If widgets_values is malformed or empty, reset it with input text
                            node["widgets_values"] = [text_to_display]
                    else:
                        # If no widgets_values (first run or reset), use the input text
                        # and initialize widgets_values to save it in the workflow
                        node["widgets_values"] = [text_to_display]
        
        # Always return the text that was determined to be displayed
        return {"ui": {"text": [text_to_display]}, "result": (text_to_display,)}


NODE_CLASS_MAPPINGS = {
    "ShowText|SimpleText": SimpleShowText,
}

NODE_DISPLAY_NAME_MAPPINGS = {
    "ShowText|SimpleText": "Show Text 🐍",
}