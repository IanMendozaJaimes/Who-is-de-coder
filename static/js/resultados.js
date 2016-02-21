(function(){
    var id_reclutador;
    id_reclutador=$('.nickname_val').val();
    var keyword=$('.keyword').val();
	var obtener_resultados = function(){
		//GET ultimos hackatones
		var container = $(".resultados-busqueda");
        var template;
            template = "<div class='resultados'>"+
                +"<h3 class='nombre-proyecto'>:nombre-proyecto:</h3>"+
                "<ul class='resultado-data'>"+
                    "<li class='nombre-equipo'>:nombre-equipo:</li>"+
                    "<li class='language'>:language:</li>"+
                    "<li class='id'>:id:</li>"
                "</ul>"+
            "</div>";
		$.get("/find/"+keyword,function(data){
			data.forEach(function(item){
				var binding = template.replace(":nombre-proyecto:", item.nombreProyecto)
                .replace(":nombre-equipo:", item.nombreEquipo)
				.replace(":language:", item.tecnologias)
				.replace(":id:", item.id)
				container.append($(binding).fadeIn(1500));
			});
		});
	}
    obtener_resultados();

})();
