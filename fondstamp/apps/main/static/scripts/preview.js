/*
 * Image preview script 
 */

this.imagePreview = function() {
	$("a.preview").hover(function(e) {
		var img = new Image();
		img.id = "preview";
		img.onload = function() {
			var pos_x = ($(window).width() - $("#preview").outerWidth(true)) / 2;
			if (pos_x < 0) pos_x = 0;
//			var pos_y = this.src.indexOf("schema") == -1 ? ($(window).height() - $("#preview").outerHeight()) / 2 : parseInt($("body").css("padding-top").replace("px", ""));
			var pos_y = ($(window).height() - $("#preview").outerHeight(true)) / 2;
			if (pos_y < 0) pos_y = 0;
			$("#preview")
				.css("top", pos_y + "px")
				.css("left", pos_x + "px")
				.fadeIn("fast");
		}
		$("body").append(img);
		var margin = parseInt($("#preview").css("margin-top").replace("px", ""));
		var padding = parseInt($("#preview").css("padding-left").replace("px", ""));
		var border = parseInt($("#preview").css("border-left-width").replace("px", ""));
		var delta = margin*2 + padding*2 + border*2;
		$("#preview")
			.css("max-width", $(window).width() - delta + "px")
			.css("max-height", $(window).height() - delta + "px");
		img.src = this.href;
    },
	function() {
		$("#preview").remove();
    });
//	$("a.preview").mousemove(function(e){
//		$("#preview")
// 			.css("top",(e.pageY - xOffset) + "px")
// 			.css("left",(e.pageX + yOffset) + "px");
//	});
};

// starting the script on page load
$(document).ready(function() {
	imagePreview();
});