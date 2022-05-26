$(document).ready(function () {
    // Smooth Anchor Scrolling
    $('a').click(function () {
        $('html, body').animate({
            scrollTop: $($(this).attr('href')).offset().top
        }, 500);
        return false;
    });
});
