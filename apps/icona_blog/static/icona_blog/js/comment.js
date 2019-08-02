$(".button-public").click(function () {
    $(".form-comment").show()
    $(this).hide()
})


$("form#comment").formValidation({
    framework: 'bootstrap',
    icon: {
        valid: 'glyphicon glyphicon-ok',
        invalid: 'glyphicon glyphicon-remove',
        validating: 'glyphicon glyphicon-refresh'
    },
    fields: {
        name: {
            validators: {
                notEmpty: {
                    message: 'Nome is required'
                },
            }
        },
        email: {
            validators: {
                notEmpty: {
                    message: 'Email is required'
                },
            }
        },
    }
})