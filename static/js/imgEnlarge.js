// 依赖jq 默认点击<img>标签就会放大，可根据自己情况修改

$(document).ready(function () {
    $("body").append("<!--放大图片-->\n" +
        "<div class=\"blackScreen\" style=\"display: none;display:none;    position:fixed;    top:0;    right:0;    bottom:0;    left:0;    background-color:#000000;    z-index:1000;\">\n" +
        "    <span class=\"fullScreenImg\" style='position:absolute;    top:0;    right:0;    bottom:60px;    left:0;    background:center center no-repeat;    background-size:contain;'></span>\n" +
        "</div>");
});

$(function () {

// 放大图片
    $('img').on('click', function () {
        // console.log("放大");
        if (this.getAttribute("src") != "url(\"null\") 0% 0% / 100% no-repeat") {
            $(".fullScreenImg").css("background-image", "url(\"" + this.getAttribute("src") + "\")");
            $(".blackScreen").fadeIn(100);
        }
    });

// 关闭放大图片
    $(".blackScreen").on("click", function () {
        // console.log("关闭");
        $(".blackScreen").fadeOut(100);
    });

});