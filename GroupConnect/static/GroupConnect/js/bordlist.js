$(function(){
    $('.dropdown-menu .dropdown-item').click(function(){
        var visibleItem = $('.dropdown-toggle', $(this).closest('.dropdown'));
        visibleItem.text($(this).attr('value'));
    });
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
    
    $('#btn2').on('click', function(){

        const content = $('#modal2');
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
        $('#title-close', content).on('click', () => {
            content.modal('hide');
        });
    });
})(jQuery);


// 複数選択
var countUpValue = 0;
$(function () {
    $('#multi-btn').click(function countUp() {
        countUpValue++;
        if ( ( countUpValue % 2 ) != 0  ) {
            $('[id=checkbox]').show();
            $('[id=delete]').hide();
            $('#alldelete').show();
        } else {
            $('[id=checkbox]').hide();
            $('[id=delete]').show();
            $('#alldelete').hide();
        }
    });
});


//カテゴリー削除
function myEnter(){
    myRet = confirm("カテゴリを消す前に中に掲示板が残っているか確認してください。")
    if(myRet ==true){
        myconfirm = confirm("カテゴリを消すと中身も消えますがよろしいですか？")
        if(myconfirm == true){
            $('[id=category-delete]').show();
        }else{
            $('[id=category-delete]').hide();
        }
    }else{
        $('[id=category-delete]').hide();
    }
}

// var countcategory = 0;
// $(function () {
//     $('#Categorydelete').click(function() {
//         countcategory++;
//         if ((countcategory % 2) !=0) {
//             $('[id=category-delete]').show();
//         } else {
//             $('[id=category-delete]').hide();
//         }
//     });
// });



//カテゴリエラー
$(function() {
    $("#category-add").submit(function(){
        if ($("input[name='add']").val() == '' ) {
            //カテゴリ名が入力されていなかった場合
            $('.category-error').show();
            
            return false;
            
            
        } else {
          $("#category-add").submit();
        }
    });
}); 

//タイトルエラー
$(function() {
    $("#mainform").submit(function(){
        if ($("input[name='title']").val() == '' ) {
            //タイトル名が入力されていなかった場合
            $('.title-error').show();
            
            return false;
            
            
        } else {
          $("#mainform").submit();
        }
    });
}); 
//キャンセル押してエラーを隠す
(function($) {
    $('#close').on('click',function(){
        $('.category-error').hide();
        $('.title-error').hide();
    });
})(jQuery);


(function($) {
    $('#title-close').on('click',function(){
        $('.category-error').hide();
        $('.title-error').hide();
        
    });
})(jQuery);







    