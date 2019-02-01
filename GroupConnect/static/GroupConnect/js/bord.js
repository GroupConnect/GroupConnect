$(function(){
    $('.dropdown-menu .dropdown-item').click(function(){
        var visibleItem = $('.dropdown-toggle', $(this).closest('.dropdown'));
        visibleItem.text($(this).attr('value'));
    });
});

(function($){
    
    $('#category-btn').on('click', function(){

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

var countUpValue = 0;
$("#button").click(function countUp(){
    countUpValue++;
    $("#large-frame").prepend('<div id="post-outside0"><div class="post-outside" id="post-outside"><div class="post"><p class="Contributor">白方丈晴</p><p class="time" id="time"></p><p class="read">既読：<a data-toggle="modal" data-target="#basicModal2" href="#">0件</a></p><a class="post-delete" data-toggle="modal" data-target="#basicModal3" href="">投稿を削除</a><p class="letter-body" id="p"></p><a class="filename" href="#"></a></div><img src="{% static &ldquo;GroupConnect/img/返信アイコン.jpg&rdquo; %}" id="passcheck2" class="reply-icon"><a class="reply" id="reply" href="#">返信する</a></div></div>');
    /* // idがpの要素に入力したものを反映
    var newText = $("#UserInput").val();
    $("#p").text(newText);
    // 時間の取得
    var now = new Date();
    var y = now.getFullYear();
    var m = now.getMonth() + 1;
    var d = now.getDate();
    var mm = ('0' + m).slice(-2);
    var dd = ('0' + d).slice(-2);
    $('#time').text(y + '/' + mm + '/' + dd); */
});

$("#reply").on("click", function(){
	
    $("#post-outside0").append('<form action="bord" method="get" enctype="multipart/form-data"><div class="form-group d-inline"><textarea class="form-control" id="UserInput2" rows="6"></textarea><input type="file" name="s_file" accept="image/png, image/jpeg, image/gif" class="file-select"　multiple><input type="button" id="reply-button" class="btn btn-warning" value="返信"></div></form>');
    $("#reply-button").on("click", function(){
        $("#post-outside").append('<div id="post-outside0"><div class="post-outside" id="post-outside"><div class="post"><p class="Contributor">白方丈晴</p><p class="time" id="time2"></p><p class="read">既読：<a data-toggle="modal" data-target="#basicModal2" href="#">0件</a></p><a class="post-delete" data-toggle="modal" data-target="#basicModal3" href="">投稿を削除</a><p class="letter-body" id="p2"></p><a class="filename" href="#"></a></div><img src="{% static \'GroupConnect/img/返信アイコン.jpg\' %}" id="passcheck2" class="reply-icon"><a class="reply" id="reply" href="#">返信する</a></div></div>');
        /* // idがpの要素に入力したものを反映
        var newText = $("#UserInput2").val();
        $("#p2").text(newText);
        // 時間の取得
        var now = new Date();
        var y = now.getFullYear();
        var m = now.getMonth() + 1;
        var d = now.getDate();
        var mm = ('0' + m).slice(-2);
        var dd = ('0' + d).slice(-2);
        $('#time2').text(y + '/' + mm + '/' + dd); */
    });
});

