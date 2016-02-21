(function(){
	var id = $('#id_proyecto').val()
	var github_repo;
	//GET Proyecto
	var container_proyecto = $('.project-info');
	var template_proyecto = "<div class='proyecto-div'><h2>:nombre:</h2><h3>¿Que hacemos?</h3><p>:desc:</p><p>Encuentra el proyecto: <a href=':github:'></a></p><a href=':link:'></a><p></p></div>";
	$.get("/hackaton/equipos/"+id,function(data){
		var bind_proyecto = template_proyecto.replace(':nombre:',data.nombreProyecto).replace(':desc:', data.descripcionProyecto)
		.replace(':github:', data.githubProyecto).replace(':link:', data.linkProyecto);
		container_proyecto.append($(bind_proyecto).fadeIn(1000));
	});
	//GET Participants
	var container_participant = $('.project-participants');
	var template_participant = "<div class='participants-div'><h3>Our Team</h3><ul>";
	$.ajax({
		url:"/hackaton/equipos/"+id,
		success:function(data,txtStatus,xhr){
			data = [data]
			data.forEach(function(item_participant){
				template_participant += "<li>lechugaverde</li>"
				template_participant += "<li>agua de mar</li>"
			})
			template_participant += "</ul></div>"
			container_participant.append(template_participant);
		}
	})
	//GET tECNOLOGIES
	$.ajax({url:'/hackaton/equipos/'+item_project.id,
		success: function(data_tecno){
				data_tecno.forEach(function(tecno){
				bind_projecto += "<li>"+tecno.nombre+"</li>"
			});
				bind_projecto += "</ul></div>"
				container_projects.append($(bind_projecto).fadeIn(1200));
			}
		});
	//GET Commits
	var container = $('.project-commits');
	//¿Y si no tengo Github?
	var github2 = $('#git').val();
	if(github2===0){
		container.append('<h2>Aun no se vincula una cuenta</h2>');
	}else{
		/*$.get("http://api.github.com/repos/"+Owner+"/"+Repository+"/commits",function(data){
			var template = "<div class='github-div'><h4>Commit :message:</h4><p>:date:</p></div>";
			data.forEach(function(item){
				var bind = template.replace(":message:",item.commit.message).replace(":date:",item.commit.commiter.date);
				container.append($(bind).fadeIn(1500);
			})
		})*/
	}


})();
