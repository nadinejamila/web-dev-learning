$(document).ready(function() {

	$('#like').click(function() {
		var catid;
		catid = $(this).attr("data-catid");
		$.get('/rango/like-category', {category_id: catid}, function(data){
			$('#like_count').html(data);
			$('#like').hide();
		});
	});
	
	$('#suggestion').keyup(function(){
		var query;
		query = $(this).val();
		$.get('/rango/suggest-category/', {suggestion: query}, function(data){
			$('#cats').html(data);
		});
	});
});