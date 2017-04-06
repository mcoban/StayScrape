window.onload = function() {


	// $('.lazyload').each(function() {
	// 	var img = $(this);
	// 	var src = img.attr('data-origin');
	// 	$(this).attr('src', src);
	// });

	// lazyload = function() {
	// 	var lazy_images = $('.lazyload');
	// 	$.each(lazy_images, function() {
	// 		var img = $(this);
	// 		var src = img.attr('data-origin');
	// 		$(this).attr('src', src);
	// 	});
	// }

	// lazyload();

};


$(window).bind("load", function() {

	setTimeout(function() {
		$('.lazyload').each(function() {
			var img = $(this);
			var src = img.attr('data-origin');
			$(this).attr('src', src);
		});
	}, 2000);

});