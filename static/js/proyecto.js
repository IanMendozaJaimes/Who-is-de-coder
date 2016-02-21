(function(){
	//Get Commits
	$.get("http://api.github.com/repos/"+Owner+"/"+Repository+"/commits",function(data){
		var container = $('.project-commits');
		var template = "<h4>Commit :message:</h4><p>:date:</p>";
		data.forEach(item){
			var bind = template.replace(":message:",item.commit.message).replace(":message:",item.commit.commiter.date);
			container.append($(bind).fadeIn(1500);
		}
	});

})();