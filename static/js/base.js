jQuery(function($) {

    function adjustNav() {
        var winWidth = $(window).width(),
            dropdown = $('.dropdown'),
            dropdownMenu = $('.dropdown-menu');

        if (winWidth >= 768) {
            dropdown.on('mouseenter', function() {
                $(this).addClass('show')
                    .children(dropdownMenu).addClass('show');
            });

            dropdown.on('mouseleave', function() {
                $(this).removeClass('show')
                    .children(dropdownMenu).removeClass('show');
            });

        } else {
            dropdown.off('mouseenter mouseleave');
        }
    }

    $(window).on('resize', adjustNav);

    adjustNav();
});

/* When the user scrolls down, hide the navbar. When the user scrolls up, show the navbar */
var prevScrollpos = window.pageYOffset;
window.onscroll = function() {
    var currentScrollPos = window.pageYOffset;
    if (prevScrollpos > currentScrollPos) {
        document.getElementById("header").classList.add("showing")
        document.getElementById("header").classList.remove("hiding")

    } else {
        document.getElementById("header").classList.add("hiding")
        document.getElementById("header").classList.remove("showing")
    }
    prevScrollpos = currentScrollPos;
}

// Delete session variable on tab close - not working

$(window).unload(function() {
    $.sessionStorage.removeItem('investor_password');
});