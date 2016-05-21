
// FUNCTIONS ---------------------------------------------------------

function set_navbar_padding() {
	if (window.innerWidth > 550) {
		var padding = $('#main-container').css('margin-right');

		$('.navbar-default').css('padding-left', padding);
		$('.navbar-default').css('padding-right', padding);
	}
	else {
		$('.navbar-default').css('padding-left', 15);
		$('.navbar-default').css('padding-right', 15);
	}
}

function show_body() {
	var current_url = window.location.href
	
	if (current_url.indexOf("/blog/post/") != -1) { 
		$('.post-body').show();
		$('#tags-button').show();
		$('.repo-button').show();
	}
}

// EVENTS ------------------------------------------------------------

$(document).ready(function() {
	set_navbar_padding();
});

$(window).resize(function() {
	set_navbar_padding();
});

$(window).load(function() {
	show_body();

	$('#tags-button').click(function(e) {
		var postTags = $('.post-tags');
		
		if (postTags.css('display') == 'none') {
			postTags.show();
		}
		else {
			postTags.hide();
		}

		e.preventDefault();
	});

	set_navbar_padding();
});