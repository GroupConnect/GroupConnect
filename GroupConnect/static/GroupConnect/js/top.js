$(function() {
    $("form").submit(function(){
        if ($("input[name='mail']").val() == '' && $("input[name='pass']").val() == '') {
            //メールとパスワードが入力されていない場合
            $('.mailblank').show();
            $('.passblank').show();
            $('.mailformatcheck').hide();
            $('.passformatcheck').hide();
            return false;
        } else if ($("input[name='mail']").val() == '') {
            //メールが入力されていない場合
            $('.mailblank').show();
            $('.passblank').hide();
            $('.mailformatcheck').hide();
            $('.passformatcheck').hide();
            return false; 
        } else if ($("input[name='pass']").val() == '') {
            //パスワードが入力されていない場合
            $('.mailblank').hide();
            $('.passblank').show();
            $('.mailformatcheck').hide();
            $('.passformatcheck').hide();
            return false; 
        } else if (!$("input[name='mail']").val().match(/^([a-zA-Z0-9])+([a-zA-Z0-9\._-])*@([a-zA-Z0-9_-])+([a-zA-Z0-9\._-]+)+$/) && !$("input[name='pass']").val().match(/^[0-9a-zA-Z]{8}$/)){
            //メールの形式とパスワードの文字数、形式が違う場合
            $('.mailblank').hide();
            $('.passblank').hide();
            $('.mailformatcheck').show();
            $('.passformatcheck').show();
            return false;
        } else if (!$("input[name='mail']").val().match(/^([a-zA-Z0-9])+([a-zA-Z0-9\._-])*@([a-zA-Z0-9_-])+([a-zA-Z0-9\._-]+)+$/)){
            //メールの形式が違う場合
            $('.mailblank').hide();
            $('.passblank').hide();
            $('.mailformatcheck').show();
            $('.passformatcheck').hide();
            return false;
        } else if (!$("input[name='pass']").val().match(/^[0-9a-zA-Z]{8}$/)) {
            //パスワードの文字数、形式が違う場合
            $('.mailblank').hide();
            $('.passblank').hide();
            $('.mailformatcheck').hide();
            $('.passformatcheck').show();
            return false;
        } else {
          $("form").submit();
        }
    });
}); 