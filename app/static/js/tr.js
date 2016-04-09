$(window).load(function() {
	var current_url = window.location.href
	if (current_url.indexOf("/blog/post/") != -1) { 
		$('.post-body').show();
		$('.show-comments-button').show();
	}

	$('.show-comments-button').click(function() {
		if($('.post-comments').css('display') == 'none') {
			$('.post-comments').show();
			$('.post-comments').css('height', 'auto');
		}
		else {
			$('.post-comments').hide();
		}
	});
});