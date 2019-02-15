$(function(){
    $('.dropdown-menu .dropdown-item').click(function(){
        var visibleItem = $('.dropdown-toggle', $(this).closest('.dropdown'));
        visibleItem.text($(this).attr('value'));
    });


    var post_length = $('#large-frame .post-frame').length;
    for (cnt = 0; cnt < post_length; cnt++) {
        (function(count) {
            $(document).on('click', '#reply-show' + count, function() {
                $('#reply-show' + count).addClass('reply-hide');
                $('#reply-hide' + count).removeClass('reply-hide');
                $('#post-form' + count).removeClass('post-form');
            });
            $(document).on('click', '#reply-hide' + count, function() {
                $('#reply-show' + count).removeClass('reply-hide');
                $('#reply-hide' + count).addClass('reply-hide');
                $('#post-form' + count).addClass('post-form');
            });
        })(cnt);
    };
});

(function($) {
    
    $('#category-btn').on('click', function() {

        const content = $('#modal');
        content
        // モーダル開始前の処理
        .on('show.bs.modal', () => {
            console.log('modal open start');
        })
        // モーダル開始後の処理
        .on('shown.bs.modal', () => {
            console.log('modal open complete');
        })
        // モーダル終了後の処理
        .on('hidden.bs.modal', () => {
            console.log('modal hidden complete');

        // 後片付け
            $('.form-control', content).val('');
        })
        .modal({
            backdrop: 'static',
            keyboard: true
        });

        // Close(手動)ボタン
        $('#close', content).on('click', () => {
            content.modal('hide');
        });
    });
})(jQuery);

