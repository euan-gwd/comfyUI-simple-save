import { app } from "../../../scripts/app.js";
import { ComfyWidgets } from "../../../scripts/widgets.js";

app.registerExtension({
    name: "SimpleSave.ShowText",
    async beforeRegisterNodeDef(nodeType, nodeData, app) {
        if (nodeData.name === "SimpleSaveText") {

            function populate(text) {
                if (this.widgets) {
                    // Remove all widgets except the converted input widget if present
                    const isConvertedWidget = +!!this.inputs?.[0]?.widget;
                    for (let i = isConvertedWidget; i < this.widgets.length; i++) {
                        this.widgets[i].onRemove?.();
                    }
                    this.widgets.length = isConvertedWidget;
                }

                const v = [...text];
                if (!v[0]) v.shift();
                for (let list of v) {
                    if (!(list instanceof Array)) list = [list];
                    for (const l of list) {
                        const w = ComfyWidgets["STRING"](this, "display_text_" + (this.widgets?.length ?? 0), ["STRING", { multiline: true }], app).widget;
                        w.inputEl.readOnly = true;
                        w.inputEl.style.cursor = "text";
                        w.inputEl.style.userSelect = "text";
                        w.inputEl.style.color = "white";
                        w.inputEl.placeholder = "Run character builder to see text...";
                        w.value = l;
                    }
                }

                requestAnimationFrame(() => {
                    const sz = this.computeSize();
                    if (sz[0] < this.size[0]) sz[0] = this.size[0];
                    if (sz[1] < this.size[1]) sz[1] = this.size[1];
                    this.onResize?.(sz);
                    app.graph.setDirtyCanvas(true, false);
                });
            }

            const onExecuted = nodeType.prototype.onExecuted;
            nodeType.prototype.onExecuted = function (message) {
                onExecuted?.apply(this, arguments);
                if (message?.text) {
                    populate.call(this, message.text);
                }
            };

            // Optionally, set a default size on node creation
            const onNodeCreated = nodeType.prototype.onNodeCreated;
            nodeType.prototype.onNodeCreated = function () {
                const r = onNodeCreated ? onNodeCreated.apply(this, arguments) : undefined;
                this.size = [400, 250];
                return r;
            };
        }
    },
});