$(function(){
    $('.dropdown-menu .dropdown-item').click(function(){
        var visibleItem = $('.dropdown-toggle', $(this).closest('.dropdown'));
        visibleItem.text($(this).attr('value'));
    });
});

$(function(){
    var $setText = $('ul li .name_limit');
    var cutFigure = '13'; // 表示する文字数の設定
    var afterText = ' …'; // 省略した末尾に追加するテキスト

    $setText.each(function(){
        var textLength = $(this).text().length;
        var textTrim = $(this).text().substr(0,(cutFigure))

        if(cutFigure < textLength) {
            $(this).html(textTrim + afterText).css({visibility:'visible'});
        } else if(cutFigure >= textLength) {
            $(this).css({visibility:'visible'});
        }
    });
});