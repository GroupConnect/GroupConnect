var countUpValue = 0;
$(function() {
    $('#passcheck').click(function countUp(){
        countUpValue++;
        if ( ( countUpValue % 2 ) != 0  ) {
            $('#currentpass').attr('type','text');
        } else {
            $('#currentpass').attr('type','password');
        }
    });
});

var countUpValue2 = 0;
$(function() {
    $('#passcheck2').click(function countUp(){
        countUpValue2++;
        if ( ( countUpValue2 % 2 ) != 0  ) {
            $('#pass').attr('type','text');
        } else {
            $('#pass').attr('type','password');
        }
    });
});

var countUpValue3 = 0;
$(function() {
    $('#passcheck3').click(function countUp(){
        countUpValue3++;
        if ( ( countUpValue3 % 2 ) != 0  ) {
            $('#passconf').attr('type','text');
        } else {
            $('#passconf').attr('type','password');
        }
    });
});

$(function() {
    $("form").submit(function(){
    if ($("input[name='old-password']").val() == '' && $("input[name='new-password1']").val() == '' && $("input[name='new-password2']").val() == '') {
        //現在のパスワード、新しいパスワード、新しいパスワード(確認用)が入力されていない場合
        $('.currentpassblank').show();
        $('.passblank').show();
        $('.passconfblank').show();
        $('.currentpassformatcheck').hide();
        $('.passformatcheck').hide();
        $('.passconfformatcheck').hide();
        $('.passconfdifferent').hide();
        return false;
    }else if ($("input[name='old-password']").val() == '' && $("input[name='new-password1']").val() == '') {
        //現在のパスワード、新しいパスワードが入力されていない場合
        $('.currentpassblank').show();
        $('.passblank').show();
        $('.passconfblank').hide();
        $('.currentpassformatcheck').hide();
        $('.passformatcheck').hide();
        $('.passconfformatcheck').hide();
        $('.passconfdifferent').hide();
        return false;
    }else if ($("input[name='old-password']").val() == '' && $("input[name='new-password2']").val() == '') {
        //現在のパスワード、新しいパスワード(確認用)が入力されていない場合
        $('.currentpassblank').show();
        $('.passblank').hide();
        $('.passconfblank').show();
        $('.currentpassformatcheck').hide();
        $('.passformatcheck').hide();
        $('.passconfformatcheck').hide();
        $('.passconfdifferent').hide();
        return false;
    }else if ($("input[name='new-password1']").val() == '' && $("input[name='new-password2']").val() == '') {
        //新しいパスワード、新しいパスワード(確認用)が入力されていない場合
        $('.currentpassblank').hide();
        $('.passblank').show();
        $('.passconfblank').show();
        $('.currentpassformatcheck').hide();
        $('.passformatcheck').hide();
        $('.passconfformatcheck').hide();
        $('.passconfdifferent').hide();
        return false;
    } else if ($("input[name='old-password']").val() == '') {
        //現在のパスワードが入力されていない場合
        $('.currentpassblank').show();
        $('.passblank').hide();
        $('.passconfblank').hide();
        $('.currentpassformatcheck').hide();
        $('.passformatcheck').hide();
        $('.passconfformatcheck').hide();
        $('.passconfdifferent').hide();
        return false;
    } else if ($("input[name='new-password1']").val() == '') {
        //新しいパスワードが入力されていない場合
        $('.currentpassblank').hide();
        $('.passblank').show();
        $('.passconfblank').hide();
        $('.currentpassformatcheck').hide();
        $('.passformatcheck').hide();
        $('.passconfformatcheck').hide();
        $('.passconfdifferent').hide();
        return false;
    } else if ($("input[name='new-password2']").val() == '') {
        //新しいパスワード(確認用)が入力されていない場合
        $('.currentpassblank').hide();
        $('.passblank').hide();
        $('.passconfblank').show();
        $('.currentpassformatcheck').hide();
        $('.passformatcheck').hide();
        $('.passconfformatcheck').hide();
        $('.passconfdifferent').hide();
        return false;
    } else if (!$("input[name='old-password']").val().match(/^[0-9a-zA-Z]{8,32}$/) && !$("input[name='new-password1']").val().match(/^[0-9a-zA-Z]{8,32}$/) && !$("input[name='new-password2']").val().match(/^[0-9a-zA-Z]{8,32}$/)) {
        //現在のパスワード、新しいパスワード、新しいパスワード(確認用)の文字数が違う場合
        $('.currentpassblank').hide();
        $('.passblank').hide();
        $('.passconfblank').hide();
        $('.currentpassformatcheck').show();
        $('.passformatcheck').show();
        $('.passconfformatcheck').show();
        $('.passconfdifferent').hide();
        return false;
    } else if (!$("input[name='old-password']").val().match(/^[0-9a-zA-Z]{8,32}$/) && !$("input[name='new-password1']").val().match(/^[0-9a-zA-Z]{8,32}$/)) {
        //現在のパスワードと新しいパスワードの文字数が違う場合
        $('.currentpassblank').show();
        $('.passblank').show();
        $('.passconfblank').hide();
        $('.currentpassformatcheck').hide();
        $('.passformatcheck').hide();
        $('.passconfformatcheck').hide();
        $('.passconfdifferent').hide();
        return false;
    } else if (!$("input[name='old-password']").val().match(/^[0-9a-zA-Z]{8,32}$/) && !$("input[name='new-password2']").val().match(/^[0-9a-zA-Z]{8,32}$/)) {
        //現在のパスワードと新しいパスワード(確認用)の文字数が違う場合
        $('.currentpassblank').hide();
        $('.passblank').hide();
        $('.passconfblank').hide();
        $('.currentpassformatcheck').show();
        $('.passformatcheck').hide();
        $('.passconfformatcheck').show();
        $('.passconfdifferent').hide();
        return false;
    } else if (!$("input[name='new-password1']").val().match(/^[0-9a-zA-Z]{8,32}$/) && !$("input[name='new-password2']").val().match(/^[0-9a-zA-Z]{8,32}$/)) {
        //パスワードとパスワード(確認用)の文字数が違う場合
        $('.currentpassblank').hide();
        $('.passblank').hide();
        $('.passconfblank').hide();
        $('.currentpassformatcheck').hide();
        $('.passformatcheck').show();
        $('.passconfformatcheck').show();
        $('.passconfdifferent').hide();
        return false;
    } else if (!$("input[name='old-password']").val().match(/^[0-9a-zA-Z]{8,32}$/)) {
        //パスワードの文字数が違う場合
        $('.currentpassblank').hide();
        $('.passblank').hide();
        $('.passconfblank').hide();
        $('.currentpassformatcheck').show();
        $('.passformatcheck').hide();
        $('.passconfformatcheck').hide();
        $('.passconfdifferent').hide();
        return false;
    } else if (!$("input[name='new-password1']").val().match(/^[0-9a-zA-Z]{8,32}$/)) {
        //パスワードの文字数が違う場合
        $('.currentpassblank').hide();
        $('.passblank').hide();
        $('.passconfblank').hide();
        $('.currentpassformatcheck').hide();
        $('.passformatcheck').show();
        $('.passconfformatcheck').hide();
        $('.passconfdifferent').hide();
        return false;
    } else if (!$("input[name='new-password2']").val().match(/^[0-9a-zA-Z]{8,32}$/)) {
        //パスワード(確認用)の文字数が違う場合
        $('.currentpassblank').hide();
        $('.passblank').hide();
        $('.passconfblank').hide();
        $('.currentpassformatcheck').hide();
        $('.passformatcheck').hide();
        $('.passconfformatcheck').show();
        $('.passconfdifferent').hide();
        return false;
    } else if ($("input[name='new-password1']").val() !== $("input[name='new-password2']").val()) {
        //パスワードとパスワード(確認用)が異なる場合
        $('.currentpassblank').hide();
        $('.passblank').hide();
        $('.passconfblank').hide();
        $('.currentpassformatcheck').hide();
        $('.passformatcheck').hide();
        $('.passconfformatcheck').hide();
        $('.passconfdifferent').show();
        return false;
    } else {
      $("form").submit();
    }
});
}); 