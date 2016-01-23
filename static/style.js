$( "select" ).change(function() {
    var text = $( "#school option:selected" ).text();
    if (text == "Other") {
	$("#other").html("<input type='text' name='other' class='form-control input-lg' placeholder='Input Your School'  required>");
    }
    else {
	$("#other").html("");
    }
});
