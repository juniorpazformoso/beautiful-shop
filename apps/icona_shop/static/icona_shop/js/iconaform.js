function validators(){
    $("form").formValidation({
        framework: 'bootstrap',
        icon: {
            valid: 'glyphicon glyphicon-ok',
            invalid: 'glyphicon glyphicon-remove',
            validating: 'glyphicon glyphicon-refresh'
        },
        fields: {
            enterpr:{
                validators: {
                    notEmpty: {
                        message: 'Nome is required'
                    },
                }
            },
            first_name: {
                validators: {
                    notEmpty: {
                        message: 'Nome is required'
                    },
                }
            },
            last_name: {
                validators: {
                    notEmpty: {
                        message: 'Cognome is required'
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
            phone: {
                validators: {
                    notEmpty: {
                        message: 'Telefono is required'
                    },
                }
            },
            via_numero: {
                validators: {
                    notEmpty: {
                        message: 'Via e numero is required'
                    },
                }
            },
            city: {
                validators: {
                    notEmpty: {
                        message: 'Città is required'
                    },
                }
            },
            cap: {
                validators: {
                    notEmpty: {
                        message: 'Cap is required'
                    },
                }
            },
            subject: {
                validators: {
                    notEmpty: {
                        message: 'Oggeto is required'
                    },
                }
            },
            message: {
                validators: {
                    notEmpty: {
                        message: 'Messagio is required'
                    },
                }
            },
        }
    })
}

/*
function validateCheckbox(){
    $(".danger-message-onlyoption").hide()
    $(".danger-message").hide()

    if ($("#partnercheckbox").is(":checked") == false &&
        $("#consumercheck").is(":checked") == false)
    {
        $(".danger-message").show()
        return false
    }

    else if ($("#partnercheckbox").is(":checked") == true &&
        $("#consumercheck").is(":checked") == true)
    {
        $(".danger-message-onlyoption").show()
        return false
    }

    $("#perfil .button-black").removeAttr("disabled")
    return true
}
*/

$("#perfil-partner").click(function (e) {
    var urlForm = $(this).data('url')

    if ($("#first_name").val() && $("#last_name").val() &&
        $("#email").val() && $("#phone").val() &&
        $("#via_numero").val() && $("#city").val() &&
        $("#cap").val() && $("#message").val() && $("#subject").val() && $("#social_reason").val()) {

        $.ajax({
            url: urlForm,
            type: "POST",
            dataType: "json",
            data: {
                first_name: $("#first_name").val(),
                last_name: $("#last_name").val(),
                social_reason: $("#social_reason").val(),
                email: $("#email").val(),
                phone: $("#phone").val(),
                via_numero: $("#via_numero").val(),
                city: $("#city").val(),
                cap: $("#cap").val(),
                message: $("#message").val(),
                subject: $("#subject").val(),
            },
            success: function () {
                $('form').trigger("reset");
                $('form').formValidation('destroy');
                validators()
                $("#myModal").modal()
            }
        })
    }
})


$("#create-profile-consumer").click(function (e) {

    var urlForm = $(this).data('url')

    if ($("#consumer_first_name").val() && $("#consumer_last_name").val() &&
        $("#consumer_email").val() && $("#consumer_phone").val() &&
        $("#consumer_via_numero").val() && $("#consumer_city").val() &&
        $("#consumer_cap").val() && $("#consumer_message").val() && $("#consumer_subject").val()) {



        $.ajax({
            url: urlForm,
            type: "POST",
            dataType: "json",
            data: {
                first_name: $("#consumer_first_name").val(),
                last_name: $("#consumer_last_name").val(),
                email: $("#consumer_email").val(),
                phone: $("#consumer_phone").val(),
                via_numero: $("#consumer_via_numero").val(),
                city: $("#consumer_city").val(),
                cap: $("#consumer_cap").val(),
                message: $("#consumer_message").val(),
                subject: $("#consumer_subject").val(),
            },
            success: function () {
                $('form').trigger("reset");
                $('form').formValidation('destroy');
                validators()
                $("#myModal").modal()

            }
        })
    }
})

/*
$("#partnercheckbox").change(function (){
    validateCheckbox()
})

$("#consumercheck").change(function (){
    validateCheckbox()
})
*/

$("form").submit(function (e){
    e.preventDefault()
})

validators()