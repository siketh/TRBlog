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
    var current_url = window.location.href;
    var dev_url = 'http://localhost:5000/';
    var prod_url = 'http:/www.trevorroman.com/';

    if (current_url.indexOf(dev_url + "blog/post/") == 0 ||
        current_url.indexOf(prod_url + "blog/post/") == 0)  {
        $('.post-body').show();
        $('#tags-button').show();
        $('.repo-button').show();
    }
    else if (current_url == dev_url || current_url == prod_url) {
        $('.post-body').show();
    }
}

function listen_for_clicks() {
    $('#tags-button').click(function (e) {
        var postTags = $('.post-tags');

        if (postTags.css('display') == 'none') {
            postTags.show();
        }
        else {
            postTags.hide();
        }

        e.preventDefault();
    });
}

// EVENTS ------------------------------------------------------------

$(document).ready(function () {
    set_navbar_padding();
});

$(window).resize(function () {
    set_navbar_padding();
});

$(window).load(function () {
    show_body();
    set_navbar_padding();
    listen_for_clicks();
});