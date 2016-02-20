$.ajax({
        url: "https://api.github.com/eliothmonroy/repos",
        data: {q: cadena_busqueda},
        success: function (data, textStatus, xhr) {

            $('.tv-show').remove();
            data.forEach(function (item) {
                var template_bind =
                    template.replace(":name:", item.show.name)
                        .replace(":summary:", item.show.summary)
                        .replace(":img:", item.show.image.medium)
                        .replace(":img_alt:", item.show.name + " Logo")
                        .replace(":id:", item.id)

                container.append($(template_bind).fadeIn(1500));
            })
        }
    }
)