$(function(){
    var $setText = $('.name_limit');
    var cutFigure = '5'; // 表示する文字数の設定
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




// $(function() {

//     var post_length = $('#large-frame .post-frame').length;
//     for (cnt = 0; cnt < post_length; cnt++) {
//         $(document).on('click', '#reply-show' + cnt, function() {
//             $('#post-form' + cnt).removeClass('post-form');
//             $('#reply-show' + cnt).addClass('reply-hide');
//             $('#reply-hide' + cnt).removeClass('reply-hide');
//         });
//         $(document).on('click', '#reply-hide' + cnt, function() {
//             $('#post-form' + cnt).addClass('post-form');
//             $('#reply-show' + cnt).removeClass('reply-hide');
//             $('#reply-hide' + cnt).addClass('reply-hide');
//         });
//     };

    
// });

// $("#button").on("click", function(){
//     $("#large-frame").prepend('<div class="post-frame"><div class="post-outside"><div class="post"><p class="Contributor">白方丈晴</p><p class="time"></p><p class="read">既読：<a data-toggle="modal" data-target="#basicModal2" href="#">0件</a></p><a class="post-delete" data-toggle="modal" data-target="#basicModal3" href="">投稿を削除</a><p class="letter-body"></p><a class="filename" href="#"></a></div><img src="{% static &ldquo;GroupConnect/img/返信アイコン.jpg&rdquo; %}" id="passcheck2" class="reply-icon"><a class="reply" href="#">返信する</a></div><form action="bord" class="post-form" method="get" enctype="multipart/form-data"><div class="form-group d-inline"><textarea class="form-control" id="UserInput" rows="6"></textarea><input type="file" name="s_file" accept="image/png, image/jpeg, image/gif" class="file-select"　multiple><input type="button" class="btn btn-warning reply-button" value="返信"></div></form></div>');
//     $($('.post-frame').get().reverse()).each(function(i){
//         $(this).attr('id','post-frame' + (i+1));
//     });
//     $($('.post-outside').get().reverse()).each(function(i){
//         $(this).attr('id','post-outside' + (i+1));
//     });
//     $($('.reply').get().reverse()).each(function(i){
//         $(this).attr('id','reply' + (i+1));
//     });
//     $($('.letter-body').get().reverse()).each(function(i){
//         var a = $(this).attr('id','letter-body' + (i+1));
//     });
//     $($('.post-form').get().reverse()).each(function(i){
//         $(this).attr('id','post-form' + (i+1));
//     });
//     $($('.reply-button').get().reverse()).each(function(i){
//         $(this).attr('id','reply-button' + (i+1));
//     });

//     //id=reply1のボタンをクリックした場合
//     $("#reply1").on("click", function(){
//         $('#post-form1').show();
//         //id=post-form2があった場合
//         if($('#post-form2').length) {
//             $('#post-form2').hide(); 
//             $("#post-frame1").append('<form action="bord" id="replyarea-frame" method="get" enctype="multipart/form-data"><div class="form-group d-inline"><textarea class="form-control" id="UserInput" rows="6"></textarea><input type="file" name="s_file" accept="image/png, image/jpeg, image/gif" class="file-select"　multiple><input type="button" id="reply-button1" class="btn btn-warning" value="返信"></div></form>');
            
//             $("#reply-button1").on("click", function(){
//                 $("#post-frame1").append('<div class="post-outside"><div class="post"><p class="Contributor">白方丈晴</p><p class="time"></p><p class="read">既読：<a data-toggle="modal" data-target="#basicModal2" href="#">0件</a></p><a class="post-delete" data-toggle="modal" data-target="#basicModal3" href="">投稿を削除</a><p class="letter-body"></p><a class="filename" href="#"></a></div><img src="{% static \'GroupConnect/img/返信アイコン.jpg\' %}" id="passcheck2" class="reply-icon"><a class="reply" href="#">返信する</a></div><form action="bord" class="post-form" method="get" enctype="multipart/form-data"><div class="form-group d-inline"><textarea class="form-control" id="UserInput" rows="6"></textarea><input type="file" name="s_file" accept="image/png, image/jpeg, image/gif" class="file-select"　multiple><input type="button" class="btn btn-warning reply-button" value="返信"></div></form>');
//                 $('#post-form1').hide();
//                 $($('.post-outside').get().reverse()).each(function(i){
//                     $(this).attr('id','post-outside' + (i+1));
//                 });
//                 $($('.reply').get().reverse()).each(function(i){
//                     $(this).attr('id','reply' + (i+1));
//                 });
//                 $($('.letter-body').get().reverse()).each(function(i){
//                     $(this).attr('id','letter-body' + (i+1));
//                 });
//                 $($('.post-form').get().reverse()).each(function(i){
//                     $(this).attr('id','post-form' + (i+1));
//                 });
//                 $($('.reply-button').get().reverse()).each(function(i){
//                     $(this).attr('id','reply-button' + (i+1));
//                 });
//             });
//         } else {
//             $("#post-frame1").append('<form action="bord" id="replyarea-frame" method="get" enctype="multipart/form-data"><div class="form-group d-inline"><textarea class="form-control" id="UserInput" rows="6"></textarea><input type="file" name="s_file" accept="image/png, image/jpeg, image/gif" class="file-select"　multiple><input type="button" id="reply-button1" class="btn btn-warning" value="返信"></div></form>');
            
//             $("#reply-button1").on("click", function(){
//                 $("#post-frame1").append('<div class="post-outside"><div class="post"><p class="Contributor">白方丈晴</p><p class="time"></p><p class="read">既読：<a data-toggle="modal" data-target="#basicModal2" href="#">0件</a></p><a class="post-delete" data-toggle="modal" data-target="#basicModal3" href="">投稿を削除</a><p class="letter-body"></p><a class="filename" href="#"></a></div><img src="{% static \'GroupConnect/img/返信アイコン.jpg\' %}" id="passcheck2" class="reply-icon"><a class="reply" href="#">返信する</a></div><form action="bord" class="post-form" method="get" enctype="multipart/form-data"><div class="form-group d-inline"><textarea class="form-control" id="UserInput" rows="6"></textarea><input type="file" name="s_file" accept="image/png, image/jpeg, image/gif" class="file-select"　multiple><input type="button" class="btn btn-warning reply-button" value="返信"></div></form>');
//                 $('#post-form1').hide();
//                 $($('.post-outside').get().reverse()).each(function(i){
//                     $(this).attr('id','post-outside' + (i+1));
//                 });
//                 $($('.reply').get().reverse()).each(function(i){
//                     $(this).attr('id','reply' + (i+1));
//                 });
//                 $($('.letter-body').get().reverse()).each(function(i){
//                     $(this).attr('id','letter-body' + (i+1));
//                 });
//                 $($('.post-form').get().reverse()).each(function(i){
//                     $(this).attr('id','post-form' + (i+1));
//                 });
//                 $($('.reply-button').get().reverse()).each(function(i){
//                     $(this).attr('id','reply-button' + (i+1));
//                 });
//             });
//         };
//     }); 
//     //id=reply2のボタンをクリックした場合
//     $("#reply2").on("click", function(){
//         $('#post-form2').show();
//         if($('#post-form1').length) {
//             $('#post-form1').hide(); 
//             $("#post-frame2").append('<form action="bord" id="replyarea-frame" method="get" enctype="multipart/form-data"><div class="form-group d-inline"><textarea class="form-control" id="UserInput" rows="6"></textarea><input type="file" name="s_file" accept="image/png, image/jpeg, image/gif" class="file-select"　multiple><input type="button" id="reply-button1" class="btn btn-warning" value="返信"></div></form>');
            
//             $("#reply-button2").on("click", function(){
//                 $("#post-frame2").append('<div class="post-outside"><div class="post"><p class="Contributor">白方丈晴</p><p class="time"></p><p class="read">既読：<a data-toggle="modal" data-target="#basicModal2" href="#">0件</a></p><a class="post-delete" data-toggle="modal" data-target="#basicModal3" href="">投稿を削除</a><p class="letter-body"></p><a class="filename" href="#"></a></div><img src="{% static \'GroupConnect/img/返信アイコン.jpg\' %}" id="passcheck2" class="reply-icon"><a class="reply" href="#">返信する</a></div><form action="bord" class="post-form" method="get" enctype="multipart/form-data"><div class="form-group d-inline"><textarea class="form-control" id="UserInput" rows="6"></textarea><input type="file" name="s_file" accept="image/png, image/jpeg, image/gif" class="file-select"　multiple><input type="button" class="btn btn-warning reply-button" value="返信"></div></form>');
//                 $('#post-form2').hide();
//                 $($('.post-outside').get().reverse()).each(function(i){
//                     $(this).attr('id','post-outside' + (i+1));
//                 });
//                 $($('.reply').get().reverse()).each(function(i){
//                     $(this).attr('id','reply' + (i+1));
//                 });
//                 $($('.letter-body').get().reverse()).each(function(i){
//                     $(this).attr('id','letter-body' + (i+1));
//                 });
//                 $($('.post-form').get().reverse()).each(function(i){
//                     $(this).attr('id','post-form' + (i+1));
//                 });
//                 $($('.reply-button').get().reverse()).each(function(i){
//                     $(this).attr('id','reply-button' + (i+1));
//                 });
//             });
//         } else {
//             $("#post-frame2").append('<form action="bord" id="replyarea-frame" method="get" enctype="multipart/form-data"><div class="form-group d-inline"><textarea class="form-control" id="UserInput" rows="6"></textarea><input type="file" name="s_file" accept="image/png, image/jpeg, image/gif" class="file-select"　multiple><input type="button" id="reply-button1" class="btn btn-warning" value="返信"></div></form>');
            
//             $("#reply-button2").on("click", function(){
//                 $("#post-frame2").append('<div class="post-outside"><div class="post"><p class="Contributor">白方丈晴</p><p class="time"></p><p class="read">既読：<a data-toggle="modal" data-target="#basicModal2" href="#">0件</a></p><a class="post-delete" data-toggle="modal" data-target="#basicModal3" href="">投稿を削除</a><p class="letter-body"></p><a class="filename" href="#"></a></div><img src="{% static \'GroupConnect/img/返信アイコン.jpg\' %}" id="passcheck2" class="reply-icon"><a class="reply" href="#">返信する</a></div><form action="bord" class="post-form" method="get" enctype="multipart/form-data"><div class="form-group d-inline"><textarea class="form-control" id="UserInput" rows="6"></textarea><input type="file" name="s_file" accept="image/png, image/jpeg, image/gif" class="file-select"　multiple><input type="button" class="btn btn-warning reply-button" value="返信"></div></form>');
//                 $('#post-form2').hide();
//                 $($('.post-outside').get().reverse()).each(function(i){
//                     $(this).attr('id','post-outside' + (i+1));
//                 });
//                 $($('.reply').get().reverse()).each(function(i){
//                     $(this).attr('id','reply' + (i+1));
//                 });
//                 $($('.letter-body').get().reverse()).each(function(i){
//                     $(this).attr('id','letter-body' + (i+1));
//                 });
//                 $($('.post-form').get().reverse()).each(function(i){
//                     $(this).attr('id','post-form' + (i+1));
//                 });
//                 $($('.reply-button').get().reverse()).each(function(i){
//                     $(this).attr('id','reply-button' + (i+1));
//                 });
//             });
//         };
//     });
// });

// $("#button").on("click", function(){
//     $("#large-frame").prepend('<div class="post-frame"><div class="post-outside"><div class="post"><p class="Contributor">白方丈晴</p><p class="time" id="time"></p><p class="read">既読：<a data-toggle="modal" data-target="#basicModal2" href="#">0件</a></p><a class="post-delete" data-toggle="modal" data-target="#basicModal3" href="">投稿を削除</a><p class="letter-body"></p><a class="filename" href="#"></a></div><img src="{% static &ldquo;GroupConnect/img/返信アイコン.jpg&rdquo; %}" id="passcheck2" class="reply-icon"><a class="reply" href="#">返信する</a></div></div>');
//     $($('.post-frame').get().reverse()).each(function(i){
//         $(this).attr('id','post-frame' + (i+1));
//     });
//     $($('.post-outside').get().reverse()).each(function(i){
//         $(this).attr('id','post-outside' + (i+1));
//     });
//     $($('.reply').get().reverse()).each(function(i){
//         $(this).attr('id','reply' + (i+1));
//     });
//     $($('.letter-body').get().reverse()).each(function(i){
//         var a = $(this).attr('id','text' + (i+1));
//     });

//     $("[id^=reply]").on("click", function(){
//         if($('[id=replyarea-frame]').length) {
//             $('[id=replyarea-frame]').hide();
//             $("#post-frame1").append('<form action="bord" id="replyarea-frame" method="get" enctype="multipart/form-data"><div class="form-group d-inline"><textarea class="form-control" id="UserInput" rows="6"></textarea><input type="file" name="s_file" accept="image/png, image/jpeg, image/gif" class="file-select"　multiple><input type="button" id="reply-button1" class="btn btn-warning" value="返信"></div></form>');
            
//             $("[id^=reply-button]").on("click", function(){
//                 $("#post-frame1").append('<div id="post-frame"><div class="post-outside" id="post-outside"><div class="post"><p class="Contributor">白方丈晴</p><p class="time" id="time2"></p><p class="read">既読：<a data-toggle="modal" data-target="#basicModal2" href="#">0件</a></p><a class="post-delete" data-toggle="modal" data-target="#basicModal3" href="">投稿を削除</a><p class="letter-body" id="p2"></p><a class="filename" href="#"></a></div><img src="{% static \'GroupConnect/img/返信アイコン.jpg\' %}" id="passcheck2" class="reply-icon"><a class="reply" id="reply" href="#">返信する</a></div></div>');
//                 $('[id=replyarea-frame]').hide();
//                 $($('.post-frame').get().reverse()).each(function(i){
//                     $(this).attr('id','post-frame' + (i+1));
//                 });
//                 $($('.post-outside').get().reverse()).each(function(i){
//                     $(this).attr('id','post-outside' + (i+1));
//                 });
//                 $($('.reply').get().reverse()).each(function(i){
//                     $(this).attr('id','reply' + (i+1));
//                 });
//                 $($('.letter-body').get().reverse()).each(function(i){
//                     var b = $(this).attr('id','text' + (i+1));
//                 });
//             });
//         } else {
//             $("#post-frame1").append('<form action="bord" id="replyarea-frame" method="get" enctype="multipart/form-data"><div class="form-group d-inline"><textarea class="form-control" id="UserInput" rows="6"></textarea><input type="file" name="s_file" accept="image/png, image/jpeg, image/gif" class="file-select"　multiple><input type="button" id="reply-button1" class="btn btn-warning" value="返信"></div></form>');
            
//             $("[id^=reply-button]").on("click", function(){
//                 $($('.post-frame').get().reverse()).each(function(i){
//                     $(this).attr('id','post-frame' + (i+1));
//                 });
//                 $("#post-frame1").append('<div id="post-frame"><div class="post-outside" id="post-outside"><div class="post"><p class="Contributor">白方丈晴</p><p class="time" id="time2"></p><p class="read">既読：<a data-toggle="modal" data-target="#basicModal2" href="#">0件</a></p><a class="post-delete" data-toggle="modal" data-target="#basicModal3" href="">投稿を削除</a><p class="letter-body" id="p2"></p><a class="filename" href="#"></a></div><img src="{% static \'GroupConnect/img/返信アイコン.jpg\' %}" id="passcheck2" class="reply-icon"><a class="reply" id="reply" href="#">返信する</a></div></div>');
//                 $('[id=replyarea-frame]').hide();
//                 $($('.post-frame').get().reverse()).each(function(i){
//                     $(this).attr('id','post-frame' + (i+1));
//                 });
//                 $($('.post-outside').get().reverse()).each(function(i){
//                     $(this).attr('id','post-outside' + (i+1));
//                 });
//                 $($('.reply').get().reverse()).each(function(i){
//                     $(this).attr('id','reply' + (i+1));
//                 });
//                 $($('.letter-body').get().reverse()).each(function(i){
//                     var b = $(this).attr('id','text' + (i+1));
//                 });
//             });
//         };
//     });
// });