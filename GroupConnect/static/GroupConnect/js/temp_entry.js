$(function() {
    $("form").submit(function(){
        if ($("input[name='mail']").val() == '') {
            //メールが入力されていない場合
            $('.mailblank').show();
            return false; 
        } else {
          $("form").submit();
        }
    });
}); 