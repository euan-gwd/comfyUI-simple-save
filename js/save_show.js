import { app } from "../../../scripts/app.js";
import { ComfyWidgets } from "../../../scripts/widgets.js";

app.registerExtension({
    name: "SimpleSave.ShowText",
    async beforeRegisterNodeDef(nodeType, nodeData, app) {
        if (nodeData.name === "SimpleSaveText") {

            const onNodeCreated = nodeType.prototype.onNodeCreated;
            nodeType.prototype.onNodeCreated = function () {
                const r = onNodeCreated ? onNodeCreated.apply(this, arguments) : undefined;

                // 1. Find or Create the display widget
                const w = ComfyWidgets["STRING"](this, "display_text", ["STRING", { multiline: true }], app).widget;

                // 2. Setup Selection/Copy properties
                w.inputEl.readOnly = true;
                w.inputEl.style.cursor = "text";
                w.inputEl.style.userSelect = "text";
                w.inputEl.style.color = "white";
                w.inputEl.placeholder = "Run character builder to see text...";

                this.size = [400, 250];
                return r;
            };

            const onExecuted = nodeType.prototype.onExecuted;
            nodeType.prototype.onExecuted = function (message) {
                onExecuted?.apply(this, arguments);
                if (message?.text) {
                    const w = this.widgets.find((w) => w.name === "display_text");
                    if (w) {
                        w.value = message.text[0];
                    }
                }
            };
        }
    },
});