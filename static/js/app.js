(function(){
	console.log("Listo");

	var obtener_hackatones = function(){
		//GET ultimos hackatones
		var container = $(".append-ajax-hacks");

		var template = "<div class='hack-intro list-group'><div class='list-group-item'>"+
		"<h3 class='hack-name list-group-item-heading'><a href='/hackatones/:id_hack:'>:name:</a></h3>"+
          "<ul class='hack-data'>"+
            "<div class='list-group-item-text'><li class='hack-place'>Lugar: :place:</li>"+
            "<li class='hack-date'>Fecha: :fecha:</li></div>"+
          "</ul>"+
        "</div></div>";


		$.get("/hackaton/preview",function(data){
			data.forEach(function(item){
				var binding = template.replace(":name:", item.nombreHackaton)
				.replace(":place:", item.lugar)
				.replace(":fecha:", item.fecha_format)
				.replace(":id_hack:", item.id)

				container.append($(binding).fadeIn(1500));
			});
		});
	}

	var obtener_user = function(){
		//GET info facebook + correo
		var container = $('.user-facebook');
		var template ="<img src=':direccion:'/>"*
              "<h4 class='user-name'>:user-name:</h4>"+
              "<p class='user-mail'>:user-mail:</p>";

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
	obtener_hackatones();
})();
