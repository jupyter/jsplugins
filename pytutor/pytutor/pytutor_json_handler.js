var pytutor_json_handler = function (json, element) {
    var id = 'optviz-'+IPython.utils.uuid();
    var toinsert = $("<div/>").attr('id',id);
    element.append(toinsert);
    var viz = new ExecutionVisualizer(toinsert, json, {embeddedMode: true});
    $(window).resize(function() {
        viz.redrawConnectors();
    });
}

IPython.json_handlers.register_handler('pytutor', pytutor_json_handler)
