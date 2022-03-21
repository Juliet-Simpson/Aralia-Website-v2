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

//Try to put navbar in same layer and push content down when content is scrolled to top
// if (window.pageYOffset == 0.0) {
//     document.getElementById("header").classList.add("view-all")
// }