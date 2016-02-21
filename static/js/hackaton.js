(function(){
	function obtener_proyectos(){
		var container = $('.hackaton-proyectos');
		var template_proyectos = "<h3>:nombre:</h3><p>:descripcion:</p>"+
		"<p>Tecnologías</p><ul>"
		$.get('/hackaton/proyectos', function(data){
			data.forEach(item){
				var binding = template_proyectos.replace(":nombre:",item.nombre).replace(":descripcion:", item.descripcion);
				var i=0;
				var tecnologias = item.tecnologias;
				for(i; i<tecnologias.lenght;i++){
					template_proyectos += "<li><a href='"+tecnologias[i].id+"'>"+tecnologias[i].name+"</a></li>";
				}
				template_proyectos += "</ul><p>Integrantes</p><ul>"
				for(i=0;i<item.integrantes.lenght;i++){
					template_proyectos += "<li><a href='"+item.integrantes[i].nickname+"'>"+item.integrantes[i].name+"</a></li>";
				}
				template_proyectos += "</ul>"
				container.append($(binding).fadeIn(1500));
			}
		})
	}
	obtener_proyectos();
})();
