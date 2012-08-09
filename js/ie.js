(function ($, undefined) {
    $(document).ready(function () {

	//gallery
	//mouseenter event on each thumb
    var zIndex = 99;
	function upImage(){
		var $content 	= $(this);
        $content.css('z-index', zIndex++);
		$content.animate({
			'margin-top' : -50}).find('img')
			.animate({'rotate': '0deg'},400);
	}

	//mouseleave event on each thumb
	function downImage(){
		var $content 	= $(this);
		var r 			= Math.floor(Math.random()*41)-20;
        $content.css('z-index', zIndex-1);
		$content.animate({
			'marginTop' : '0px'}).find('img')
			.animate({'rotate': r + 'deg'},400);
	}

    function showPic(src) {
        var box = $("<div class='floatbox' style='background: black'>&nbsp;</div>").click(function () {
            $(this).remove();
        });
        $(".floatbox").remove();
        box.css('opacity', 0);
        $("body").append(box);

        box.append("<i class='icon-remove-circle'></i>");
        box.append("<img src='" + src + "' class='float-img'>")
    }

	$("#gallery .pic").each(function () {
		$(this).mouseover(upImage);
		$(this).mouseout(downImage);
        $(this).click (function () {
            showPic($(this).find("a").attr("href"));
            return false;
        });
	});

    });
})(Zepto);
