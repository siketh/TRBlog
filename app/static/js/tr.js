$(window).load(function() {
	var current_url = window.location.href
	if (current_url.indexOf("/blog/post/") != -1) { 
		$('.post-body').show();
	}
});