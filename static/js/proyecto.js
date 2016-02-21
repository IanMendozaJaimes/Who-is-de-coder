(function(){
	var id = $('#id_proyecto').val();
	var github_repo;
	//GET Proyecto
	var container_proyecto = $('project-info');
	var template_proyecto = "<div class='proyecto-div'><h2>:nombre:</h2><h3>¿Que hacemos?</h3><p>:desc:</p><p>Encuentra el proyecto: <a href=':github:'></a></p>";
	$.get("/proyecto/"+id,function(data){

	});

      <p id="github">{{github}}</p>
      <p id="url">{{url}}</p>
	//GET Commits
	$.get("http://api.github.com/repos/"+Owner+"/"+Repository+"/commits",function(data){
		var container = $('.project-commits');
		var template = "<div class='github-div'><h4>Commit :message:</h4><p>:date:</p></div>";
		data.forEach(item){
			var bind = template.replace(":message:",item.commit.message).replace(":message:",item.commit.commiter.date);
			container.append($(bind).fadeIn(1500);
		}
	});

})();