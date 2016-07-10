// FUNCTIONS ---------------------------------------------------------

function set_navbar_padding() {
    if (window.innerWidth > 550) {
        var padding = parseInt($('#main-container').css('margin-right'));

        $('.navbar-default').css('padding-left', padding);
        $('.navbar-default').css('padding-right', padding);
    }
    else {
        $('.navbar-default').css('padding-left', 15);
        $('.navbar-default').css('padding-right', 15);
    }
}

function show_body() {
    var current_path = window.location.pathname;

    if (current_path.indexOf("/blog/post/") == 0)  {
        $('.post-body').show();
        $('#tags-button').show();
        $('.repo-button').show();
    }
    else if (current_path == "/") {
        $('.post-body').show();
    }
}

function listen_for_clicks() {
    $('#tags-button').click(function (e) {
        var post_tags = $('.post-tags');

        if (post_tags.css('display') == 'none') {
            post_tags.show();
        }
        else {
            post_tags.hide();
        }

        e.preventDefault();
    });
}

function remove_homepage_anchor() {
    var href = window.location.href;

    if (href == window.location.protocol + "//" + window.location.host + "/") {
        var post_title_text = $('.post-title a').contents();
        $('.post-title a').replaceWith(post_title_text);
    }
}

// EVENTS ------------------------------------------------------------

$(document).ready(function () {
    set_navbar_padding();
    remove_homepage_anchor();
});

$(window).resize(function () {
    set_navbar_padding();
});

$(window).load(function () {
    show_body();
    set_navbar_padding();
    listen_for_clicks();
});