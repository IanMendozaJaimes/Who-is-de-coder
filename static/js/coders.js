(function(){
    var user;
    var nickname;
    //GET ultimos hackatones
	var obtener_hackatones = function(){
		var container = $(".append-ajax-hacks");

		var template = "<div class='hack-intro'>"+
		"<h3 class='hack-name'><a href='/hackaton/:id_hack:'>:name:</a></h3>"+
          "<ul class='hack-data'>"+
            "<li class='hack-place'>:place:</li>"+
            "<li class='hack-date'>:fecha:</li>"+
          "</ul>"+
        "</div>";

		$.get("/hackaton/preview",function(data){
			data.forEach(function(item){
				if(item.paso!=1){
				var binding = template.replace(":name:", item.nombreHackaton)
				.replace(":place:", item.lugar)
				.replace(":fecha:", item.fecha)
				.replace(":id_hack:", item.id)
				}
				container.append($(binding).fadeIn(1500));
			});
		});
	}

    //GET API Github
    var obtener_repos=function()
    {
         var container = $(".container-apis");
        //Obtener repos de github
        var template = "<div class='github-repos'>" +
            "<h3 class='repo-name'>:name:</h3>" +
            "<ul class='repo-data'>" +
            "<li class='repo-description'>:description:</li>" +
            "<li class='repo-language'>:language:</li>" +
            "<li class='repo-watchers'>:watchers:</li>" +
            "<li class='repo-updated'>:updated:</li>" +
            "</ul>" +
            "<a href=':id_repo:' class='repo-link' id=':id_repo:'>:name:</a>" +
            "</div>";

        $.get({'https://api.github.com/users/'+user+'/repos', function (data) {
                    data.forEach(function (item) {
                        var template_bind =
                            template.replace(":name:", item.name)
                                .replace(":description:", item.description)
                                .replace(":language:", item.language)
                                .replace(":updated:", item.updated_at)
                                .replace(":watchers:", item.watchers)
                                .replace(":id_repo:", item.html_url)

                        container.append($(template_bind).fadeIn(1500));
                    });
                }
            }
        );
    }
    //Funcion para validar el ingreso como usuario
    function registro_datos(){
        var queEs = $('.que_es').val();
        if(queEs==1){
            $('.container-apis').hide();
            $('.yo_soy').text('Programador');
        }else if(queEs==3){
            $('.yo_soy').text('Reclutador');
        }else if(queEs==2)
         $('.yo_soy').text('Organizador');
    }

    //Funcion para ocultar el formulario
    function data_form(){
        var num_veces = $('.es_coder').val();
        if(num_veces == 1){
            $('.register').hide();
            user = $('#Nickname');
            if(user!=null){
                var repos = obtener_repos();
                var container_participacion = $('.hacks-participacion');
                var template_participacion = "<div><h3>:name:</h3><p>:date:</p><p>:place:</p><p>:place: ... </p></div>"
                nickname = $('nickname_val');
                $.get('/hackaton/preview/'+nickname, function(data){
                    if(data.lenght!=0){
                        data.forEach(function(item){var bind = template_participacion.replace(":name:",item.name).replace(":date:", item.date)
                        .replace(":place:", item.place).replace(":desc:",item.place);
                        container_participacion.append($(bind).fadeIn(1500));})

                    }else{
                        container_participacion.append("<h4 class='noob'>No tienes particpaciones!</h4>")
                    }
                })
            }else{
                    alert("Error");
                }
        }else{
            $('.info-users').hide();

        }
    }

    var data = data_form();
    var registro = registro_datos();
    var hackatones = obtener_hackatones();

})();
