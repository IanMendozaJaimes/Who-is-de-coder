(function(){
	console.log("Listo");



    var obtener_repos=function()
    {
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
            "<span class='repo-link' id=':id_repo:'>+ :name:</span>" +
            "</div>";
    var user="eliothmonroy";
        $.get({
                url: "https://api.github.com/eliothmonroy/repos",
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
    obtener_repos();
})();