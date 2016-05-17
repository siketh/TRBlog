$(window).load(function() {
	var current_url = window.location.href
	
	if (current_url.indexOf("/blog/post/") != -1) { 
		$('.post-body').show();
		$('#tags-button').show();
		$('.repo-button').show();
		//$('#comments-button').show();
	}

	$('#tags-button').click(function(e) {
		var postTags = $('.post-tags');
		
		if(postTags.css('display') == 'none') {
			postTags.show();
		}
		else {
			postTags.hide();
		}

		e.preventDefault();
	});

	/*
	$('#comments-button').click(function() {
		if($('.post-comments').css('display') == 'none') {
			$('.post-comments').show();
			$('.post-comments').css('height', 'auto');
		}
		else {
			$('.post-comments').hide();
		}
	});
	*/
});