$('document').ready(function() {
	$.get('https://hellosalut.stefanbohacek.dev/?lang=fr', function(data.hello) {
		$('DIV#hello').text(data);
	});
});
