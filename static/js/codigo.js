$(document).ready(function(){

<<<<<<< HEAD
    /*$('#subir_img').attr('disabled',true);
    $('#upload_file').on('keyup',function(){
        if($(this).val().length !=0){
            $('#subir_img').attr('disabled', false);
        }else{
            $('#subir_img').attr('disabled', true);
        }
    });*/

=======
>>>>>>> b8d0367f1526d38c8b39339dd003955deb5b863d
    $('#search').attr('disabled', true);
    $('#input_search').on('keyup',function(){
        if($(this).val().length !=0){
            $('#search').attr('disabled', false);
        }else{
            $('#search').attr('disabled', true);
        }
    });

    $('#register_button').on('click', function(e){
        e.preventDefault();
        datos = $('#register_form').serialize();
        var csrftoken = $("[name=csrfmiddlewaretoken]").val();
        $.ajax({
            url: '/usuario/registrar/',
            type: 'POST',
            headers: {
                "X-CSRFToken": csrftoken
            },
            data: datos,
            dataType: 'json',
            success: function(respuesta){
                if(respuesta.error){
                    $('.errores').css({display: 'block'});
                    $('.errores').html(respuesta.msj);
                }
                else if(respuesta.success){
                    $(location).attr('href', '/usuario/index');
                }
            },
            error: function(e){
                console.log(e);
            }
        });
    });

    $('#login_button').on('click', function(e){
        e.preventDefault();
        datos = $('#login_form').serialize();
        var csrftoken = $("[name=csrfmiddlewaretoken]").val();
        $.ajax({
            type: 'POST',
            url: '/usuario/loguearse/',
            data: datos,
            dataType: 'json',
            headers: {
                "X-CSRFToken": csrftoken
            },
            success: function(respuesta){
                if(respuesta.error){
                    $('.errores2').css({display: 'block'});
                    $('.errores2').html(respuesta.msj);
                }
                else if(respuesta.success){
                    $(location).attr('href', '/usuario/index');
                }
            },
            error: function(e){
                console.log(e);
            }
        });
    });

    $('#register_manager').on('click', function(e){
        e.preventDefault();
        datos = $('#register_form_manager').serialize();
        var csrftoken = $("[name=csrfmiddlewaretoken]").val();
        $.ajax({
            url: '/usuario/registrarmanager/',
            type: 'POST',
            headers: {
                "X-CSRFToken": csrftoken
            },
            data: datos,
            dataType: 'json',
            success: function(respuesta){
                if(respuesta.error){
                    $('.errores4').css({display: 'block'});
                    $('.errores4').html(respuesta.msj);
                }
                else if(respuesta.success){
                    var dir = $('#manager_index3').attr('href');
                    $(location).attr('href', dir);
                }
            },
            error: function(e){
                console.log(e);
            }
        });
    });
    $('#iniciar').on('click', function(){
        $('#modal_manager').modal("hide");
    });

    $('#login_button_manager').on('click', function(e){
        e.preventDefault();
        datos = $('#login_form_manager').serialize();
        var csrftoken = $("[name=csrfmiddlewaretoken]").val();
        $.ajax({
            type: 'POST',
            url: 'usuario/loguearmanager/',
            data: datos,
            dataType: 'json',
            headers: {
                "X-CSRFToken": csrftoken
            },
            success: function(respuesta){
                if(respuesta.error){
                    $('.errores3').css({display: 'block'});
                    $('.errores3').html(respuesta.msj);
                }
                else if(respuesta.success){
                    var dir = $('#manager_index2').attr('href');
                    $(location).attr('href', dir);
                }
            },
            error: function(e){
                console.log(e);
            }
        });
    });

    $('#register_resto_button').on('click', function(e){
        e.preventDefault();
        var form = $('#registrar_restaurante').get(0);
        var formData = new FormData(form);
        var csrftoken = $("[name=csrfmiddlewaretoken]").val();
        var url1 = $('#url').attr('href');
        $.ajax({
            url: url1,
            type: 'POST',
            headers: {
                "X-CSRFToken": csrftoken
            },
            data: formData,
            dataType: 'json',
            success: function(respuesta){
                if(respuesta.error){
                    $('.errores5').css({display: 'block'});
                    $('.errores5').html(respuesta.msj);
                }
                else if(respuesta.success){
                    location.reload(true);
                }
            },
            error: function(e){
                console.log(e);
            },
            cache: false,
            contentType: false,
            processData: false
        });
    });

    $('#guardar_comida').on('click', function(e){
        e.preventDefault();
        var csrftoken = $("[name=csrfmiddlewaretoken]").val();
        var form = $('#comida').get(0);
        var formData = new FormData(form);
        $.ajax({
            url: '/subircomida/',
            type: 'POST',
            headers: {
                "X-CSRFToken": csrftoken
            },
            data: formData,
            dataType: 'json',
            success: function(respuesta){
                if(respuesta.error){
                    $('.errores8').css({display: 'block'});
                    $('.errores8').html(respuesta.msj);
                }
                else if(respuesta.success){
                    location.reload(true);
                }
            },
            error: function(e){
                console.log(e);
            },
            cache: false,
            contentType: false,
            processData: false
        });
    });
    $('#eliminar_comida_si').on('click', function(e){
        e.preventDefault();
        datos = $('#eliminar_comida').val()
        var csrftoken = $("[name=csrfmiddlewaretoken]").val();
        $.ajax({
            url: '/' + datos + '/eliminar/',
            type: 'POST',
            headers: {
                "X-CSRFToken": csrftoken
            },
            data: datos,
            dataType: 'json',
            success: function(respuesta){
                if(respuesta.success){
                    location.reload(true);
                }
            },
            error: function(e){
                console.log(e);
            }
        });
    });
    $('#subir_comentario').on('click', function(e){
        e.preventDefault();
        var radioValue = $("input[name='rating']:checked").val();
        if(radioValue){
            $('#radio_value').val(radioValue);
        }
        datos = $('#comentar').serialize();
        var csrftoken = $("[name=csrfmiddlewaretoken]").val();
        var id = $('#subir_comentario').val();
        $.ajax({
            type: 'POST',
            url: '/' + id + '/comentar/',
            data: datos,
            dataType: 'json',
            headers: {
                "X-CSRFToken": csrftoken
            },
            success: function(respuesta){
                if(respuesta.error){
                    $('.errores10').css({display: 'block'});
                    $('.errores10').html(respuesta.msj);
                }
                else if(respuesta.success){
                    $('#comentar_form').css({display: 'none'});
                    $('.comentario_user').html(respuesta.objeto[0]["user"]);
                    $('.comentario_user_texto').html(respuesta.objeto[0]["texto"]);
                    $('.comentario_user_fecha').html(respuesta.objeto[0]["fecha"]);
                }
            },
            error: function(e){
                console.log(e);
            }
        });
    });
    $('#subir_comentario_plato').on('click', function(e){
        e.preventDefault();
        var radioValue = $("input[name='rating2']:checked").val();
        if(radioValue){
            $('#radio_value2').val(radioValue);
        }
        datos = $('.comentar_plato').serialize();
        var csrftoken = $("[name=csrfmiddlewaretoken]").val();
        var id = $('#subir_comentario_plato').val();
        $.ajax({
            type: 'POST',
            url: '/' + id + '/comentar_plato/',
            data: datos,
            dataType: 'json',
            headers: {
                "X-CSRFToken": csrftoken
            },
            success: function(respuesta){
                if(respuesta.error){
                    $('.error').css({display: 'block'});
                    $('.error').html(respuesta.msj);
                }
                else if(respuesta.success){
                    $('.comentar_plato')[0].reset();
                    $('.comentario_propio').css({display: 'block'});
                    $('.comentario_user_2').html(respuesta.objeto[0]["user"]);
                    $('.comentario_user_texto_2').html(respuesta.objeto[0]["texto"]);
                    $('.comentario_user_fecha_2').html(respuesta.objeto[0]["fecha"]);
                }
            },
            error: function(e){
                console.log(e);
            }
        });
    });
    var modalDiv = $(".modal-div");
    $(".open-modal").on("click", function(){
        $.ajax({
          url: $(this).attr("data-url"),
          success: function(data) {
            modalDiv.html(data);
            $("#modaleditarcomida").modal();
          }
        });
    });
<<<<<<< HEAD
=======
    
>>>>>>> b8d0367f1526d38c8b39339dd003955deb5b863d
    $('#subir_img').on('click', function(e){
        e.preventDefault();
        var form = $('#subir_img_form').get(0);
        var formData = new FormData(form);
        var csrftoken = $("[name=csrfmiddlewaretoken]").val();
        $.ajax({
            url: '/subirimg/',
            type: 'POST',
            headers: {
                "X-CSRFToken": csrftoken
            },
            data: formData,
            dataType: 'json',
            success: function(respuesta){
                if(respuesta.error){
                    $('.errores').css({display: 'block'});
                    $('.errores').html(respuesta.msj);
                }
                else if(respuesta.success){
                    location.reload(true);
                }
            },
            error: function(e){
                console.log(e);
            },
            cache: false,
            contentType: false,
            processData: false
        });
    });
    
});