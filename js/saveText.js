import { app } from "../../../scripts/app.js";

app.registerExtension({
    name: "SimpleSaveText",
    async beforeRegisterNodeDef(nodeType, nodeData, app) {
        if (nodeData.name === "SimpleSaveText") {

            // Add output_dir input field to the node UI
            const onNodeCreated = nodeType.prototype.onNodeCreated;
            nodeType.prototype.onNodeCreated = function () {
                const r = onNodeCreated ? onNodeCreated.apply(this, arguments) : undefined;
                this.size = [400, 250];

                // Create label and input for output_dir
                const label = document.createElement("label");
                label.textContent = "Output Directory:";
                label.style.display = "block";
                label.style.margin = "8px 0 2px 8px";

                const input = document.createElement("input");
                input.type = "text";
                input.placeholder = "Leave blank for default";
                input.style.width = "90%";
                input.style.margin = "0 8px 8px 8px";
                input.value = this.widgets_values?.[2] ?? "";

                input.addEventListener("change", () => {
                    // Save value to widgets_values (third input)
                    this.widgets_values = this.widgets_values || [];
                    this.widgets_values[2] = input.value;
                });

                // Attach to node DOM
                if (this?.canvas && this?.canvas.parentNode) {
                    this.canvas.parentNode.appendChild(label);
                    this.canvas.parentNode.appendChild(input);
                } else {
                    document.body.appendChild(label);
                    document.body.appendChild(input);
                }

                // Store reference for later
                this._outputDirInput = input;

                return r;
            };

            // ...existing code for preview...
            function showPreview(text) {
                // Remove any existing preview
                if (this._previewEl && this._previewEl.parentNode) {
                    this._previewEl.parentNode.removeChild(this._previewEl);
                }

                // Create preview element (read-only, not persisted)
                const preview = document.createElement("pre");
                preview.textContent = Array.isArray(text) ? text.flat().join("\n") : (text ?? "");
                preview.style.whiteSpace = "pre-wrap";
                preview.style.background = "rgba(0,0,0,0.2)";
                preview.style.color = "white";
                preview.style.padding = "8px";
                preview.style.margin = "8px";
                preview.style.borderRadius = "4px";
                preview.style.fontFamily = "monospace";
                preview.style.maxHeight = "200px";
                preview.style.overflowY = "auto";
                preview.style.userSelect = "text";
                preview.style.fontSize = "13px";
                preview.style.pointerEvents = "none"; // Not interactive

                // Attach to node's DOM element (not persisted)
                this._previewEl = preview;
                if (this?.canvas && this?.canvas.parentNode) {
                    this.canvas.parentNode.appendChild(preview);
                } else {
                    document.body.appendChild(preview);
                }
            }

            const onExecuted = nodeType.prototype.onExecuted;
            nodeType.prototype.onExecuted = function (message) {
                onExecuted?.apply(this, arguments);
                if (message?.text) {
                    showPreview.call(this, message.text);
                } else if (this._previewEl && this._previewEl.parentNode) {
                    // Remove preview if no text returned
                    this._previewEl.parentNode.removeChild(this._previewEl);
                    this._previewEl = null;
                }
            };
        }
    },
});