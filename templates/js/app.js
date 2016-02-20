(function(){
	console.log("Listo");

	var obtener_hackatones = function(){
		//GET ultimos hackatones
		var container = $(".append-ajax-hacks");

		var template = "<div class='hack-intro'>"+
		"<h3 class='hack-name'>:name:</h3>"+
          "<ul class='hack-data'>"+
            "<li class='hack-place'>:place:</li>"+
            "<li class='hack-date'>:fecha:</li>"+
            "<li class='hack-desc'>:desc:</li>"+
          "</ul>"+
          "<span class='hack-link' id=':id_hack:'>+ :name:</span>"+
        "</div>";

		var hackatones_vista=10;
		$.get("/api/hackatones",function(data){
			data.forEach(function(item){
				var binding = template.replace(":name:", item.name)
				.replace(":place:", item.place)
				.replace(":fecha:", item.date)
				.replace(":desc:", item.desc)
				.replace(":id_hack:", item.id)

				container.append($(binding).fadeIn(1500));
			});
		});
	}

	var obtener_user = function(){
		//GET info facebook + correo
		var container = $('.user-facebook');
		var template ="<img src=':direccion:'/>"*
              "<h4 class=':user-name:'>Nombre</h4>"+
              "<p class=':user-mail:'></p>";

		$.get("/api/user", function(data){
			data.forEach(function(item){
				var binding = template.replace(":name:", item.name)
				.replace(":direccion:", item.place)
				.replace(":user-name:", item.date)
				.replace(":user-mail:", item.desc)
				container.append($(binding).fadeIn(1500));
			})
		})
	}

})();