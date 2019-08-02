$("form#form-subscription").submit(function () {
    var urlForm = $(this).attr('action')
    $.ajax({
        url: urlForm,
        type: "POST",
        dataType: "json",
        data: {
            email: $(".email-sub").val(),
        },
        success: function () {
            location.reload()
        }
    })

    return false
})

$("form#form-subscription").formValidation({
    framework: 'bootstrap',
    icon: {
        valid: 'glyphicon glyphicon-ok',
        invalid: 'glyphicon glyphicon-remove',
        validating: 'glyphicon glyphicon-refresh'
    },
    fields: {
        emailsubscription: {
            validators: {
                notEmpty: {
                    message: 'Email is required'
                },
            }
        }
    }
})