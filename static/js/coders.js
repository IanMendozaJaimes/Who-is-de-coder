(function(){

    var obtener_repos=function()
    {

	var obtener_hackatones = function(){
		//GET ultimos hackatones
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
				if(item.){

				}
				var binding = template.replace(":name:", item.nombreHackaton)
				.replace(":place:", item.lugar)
				.replace(":fecha:", item.fecha)
				.replace(":id_hack:", item.id)

				container.append($(binding).fadeIn(1500));
			});
		});
	}


         var container = $(".container-github");
        //Obtener repos de github
        var template = "<div class='github-repos'>" +
            "<h3 class='repo-name'>:name:</h3>" +
            "<ul class='repo-data'>" +
            "<li class='repo-description'>:description:</li>" +
            "<li class='repo-language'>:language:</li>" +
            "<li class='repo-watchers'>:watchers:</li>" +
            "<li class='repo-updated'>:updated:</li>" +
            "</ul>" +
            "<span class='repo-link' id=':id_repo:'></span>" +
            "</div>";
    var user="eliothmonroy";
        $.get({
                url: "https://api.github.com/users/eliothmonroy/repos",
                success: function (data) {
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
    obtener_hackatones();
    obtener_repos();

})();