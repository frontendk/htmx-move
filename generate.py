def block():
    return """
    <div id="draggable" class="ui-state-default">
        <script>
            $( function() {
            $( "#draggable" ).draggable();
            } );
            $( function() {
            $( "#sortable" ).sortable();
            } );
        </script>
        <p>Drag me around</p>
        <div id="editable" contentEditable="true"></div>
        <button type="button" hx-delete="/delete/block" hx-target="#draggable" hx-swap="outerHTML">Delete</button>
    </div>"""
