(function(){
	function obtener_proyectos(){
		var id = $('#id_hack');
		var container_hackaton = $('.hackaton-proyectos');
		var template_hackatones = "<h3>Nombre: :nombre:</h3><p>descripcion: :descripcion:</p><p>Fecha: :fecha:</p><p>Lugar: :lugar:</p><ul>";
		$.get('/hackaton/'+id, function(data){

			template_hackatones.replace(':nombre:',data.nombreHackaton).replace(':descripcion:', data.descripcion)
			.replace(':fecha:', data.fecha).replace(':lugar:', data.lugar);

			template_hackatones+="<ul><p>Nuestros Patrocinadores</p>";
			var i;
			for(i=0;i<data.sponsores.length;i++){
				template_hackatones+="<li>"+data.sponsores[i]+"</li>"
			}
			template_hackatones+="</ul>"

			container_hackaton.append(template_hackatones);
		})


		$.get('/hackaton/'+id, function(data){
				$.get(""+data.equipazo,function(data){
					
				})
			}
		})
	}
	obtener_proyectos();
})();
