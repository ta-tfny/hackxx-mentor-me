$(document).ready(() => {

    $('#next-btn').click(() => {
        const firstName = $('#first-name').val().trim();
        const lastName = $('#last-name').val().trim();
        
        $.post('/next-page', {
            "first": firstName,
            "last": lastName
        }, function (data) {
            if (data === 'done') {
                $(location).attr('href', '/second-page');
            }
        });
    });
});

