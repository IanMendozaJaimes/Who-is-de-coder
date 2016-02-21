(function(){
	function obtener_proyectos(){

		//Hackaton tencology
		var id = $('#id_hack').val();
		var container_hackaton = $('.hack-data');
		var template_hackatones = "<h3>Nombre: :nombre:</h3><p>descripcion: :descripcion:</p><p>Fecha: :fecha:</p><p>Lugar: :lugar:</p><ul>";
		$.get('/hackaton/'+id, function(data){
			var bind_hack;
			bind_hack=template_hackatones.replace(':nombre:',data.nombreHackaton).replace(':descripcion:', data.descripcion)
			.replace(':fecha:', data.fecha).replace(':lugar:', data.lugar);

			/*bind_hack+="<ul><p>Nuestros Patrocinadores</p>";
			$.get('/hackaton/'+id+'/sponsores',function(data_sponsores){
				data.forEach(function(item_sponsor){
					bind_hack += "<li>"+item_sponsor.sponsore+"</li><li><img src='"+item_sponsor.logo+"'</li>"+
					"<li><a href='"+item_sponsor.webSponsor+"'>"+item_sponsor.webSponsor+"</a</li>"
				});
			})
			bind_hack+="</ul>"*/
			console.log(bind_hack);
			container_hackaton.append(bind_hack);
		})

		//Hakcton project
		var container_projects = $('.hackaton-proyectos');
		var template_projects = "<div class='project-div'><h3><a href='/proyecto/:id:'>Equipo :equipo:</a></h3><h4>Proyecto :proyecto:</h4><p>Descripción: :desc:</p>";
		$.get('/hackaton/'+id'/equipo', function(data){
			var bind_projecto;
			data.forEach(function(item_project){
				bind_projecto= template_projects.replace(':id:', item_project.id).replace(':equipo:', item_project.nombreEquipo).replace(':proyecto:', item_project.proyectoEquipo)
				.replace(':desc:', item_project.descripcionProyecto);
				bind_projecto += "<ul><p>Tecnologias</p>";
				//Tecnologias
				$.get('', function(data_tecno){
					data_tecno.forEach(function(tecno){
						bind_projecto += "<li>"+tecno.nombre+"</li>"
					});
				})
				bind_projecto += "</ul></div>"
				container_projects.append($(bind_projecto).fadeIn(1200));
			})
		})
	}
	obtener_proyectos();
})();
