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

	$('.rango-add').click(function() {
		var catid = $(this).attr('data-catid');
		var title = $(this).attr('data-title');
		var url = $(this).attr('data-url');
		var me = $(this);
		$.get('/rango/auto-add-page/', {category_id: catid, title: title, url: url}, function(data){
			$('#pages').html(data);
			me.hide();
		});
	});

});