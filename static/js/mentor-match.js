$(document).ready(() => {

    $.get('/best-mentor', (data) => {
        $('#mentor-info').html(data);
    });

});