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
                $('#post-form' + count).removeClass('reply-form');
            });
            $(document).on('click', '#reply-hide' + count, function() {
                $('#reply-show' + count).removeClass('reply-hide');
                $('#reply-hide' + count).addClass('reply-hide');
                $('#post-form' + count).addClass('reply-form');
            });
        })(cnt);
    };

    //ファイル選択
    $(document).on('change', '.custom-file-input', handleFileSelect);
    function handleFileSelect(evt) {
        $('#preview').remove();// 繰り返し実行時の処理
        $(this).next('.custom-file-label').html('ファイル選択...');
        $(this).parents('.input-group').after('<div id="preview"></div>');
        var files = evt.target.files;

        for (var i = 0, f; f = files[i]; i++) {

            var reader = new FileReader();

            reader.onload = (function(theFile) {
                return function(e) {
                    if (theFile.type.match('image.*')) {
                        var $html = ['<div class="d-inline-block mr-1 mt-1"><img class="img-thumbnail" src="', e.target.result,'" title="', escape(theFile.name), '" style="height:100px;" /><div class="small text-muted text-center">', escape(theFile.name),'</div></div>'].join('');// 画像では画像のプレビューとファイル名の表示
                    } else {
                        var $html = ['<div class="d-inline-block mr-1"><span class="small">', escape(theFile.name),'</span></div>'].join('');//画像以外はファイル名のみの表示
                    }

                    $('#preview').append($html);
                };
            })(f);

            reader.readAsDataURL(f);
        }

        $(this).next('.custom-file-label').html(files[0].name);
    }

    //ファイルの取消
    $('.reset').click(function(){
        $(this).parent().prev().children('.custom-file-label').html('ファイル選択...');
        $('.custom-file-input').val('');
        $('#preview').remove();
    })

    // $('.custom-file-input').on('change',function(){
    //     $(this).next('.custom-file-label').html($(this)[0].files[0].name);
    // })
    // //ファイルの取消
    // $('.reset').click(function(){
    //     $(this).parent().prev().children('.custom-file-label').html('ファイル選択...');
    //     $('.custom-file-input').val('');
    // })
});

(function($){
    
    $('#btn').on('click', function(){

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

(function($){
    
    $('#Categorydelete').on('click', function(){

        const content = $('#modal-delete-category');
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
        $('#category-close', content).on('click', () => {
            $('[id=category-delete]').hide();
            content.modal('hide');
        });

        // OK(削除ボタン)
        $('#category-delete-submit', content).on('click', () => {
            $('[id=category-delete]').show();
            content.modal('hide');
        });
    });
})(jQuery);

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
