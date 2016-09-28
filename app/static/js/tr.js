// FUNCTIONS ---------------------------------------------------------

function set_navbar_padding() {
    if (window.innerWidth > 550) {
        var main_container_margin = $('#main-container').offset().left + 'px';

        $('.navbar-default').css('padding-left', main_container_margin);
        $('.navbar-default').css('padding-right', main_container_margin);
    }
    else {
        $('.navbar-default').css('padding-left', '15px');
        $('.navbar-default').css('padding-right', '15px');
    }
}

function show_posts() {
    $('#posts-container').show();
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
        $('.repo-button').show();
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
    var current_url = window.location.href;
    var home_page_url = window.location.protocol + "//" + window.location.host + "/";
    var blog_post_path = "/blog/post/";

    if (current_url == home_page_url || current_url.indexOf(blog_post_path) > -1) {
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
    set_navbar_padding();
    show_body();
    show_posts();
    listen_for_clicks();
});