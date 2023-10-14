def block():
    return """
    <div id="draggable" class="ui-widget-content">
        <script>
            $( function() {
            $( "#draggable" ).draggable();
            } );
        </script>
        <button id="add_button" 
                class="button-delete" 
                type="button" 
                hx-post="/add/textarea" 
                hx-target="#add_button" 
                hx-swap="outerHTML">
            <img src="/static/images/plus.svg" width="20px" height="20px"></img>
        </button>
        <button id="minus_button" 
            class="button-delete" 
            type="button" 
            hx-delete="/remove/textarea" 
            hx-target="#code_box" 
            hx-swap="outerHTML">
            <img src="/static/images/minus.svg" width="20px" height="20px"></img>
        </button>
        <button class="button-delete" 
                type="button" 
                hx-delete="/delete/block" 
                hx-target="closest div"
                hx-swap="outerHTML">
            <img src="/static/images/garbage.svg" width="20px" height="20px"></img>
        </button>
        <button class="button-delete" 
                type="button">
            <img src="/static/images/send.svg" width="20px" height="20px">
        </button>
    </div>"""

def new_textarea():
    return """
    <form id="code_box">
        <script>
            HTMLTextAreaElement.prototype.setCaretPosition = function (position) {
                this.selectionStart = position;
                this.selectionEnd = position;
            };
        </script>
        <textarea 
            name="codebox"
            hx-on:keydown="
                var textarea = this; 
                if (event.keyCode == 9) {
                        var newCaretPosition;
                        newCaretPosition = textarea.selectionStart + '    '.length;
                        textarea.value = textarea.value.substring(0, textarea.selectionStart) + '    ' + textarea.value.substring(textarea.selectionStart, textarea.value.length);
                        textarea.setCaretPosition(newCaretPosition);
                        return false;
                    }"
            class="text-area"></textarea>
    </form>
"""

def remove_text_area():
    return """
    <button id="add_button" class="button-delete" type="button" hx-post="/add/textarea" hx-target="#add_button" hx-swap="outerHTML">
        <img src="/static/images/plus.svg" width="20px" height="20px"></img>
    </button>
"""