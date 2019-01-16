var countUpValue = 0;
$(function() {
    $('#passcheck').click(function countUp(){
        countUpValue++;
        if ( ( countUpValue % 2 ) != 0  ) {
            $('#pass').attr('type','text');
            /* $('.pass-group img').attr('src',"{% static 'GroupConnect/img/目アイコン2.png' %}"); */
        } else {
            $('#pass').attr('type','password');
            /* $('.pass-group img').attr('src','/GroupConnect--/GroupConnect--/GroupConnect/static/GroupConnect/img/目アイコン2.png'); */
        }
    });
});

var countUpValue2 = 0;
$(function() {
    $('#passcheck2').click(function countUp(){
        countUpValue2++;
        if ( ( countUpValue2 % 2 ) != 0  ) {
            $('#passconf').attr('type','text');
        } else {
            $('#passconf').attr('type','password');
        }
    });
});

$(function() {
    $("form").submit(function(){
        if ($("input[name='name']").val() == '' && $("input[name='romaji']").val() == '' && $("input[name='mail']").val() == '' && $("input[name='pass']").val() == '' && $("input[name='passconf']").val() == '') {
            //名前、ローマ字、メール、パスワード、パスワード(確認用)が入力されていない場合
            $('.nameblank').show();
            $('.romajiblank').show();
            $('.mailblank').show();
            $('.passblank').show();
            $('.passconfblank').show();
            $('.passformatcheck').hide();
            $('.passconfformatcheck').hide();
            $('.passconfdifferent').hide();
            return false;
        } else if ($("input[name='name']").val() == '' && $("input[name='romaji']").val() == '' && $("input[name='mail']").val() == '' && $("input[name='pass']").val() == '') {
            //名前、ローマ字、メール、パスワードが入力されていない場合
            $('.nameblank').show();
            $('.romajiblank').show();
            $('.mailblank').show();
            $('.passblank').show();
            $('.passconfblank').hide();
            $('.passformatcheck').hide();
            $('.passconfformatcheck').hide();
            $('.passconfdifferent').hide();
            return false; 
        } else if ($("input[name='name']").val() == '' && $("input[name='romaji']").val() == '' && $("input[name='mail']").val() == '' && $("input[name='passconf']").val() == '') {
            //名前、ローマ字、メール、パスワード(確認用)が入力されていない場合
            $('.nameblank').show();
            $('.romajiblank').show();
            $('.mailblank').show();
            $('.passblank').hide();
            $('.passconfblank').show();
            $('.passformatcheck').hide();
            $('.passconfformatcheck').hide();
            $('.passconfdifferent').hide();
            return false; 
        } else if ($("input[name='name']").val() == '' && $("input[name='romaji']").val() == '' && $("input[name='pass']").val() == '' && $("input[name='passconf']").val() == '') {
            //名前、ローマ字、パスワード、パスワード(確認用)が入力されていない場合
            $('.nameblank').show();
            $('.romajiblank').show();
            $('.mailblank').hide();
            $('.passblank').show();
            $('.passconfblank').show();
            $('.passformatcheck').hide();
            $('.passconfformatcheck').hide();
            $('.passconfdifferent').hide();
            return false; 
        } else if ($("input[name='name']").val() == '' && $("input[name='mail']").val() == '' && $("input[name='pass']").val() == '' && $("input[name='passconf']").val() == '') {
            //名前、メール、パスワード、パスワード(確認用)が入力されていない場合
            $('.nameblank').show();
            $('.romajiblank').hide();
            $('.mailblank').show();
            $('.passblank').show();
            $('.passconfblank').show();
            $('.passformatcheck').hide();
            $('.passconfformatcheck').hide();
            $('.passconfdifferent').hide();
            return false; 
        } else if ($("input[name='romaji']").val() == '' && $("input[name='mail']").val() == '' && $("input[name='pass']").val() == '' && $("input[name='passconf']").val() == '') {
            //ローマ字、メール、パスワード、パスワード(確認用)が入力されていない場合
            $('.nameblank').hide();
            $('.romajiblank').show();
            $('.mailblank').show();
            $('.passblank').show();
            $('.passconfblank').show();
            $('.passformatcheck').hide();
            $('.passconfformatcheck').hide();
            $('.passconfdifferent').hide();
            return false; 
        } else if ($("input[name='name']").val() == '' && $("input[name='romaji']").val() == '' && $("input[name='mail']").val() == '') {
            //名前、ローマ字、メールが入力されていない場合
            $('.nameblank').show();
            $('.romajiblank').show();
            $('.mailblank').show();
            $('.passblank').hide();
            $('.passconfblank').hide();
            $('.passformatcheck').hide();
            $('.passconfformatcheck').hide();
            $('.passconfdifferent').hide();
            return false; 
        } else if ($("input[name='name']").val() == '' && $("input[name='romaji']").val() == '' && $("input[name='pass']").val() == '') {
            //名前、ローマ字、パスワードが入力されていない場合
            $('.nameblank').show();
            $('.romajiblank').show();
            $('.mailblank').hide();
            $('.passblank').show();
            $('.passconfblank').hide();
            $('.passformatcheck').hide();
            $('.passconfformatcheck').hide();
            $('.passconfdifferent').hide();
            return false; 
        } else if ($("input[name='name']").val() == '' && $("input[name='romaji']").val() == '' && $("input[name='passconf']").val() == '') {
            //名前、ローマ字、パスワード(確認用)が入力されていない場合
            $('.nameblank').show();
            $('.romajiblank').show();
            $('.mailblank').hide();
            $('.passblank').hide();
            $('.passconfblank').show();
            $('.passformatcheck').hide();
            $('.passconfformatcheck').hide();
            $('.passconfdifferent').hide();
            return false; 
        } else if ($("input[name='name']").val() == '' && $("input[name='mail']").val() == '' && $("input[name='pass']").val() == '') {
            //名前、メール、パスワードが入力されていない場合
            $('.nameblank').show();
            $('.romajiblank').hide();
            $('.mailblank').show();
            $('.passblank').show();
            $('.passconfblank').hide();
            $('.passformatcheck').hide();
            $('.passconfformatcheck').hide();
            $('.passconfdifferent').hide();
            return false; 
        } else if ($("input[name='name']").val() == '' && $("input[name='mail']").val() == '' && $("input[name='passconf']").val() == '') {
            //名前、メール、パスワード(確認用)が入力されていない場合
            $('.nameblank').show();
            $('.romajiblank').hide();
            $('.mailblank').show();
            $('.passblank').hide();
            $('.passconfblank').show();
            $('.passformatcheck').hide();
            $('.passconfformatcheck').hide();
            $('.passconfdifferent').hide();
            return false; 
        } else if ($("input[name='name']").val() == '' && $("input[name='pass']").val() == '' && $("input[name='passconf']").val() == '') {
            //名前、パスワード、パスワード(確認用)が入力されていない場合
            $('.nameblank').show();
            $('.romajiblank').hide();
            $('.mailblank').hide();
            $('.passblank').show();
            $('.passconfblank').show();
            $('.passformatcheck').hide();
            $('.passconfformatcheck').hide();
            $('.passconfdifferent').hide();
            return false; 
        } else if ($("input[name='romaji']").val() == '' && $("input[name='mail']").val() == '' && $("input[name='pass']").val() == '') {
            //ローマ字、メール、パスワードが入力されていない場合
            $('.nameblank').hide();
            $('.romajiblank').show();
            $('.mailblank').show();
            $('.passblank').show();
            $('.passconfblank').hide();
            $('.passformatcheck').hide();
            $('.passconfformatcheck').hide();
            $('.passconfdifferent').hide();
            return false; 
        } else if ($("input[name='romaji']").val() == '' && $("input[name='mail']").val() == '' && $("input[name='passconf']").val() == '') {
            //ローマ字、メール、パスワード(確認用)が入力されていない場合
            $('.nameblank').hide();
            $('.romajiblank').show();
            $('.mailblank').show();
            $('.passblank').hide();
            $('.passconfblank').show();
            $('.passformatcheck').hide();
            $('.passconfformatcheck').hide();
            $('.passconfdifferent').hide();
            return false; 
        } else if ($("input[name='romaji']").val() == '' && $("input[name='pass']").val() == '' && $("input[name='passconf']").val() == '') {
            //ローマ字、パスワード、パスワード(確認用)が入力されていない場合
            $('.nameblank').hide();
            $('.romajiblank').show();
            $('.mailblank').hide();
            $('.passblank').show();
            $('.passconfblank').show();
            $('.passformatcheck').hide();
            $('.passconfformatcheck').hide();
            $('.passconfdifferent').hide();
            return false; 
        } else if ($("input[name='mail']").val() == '' && $("input[name='pass']").val() == '' && $("input[name='passconf']").val() == '') {
            //メール、パスワード、パスワード(確認用)が入力されていない場合
            $('.nameblank').hide();
            $('.romajiblank').hide();
            $('.mailblank').show();
            $('.passblank').show();
            $('.passconfblank').show();
            $('.passformatcheck').hide();
            $('.passconfformatcheck').hide();
            $('.passconfdifferent').hide();
            return false; 
        } else if ($("input[name='name']").val() == '' && $("input[name='romaji']").val() == '') {
            //名前、ローマ字が入力されていない場合
            $('.nameblank').show();
            $('.romajiblank').show();
            $('.mailblank').hide();
            $('.passblank').hide();
            $('.passconfblank').hide();
            $('.passformatcheck').hide();
            $('.passconfformatcheck').hide();
            $('.passconfdifferent').hide();
            return false; 
        } else if ($("input[name='name']").val() == '' && $("input[name='mail']").val() == '') {
            //名前、メールが入力されていない場合
            $('.nameblank').show();
            $('.romajiblank').hide();
            $('.mailblank').show();
            $('.passblank').hide();
            $('.passconfblank').hide();
            $('.passformatcheck').hide();
            $('.passconfformatcheck').hide();
            $('.passconfdifferent').hide();
            return false; 
        } else if ($("input[name='name']").val() == '' && $("input[name='pass']").val() == '') {
            //名前、パスワードが入力されていない場合
            $('.nameblank').show();
            $('.romajiblank').hide();
            $('.mailblank').hide();
            $('.passblank').show();
            $('.passconfblank').hide();
            $('.passformatcheck').hide();
            $('.passconfformatcheck').hide();
            $('.passconfdifferent').hide();
            return false; 
        } else if ($("input[name='name']").val() == '' && $("input[name='passconf']").val() == '') {
            //名前、パスワード(確認用)が入力されていない場合
            $('.nameblank').show();
            $('.romajiblank').hide();
            $('.mailblank').hide();
            $('.passblank').hide();
            $('.passconfblank').show();
            $('.passformatcheck').hide();
            $('.passconfformatcheck').hide();
            $('.passconfdifferent').hide();
            return false; 
        } else if ($("input[name='romaji']").val() == '' && $("input[name='mail']").val() == '') {
            //ローマ字、メールが入力されていない場合
            $('.nameblank').hide();
            $('.romajiblank').show();
            $('.mailblank').show();
            $('.passblank').hide();
            $('.passconfblank').hide();
            $('.passformatcheck').hide();
            $('.passconfformatcheck').hide();
            $('.passconfdifferent').hide();
            return false; 
        } else if ($("input[name='romaji']").val() == '' && $("input[name='pass']").val() == '') {
            //ローマ字、パスワードが入力されていない場合
            $('.nameblank').hide();
            $('.romajiblank').show();
            $('.mailblank').hide();
            $('.passblank').show();
            $('.passconfblank').hide();
            $('.passformatcheck').hide();
            $('.passconfformatcheck').hide();
            $('.passconfdifferent').hide();
            return false; 
        } else if ($("input[name='romaji']").val() == '' && $("input[name='passconf']").val() == '') {
            //ローマ字、パスワード(確認用)が入力されていない場合
            $('.nameblank').hide();
            $('.romajiblank').show();
            $('.mailblank').hide();
            $('.passblank').hide();
            $('.passconfblank').show();
            $('.passformatcheck').hide();
            $('.passconfformatcheck').hide();
            $('.passconfdifferent').hide();
            return false; 
        } else if ($("input[name='mail']").val() == '' && $("input[name='pass']").val() == '') {
            //メール、パスワードが入力されていない場合
            $('.nameblank').hide();
            $('.romajiblank').hide();
            $('.mailblank').show();
            $('.passblank').show();
            $('.passconfblank').hide();
            $('.passformatcheck').hide();
            $('.passconfformatcheck').hide();
            $('.passconfdifferent').hide();
            return false; 
        } else if ($("input[name='mail']").val() == '' && $("input[name='passconf']").val() == '') {
            //メール、パスワード(確認用)が入力されていない場合
            $('.nameblank').hide();
            $('.romajiblank').hide();
            $('.mailblank').show();
            $('.passblank').hide();
            $('.passconfblank').show();
            $('.passformatcheck').hide();
            $('.passconfformatcheck').hide();
            $('.passconfdifferent').hide();
            return false; 
        } else if ($("input[name='pass']").val() == '' && $("input[name='passconf']").val() == '') {
            //パスワード、パスワード(確認用)が入力されていない場合
            $('.nameblank').hide();
            $('.romajiblank').hide();
            $('.mailblank').hide();
            $('.passblank').show();
            $('.passconfblank').show();
            $('.passformatcheck').hide();
            $('.passconfformatcheck').hide();
            $('.passconfdifferent').hide();
            return false; 
        } else if ($("input[name='name']").val() == '') {
            //名前が入力されていない場合
            $('.nameblank').show();
            $('.romajiblank').hide();
            $('.mailblank').hide();
            $('.passblank').hide();
            $('.passconfblank').hide();
            $('.passformatcheck').hide();
            $('.passconfformatcheck').hide();
            $('.passconfdifferent').hide();
            return false; 
        } else if ($("input[name='romaji']").val() == '') {
            //ローマ字が入力されていない場合
            $('.nameblank').hide();
            $('.romajiblank').show();
            $('.mailblank').hide();
            $('.passblank').hide();
            $('.passconfblank').hide();
            $('.passformatcheck').hide();
            $('.passconfformatcheck').hide();
            $('.passconfdifferent').hide();
            return false; 
        } else if ($("input[name='mail']").val() == '') {
            //メールが入力されていない場合
            $('.nameblank').hide();
            $('.romajiblank').hide();
            $('.mailblank').show();
            $('.passblank').hide();
            $('.passconfblank').hide();
            $('.passformatcheck').hide();
            $('.passconfformatcheck').hide();
            $('.passconfdifferent').hide();
            return false; 
        } else if ($("input[name='pass']").val() == '') {
            //パスワードが入力されていない場合
            $('.nameblank').hide();
            $('.romajiblank').hide();
            $('.mailblank').hide();
            $('.passblank').show();
            $('.passconfblank').hide();
            $('.passformatcheck').hide();
            $('.passconfformatcheck').hide();
            $('.passconfdifferent').hide();
            return false; 
        } else if ($("input[name='passconf']").val() == '') {
            //パスワード(確認用)が入力されていない場合
            $('.nameblank').hide();
            $('.romajiblank').hide();
            $('.mailblank').hide();
            $('.passblank').hide();
            $('.passconfblank').show();
            $('.passformatcheck').hide();
            $('.passconfformatcheck').hide();
            $('.passconfdifferent').hide();
            return false;
        } else if (!$("input[name='pass']").val().match(/^[0-9a-zA-Z]{8,32}$/) && !$("input[name='passconf']").val().match(/^[0-9a-zA-Z]{8,32}$/)) {
            //パスワードとパスワード(確認用)の文字数が違う場合
            $('.nameblank').hide();
            $('.romajiblank').hide();
            $('.mailblank').hide();
            $('.passblank').hide();
            $('.passconfblank').hide();
            $('.passformatcheck').show();
            $('.passconfformatcheck').show();
            $('.passconfdifferent').hide();
            return false;
        } else if (!$("input[name='pass']").val().match(/^[0-9a-zA-Z]{8,32}$/)) {
            //パスワードの文字数が違う場合
            $('.nameblank').hide();
            $('.romajiblank').hide();
            $('.mailblank').hide();
            $('.passblank').hide();
            $('.passconfblank').hide();
            $('.passformatcheck').show();
            $('.passconfformatcheck').hide();
            $('.passconfdifferent').hide();
            return false;
        } else if (!$("input[name='passconf']").val().match(/^[0-9a-zA-Z]{8,32}$/)) {
            //パスワード(確認用)の文字数が違う場合
            $('.nameblank').hide();
            $('.romajiblank').hide();
            $('.mailblank').hide();
            $('.passblank').hide();
            $('.passconfblank').hide();
            $('.passformatcheck').hide();
            $('.passconfformatcheck').show();
            $('.passconfdifferent').hide();
            return false;
        } else if ($("input[name='pass']").val() !== $("input[name='passconf']").val()) {
            //パスワードとパスワード(確認用)が異なる場合
            $('.nameblank').hide();
            $('.romajiblank').hide();
            $('.mailblank').hide();
            $('.passblank').hide();
            $('.passconfblank').hide();
            $('.passformatcheck').hide();
            $('.passconfformatcheck').hide();
            $('.passconfdifferent').show();
            return false;
        } else {
          $("form").submit();
        }
    });
}); 