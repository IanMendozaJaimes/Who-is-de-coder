(function(){
    var id_reclutador;
    id_reclutador=$('.nickname_val').val();

	var obtener_resultados = function(){
		//GET ultimos hackatones
		var container = $(".resultados-busqueda");
        var template;
            template = "<div class='resultados'>"+
                +"<h3 class='nombre-proyecto'>:nombre-proyecto:</h3>"+
                "<ul class='resultado-data'>"+
                    "<li class='language'>:language:</li>"+
                    "<li class='fecha'>:fecha:</li>"+
                    "<li class='id'>:id:</li>"
                "</ul>"+
            "</div>";
		$.get("/find",function(data){
			data.forEach(function(item){
				var binding = template.replace(":nombre-proyecto:", item.nombre)
				.replace(":language:", item.language)
				.replace(":fecha:", item.fecha_format)
				.replace(":id:", item.id)
				container.append($(binding).fadeIn(1500));
			});
		});
	}
    obtener_resultados();

})();
