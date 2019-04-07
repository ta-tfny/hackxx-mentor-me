$(document).ready(() => {

    $('#submit-btn').click(() => {
        const bio = $('#bio').val().trim();
        let companies = $('#companies-text-area').val().trim();

        $.post('/add-new-user', {
            "bio": bio,
            "companies": companies
        }, function (data) {
            if (data === 'done') {
                
            }
        });
    });
});

