$("form#form-login").formValidation({
    framework: 'bootstrap',
    icon: {
        valid: 'glyphicon glyphicon-ok',
        invalid: 'glyphicon glyphicon-remove',
        validating: 'glyphicon glyphicon-refresh'
    },
    fields: {
        email: {
            validators: {
                notEmpty: {
                    message: 'Email is required'
                },
            }
        },
        password: {
            validators: {
                notEmpty: {
                    message: 'Password is required'
                },
            }
        },
    }
})
