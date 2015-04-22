$(document).ready(function() {
	$('#like').click(function() {
		var catid;
		catid = $(this).attr("data-catid");
		$.get('/rango/like-category', {category_id: catid}, function(data){
			$('#like_count').html(data);
			$('#like').hide();
		});
	});
});