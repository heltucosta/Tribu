$('.addComp').click(function(){
    console.log("Clicou");
    appendString = "<div class='form-group'> \
		    	<input type='text' class='form-control'>\
			<input type='number' class='form-control'\
		</div>"
    $("form").append(appendString);
})
