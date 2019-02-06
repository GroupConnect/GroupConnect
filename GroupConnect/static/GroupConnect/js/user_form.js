$(document).on('change', ':file', function() {
    var input = $(this),
    numFiles = input.get(0).files ? input.get(0).files.length : 1,
    label = input.val().replace(/\\/g, '/').replace(/.*\//, '');
    input.parent().parent().next(':text').val(label);
});

$(function() {
    $("form").submit(function(){
        if ($("input[name='last_name']").val() == '' && $("input[name='first_name']").val() == '' && $("input[name='rome_last_name']").val() == '' && $("input[name='rome_first_name']").val() == '') {
            //苗字、名前、苗字(ローマ字)、名前(ローマ字)が入力されていない場合
            $('.last_nameblank').show();
            $('.last_namecheck').hide();
            $('.first_nameblank').show();
            $('.first_namecheck').hide();
            $('.rome_last_nameblank').show();
            $('.rome_last_namecheck').hide();
            $('.rome_first_nameblank').show();
            $('.rome_first_namecheck').hide();
            return false;
        } else if (!$("input[name='last_name']").val().match(/^[^　\x20-\x7e]+$/) && $("input[name='first_name']").val() == '' && $("input[name='rome_last_name']").val() == '' && $("input[name='rome_first_name']").val() == '') {
            //名前、苗字(ローマ字)、名前(ローマ字)が入力されてなく、苗字に全角文字以外の文字が入っている場合
            $('.last_nameblank').hide();
            $('.last_namecheck').show();
            $('.first_nameblank').show();
            $('.first_namecheck').hide();
            $('.rome_last_nameblank').show();
            $('.rome_last_namecheck').hide();
            $('.rome_first_nameblank').show();
            $('.rome_first_namecheck').hide();
            return false;
        } else if ($("input[name='first_name']").val() == '' && $("input[name='rome_last_name']").val() == '' && $("input[name='rome_first_name']").val() == '') {
            //名前、苗字(ローマ字)、名前(ローマ字)が入力されていない場合
            $('.last_nameblank').hide();
            $('.last_namecheck').hide();
            $('.first_nameblank').show();
            $('.first_namecheck').hide();
            $('.rome_last_nameblank').show();
            $('.rome_last_namecheck').hide();
            $('.rome_first_nameblank').show();
            $('.rome_first_namecheck').hide();
            return false;
        } else if (!$("input[name='first_name']").val().match(/^[^　\x20-\x7e]+$/) && $("input[name='last_name']").val() == '' && $("input[name='rome_last_name']").val() == '' && $("input[name='rome_first_name']").val() == '') {
            //苗字、苗字(ローマ字)、名前(ローマ字)が入力されてなく、名前に全角文字以外の文字が入っている場合
            $('.last_nameblank').show();
            $('.last_namecheck').hide();
            $('.first_nameblank').hide();
            $('.first_namecheck').show();
            $('.rome_last_nameblank').show();
            $('.rome_last_namecheck').hide();
            $('.rome_first_nameblank').show();
            $('.rome_first_namecheck').hide();
            return false;
        } else if ($("input[name='last_name']").val() == '' && $("input[name='rome_last_name']").val() == '' && $("input[name='rome_first_name']").val() == '') {
            //苗字、苗字(ローマ字)、名前(ローマ字)が入力されていない場合
            $('.last_nameblank').show();
            $('.last_namecheck').hide();
            $('.first_nameblank').hide();
            $('.first_namecheck').hide();
            $('.rome_last_nameblank').show();
            $('.rome_last_namecheck').hide();
            $('.rome_first_nameblank').show();
            $('.rome_first_namecheck').hide();
            return false;
        } else if (!$("input[name='rome_last_name']").val().match(/^[a-zA-Z]+$/) && $("input[name='last_name']").val() == '' && $("input[name='first_name']").val() == '' && $("input[name='rome_first_name']").val() == '') {
            //苗字、名前、名前(ローマ字)が入力されてなく、苗字(ローマ字)に半角英字以外の文字が入っている場合
            $('.last_nameblank').show();
            $('.last_namecheck').hide();
            $('.first_nameblank').show();
            $('.first_namecheck').hide();
            $('.rome_last_nameblank').hide();
            $('.rome_last_namecheck').show();
            $('.rome_first_nameblank').show();
            $('.rome_first_namecheck').hide();
            return false;
        } else if ($("input[name='last_name']").val() == '' && $("input[name='first_name']").val() == '' && $("input[name='rome_first_name']").val() == '') {
            //苗字、名前、名前(ローマ字)が入力されていない場合
            $('.last_nameblank').show();
            $('.last_namecheck').hide();
            $('.first_nameblank').show();
            $('.first_namecheck').hide();
            $('.rome_last_nameblank').hide();
            $('.rome_last_namecheck').hide();
            $('.rome_first_nameblank').show();
            $('.rome_first_namecheck').hide();
            return false;
        } else if (!$("input[name='rome_first_name']").val().match(/^[a-zA-Z]+$/) && $("input[name='last_name']").val() == '' && $("input[name='first_name']").val() == '' && $("input[name='rome_last_name']").val() == '') {
            //苗字、名前、苗字(ローマ字)が入力されてなく、名前(ローマ字)に半角英字以外の文字が入っている場合
            $('.last_nameblank').show();
            $('.last_namecheck').hide();
            $('.first_nameblank').show();
            $('.first_namecheck').hide();
            $('.rome_last_nameblank').show();
            $('.rome_last_namecheck').hide();
            $('.rome_first_nameblank').hide();
            $('.rome_first_namecheck').show();
            return false;
        } else if ($("input[name='last_name']").val() == '' && $("input[name='first_name']").val() == '' && $("input[name='rome_last_name']").val() == '') {
            //苗字、名前、苗字(ローマ字)が入力されていない場合
            $('.last_nameblank').show();
            $('.last_namecheck').hide();
            $('.first_nameblank').show();
            $('.first_namecheck').hide();
            $('.rome_last_nameblank').show();
            $('.rome_last_namecheck').hide();
            $('.rome_first_nameblank').hide();
            $('.rome_first_namecheck').hide();
            return false;
        } else if (!$("input[name='last_name']").val().match(/^[^　\x20-\x7e]+$/) && !$("input[name='first_name']").val().match(/^[^　\x20-\x7e]+$/) && $("input[name='rome_last_name']").val() == '' && $("input[name='rome_first_name']").val() == '') {
            //苗字(ローマ字)、名前(ローマ字)が入力されてなく、苗字と名前に全角文字以外の文字が入っている場合
            $('.last_nameblank').hide();
            $('.last_namecheck').show();
            $('.first_nameblank').hide();
            $('.first_namecheck').show();
            $('.rome_last_nameblank').show();
            $('.rome_last_namecheck').hide();
            $('.rome_first_nameblank').show();
            $('.rome_first_namecheck').hide();
            return false;
        } else if (!$("input[name='last_name']").val().match(/^[^　\x20-\x7e]+$/) && $("input[name='rome_last_name']").val() == '' && $("input[name='rome_first_name']").val() == '') {
            //苗字(ローマ字)、名前(ローマ字)が入力されてなく、苗字に全角文字以外の文字が入っている場合
            $('.last_nameblank').hide();
            $('.last_namecheck').show();
            $('.first_nameblank').hide();
            $('.first_namecheck').hide();
            $('.rome_last_nameblank').show();
            $('.rome_last_namecheck').hide();
            $('.rome_first_nameblank').show();
            $('.rome_first_namecheck').hide();
            return false;
        } else if (!$("input[name='first_name']").val().match(/^[^　\x20-\x7e]+$/) && $("input[name='rome_last_name']").val() == '' && $("input[name='rome_first_name']").val() == '') {
            //苗字(ローマ字)、名前(ローマ字)が入力されてなく、名前に全角文字以外の文字が入っている場合
            $('.last_nameblank').hide();
            $('.last_namecheck').hide();
            $('.first_nameblank').hide();
            $('.first_namecheck').show();
            $('.rome_last_nameblank').show();
            $('.rome_last_namecheck').hide();
            $('.rome_first_nameblank').show();
            $('.rome_first_namecheck').hide();
            return false;
        } else if ($("input[name='rome_last_name']").val() == '' && $("input[name='rome_first_name']").val() == '') {
            //苗字(ローマ字)、名前(ローマ字)が入力されていない場合
            $('.last_nameblank').hide();
            $('.last_namecheck').hide();
            $('.first_nameblank').hide();
            $('.first_namecheck').hide();
            $('.rome_last_nameblank').show();
            $('.rome_last_namecheck').hide();
            $('.rome_first_nameblank').show();
            $('.rome_first_namecheck').hide();
            return false;
        } else if (!$("input[name='last_name']").val().match(/^[^　\x20-\x7e]+$/) && !$("input[name='rome_last_name']").val().match(/^[a-zA-Z]+$/) && $("input[name='first_name']").val() == '' && $("input[name='rome_first_name']").val() == '') {
            //名前、名前(ローマ字)が入力されてなく、苗字(ローマ字)に半角英字以外の文字が入っていて、苗字に全角文字以外の文字が入っている場合
            $('.last_nameblank').hide();
            $('.last_namecheck').show();
            $('.first_nameblank').show();
            $('.first_namecheck').hide();
            $('.rome_last_nameblank').hide();
            $('.rome_last_namecheck').show();
            $('.rome_first_nameblank').show();
            $('.rome_first_namecheck').hide();
            return false;
        } else if (!$("input[name='last_name']").val().match(/^[^　\x20-\x7e]+$/) && $("input[name='first_name']").val() == '' && $("input[name='rome_first_name']").val() == '') {
            //名前、名前(ローマ字)が入力されてなく、苗字に全角文字以外の文字が入っている場合
            $('.last_nameblank').hide();
            $('.last_namecheck').show();
            $('.first_nameblank').show();
            $('.first_namecheck').hide();
            $('.rome_last_nameblank').hide();
            $('.rome_last_namecheck').hide();
            $('.rome_first_nameblank').show();
            $('.rome_first_namecheck').hide();
            return false;
        } else if (!$("input[name='rome_last_name']").val().match(/^[a-zA-Z]+$/) && $("input[name='first_name']").val() == '' && $("input[name='rome_first_name']").val() == '') {
            //名前、名前(ローマ字)が入力されてなく、苗字(ローマ字)に半角英字以外の文字が入っている場合
            $('.last_nameblank').hide();
            $('.last_namecheck').hide();
            $('.first_nameblank').show();
            $('.first_namecheck').hide();
            $('.rome_last_nameblank').hide();
            $('.rome_last_namecheck').show();
            $('.rome_first_nameblank').show();
            $('.rome_first_namecheck').hide();
            return false;
        } else if ($("input[name='first_name']").val() == '' && $("input[name='rome_first_name']").val() == '') {
            //名前、名前(ローマ字)が入力されていない場合
            $('.last_nameblank').hide();
            $('.last_namecheck').hide();
            $('.first_nameblank').show();
            $('.first_namecheck').hide();
            $('.rome_last_nameblank').hide();
            $('.rome_last_namecheck').hide();
            $('.rome_first_nameblank').show();
            $('.rome_first_namecheck').hide();
            return false;
        } else if (!$("input[name='last_name']").val().match(/^[^　\x20-\x7e]+$/) && !$("input[name='rome_first_name']").val().match(/^[a-zA-Z]+$/) && $("input[name='first_name']").val() == '' && $("input[name='rome_last_name']").val() == '') {
            //名前、苗字(ローマ字)が入力されてなく、名前(ローマ字)に半角英字以外の文字が入っていて、苗字に全角文字以外の文字が入っている場合
            $('.last_nameblank').hide();
            $('.last_namecheck').show();
            $('.first_nameblank').show();
            $('.first_namecheck').hide();
            $('.rome_last_nameblank').show();
            $('.rome_last_namecheck').hide();
            $('.rome_first_nameblank').hide();
            $('.rome_first_namecheck').show();
            return false;
        } else if (!$("input[name='last_name']").val().match(/^[^　\x20-\x7e]+$/) && $("input[name='first_name']").val() == '' && $("input[name='rome_last_name']").val() == '') {
            //名前、苗字(ローマ字)が入力されてなく、苗字に全角文字以外の文字が入っている場合
            $('.last_nameblank').hide();
            $('.last_namecheck').show();
            $('.first_nameblank').show();
            $('.first_namecheck').hide();
            $('.rome_last_nameblank').show();
            $('.rome_last_namecheck').hide();
            $('.rome_first_nameblank').hide();
            $('.rome_first_namecheck').hide();
            return false;
        } else if (!$("input[name='rome_first_name']").val().match(/^[a-zA-Z]+$/) && $("input[name='first_name']").val() == '' && $("input[name='rome_last_name']").val() == '') {
            //名前、苗字(ローマ字)が入力されてなく、名前(ローマ字)に半角英字以外の文字が入っている場合
            $('.last_nameblank').hide();
            $('.last_namecheck').hide();
            $('.first_nameblank').show();
            $('.first_namecheck').hide();
            $('.rome_last_nameblank').show();
            $('.rome_last_namecheck').hide();
            $('.rome_first_nameblank').hide();
            $('.rome_first_namecheck').show();
            return false;
        } else if ($("input[name='first_name']").val() == '' && $("input[name='rome_last_name']").val() == '') {
            //名前、苗字(ローマ字)が入力されていない場合
            $('.last_nameblank').hide();
            $('.last_namecheck').hide();
            $('.first_nameblank').show();
            $('.first_namecheck').hide();
            $('.rome_last_nameblank').show();
            $('.rome_last_namecheck').hide();
            $('.rome_first_nameblank').hide();
            $('.rome_first_namecheck').hide();
            return false;
        } else if (!$("input[name='first_name']").val().match(/^[^　\x20-\x7e]+$/) && !$("input[name='rome_first_name']").val().match(/^[a-zA-Z]+$/) && $("input[name='last_name']").val() == '' && $("input[name='rome_last_name']").val() == '') {
            //苗字、苗字(ローマ字)が入力されてなく、名前に全角文字以外の文字が入っていて、名前(ローマ字)に半角英字以外の文字が入っている場合
            $('.last_nameblank').show();
            $('.last_namecheck').hide();
            $('.first_nameblank').hide();
            $('.first_namecheck').show();
            $('.rome_last_nameblank').show();
            $('.rome_last_namecheck').hide();
            $('.rome_first_nameblank').hide();
            $('.rome_first_namecheck').show();
            return false;
        } else if (!$("input[name='first_name']").val().match(/^[^　\x20-\x7e]+$/) && $("input[name='last_name']").val() == '' && $("input[name='rome_last_name']").val() == '') {
            //苗字、苗字(ローマ字)が入力されてなく、名前に全角文字以外の文字が入っている場合
            $('.last_nameblank').show();
            $('.last_namecheck').hide();
            $('.first_nameblank').hide();
            $('.first_namecheck').show();
            $('.rome_last_nameblank').show();
            $('.rome_last_namecheck').hide();
            $('.rome_first_nameblank').hide();
            $('.rome_first_namecheck').hide();
            return false;
        } else if (!$("input[name='rome_first_name']").val().match(/^[a-zA-Z]+$/) && $("input[name='last_name']").val() == '' && $("input[name='rome_last_name']").val() == '') {
            //苗字、苗字(ローマ字)が入力されてなく、名前(ローマ字)に半角英字以外の文字が入っている場合
            $('.last_nameblank').show();
            $('.last_namecheck').hide();
            $('.first_nameblank').hide();
            $('.first_namecheck').hide();
            $('.rome_last_nameblank').show();
            $('.rome_last_namecheck').hide();
            $('.rome_first_nameblank').hide();
            $('.rome_first_namecheck').show();
            return false;
        } else if ($("input[name='last_name']").val() == '' && $("input[name='rome_last_name']").val() == '') {
            //苗字、苗字(ローマ字)が入力されていない場合
            $('.last_nameblank').show();
            $('.last_namecheck').hide();
            $('.first_nameblank').hide();
            $('.first_namecheck').hide();
            $('.rome_last_nameblank').show();
            $('.rome_last_namecheck').hide();
            $('.rome_first_nameblank').hide();
            $('.rome_first_namecheck').hide();
            return false;
        } else if (!$("input[name='first_name']").val().match(/^[^　\x20-\x7e]+$/) && !$("input[name='rome_last_name']").val().match(/^[a-zA-Z]+$/) && $("input[name='last_name']").val() == '' && $("input[name='rome_first_name']").val() == '') {
            //苗字、名前(ローマ字)が入力されてなく、苗字(ローマ字)に半角英字以外の文字が入っていて、名前に全角文字以外の文字が入っている場合
            $('.last_nameblank').show();
            $('.last_namecheck').hide();
            $('.first_nameblank').hide();
            $('.first_namecheck').show();
            $('.rome_last_nameblank').hide();
            $('.rome_last_namecheck').show();
            $('.rome_first_nameblank').show();
            $('.rome_first_namecheck').hide();
            return false;
        } else if (!$("input[name='first_name']").val().match(/^[^　\x20-\x7e]+$/) && $("input[name='last_name']").val() == '' && $("input[name='rome_first_name']").val() == '') {
            //苗字、名前(ローマ字)が入力されてなく、名前に全角文字以外の文字が入っている場合
            $('.last_nameblank').show();
            $('.last_namecheck').hide();
            $('.first_nameblank').hide();
            $('.first_namecheck').show();
            $('.rome_last_nameblank').hide();
            $('.rome_last_namecheck').hide();
            $('.rome_first_nameblank').show();
            $('.rome_first_namecheck').hide();
            return false;
        } else if (!$("input[name='rome_last_name']").val().match(/^[a-zA-Z]+$/) && $("input[name='last_name']").val() == '' && $("input[name='rome_first_name']").val() == '') {
            //苗字、名前(ローマ字)が入力されてなく、苗字(ローマ字)に半角英字以外の文字が入っている場合
            $('.last_nameblank').show();
            $('.last_namecheck').hide();
            $('.first_nameblank').hide();
            $('.first_namecheck').hide();
            $('.rome_last_nameblank').hide();
            $('.rome_last_namecheck').show();
            $('.rome_first_nameblank').show();
            $('.rome_first_namecheck').hide();
            return false;
        } else if ($("input[name='last_name']").val() == '' && $("input[name='rome_first_name']").val() == '') {
            //苗字、名前(ローマ字)が入力されていない場合
            $('.last_nameblank').show();
            $('.last_namecheck').hide();
            $('.first_nameblank').hide();
            $('.first_namecheck').hide();
            $('.rome_last_nameblank').hide();
            $('.rome_last_namecheck').hide();
            $('.rome_first_nameblank').show();
            $('.rome_first_namecheck').hide();
            return false;
        } else if (!$("input[name='rome_last_name']").val().match(/^[a-zA-Z]+$/) && !$("input[name='rome_first_name']").val().match(/^[a-zA-Z]+$/) && $("input[name='last_name']").val() == '' && $("input[name='first_name']").val() == '') {
            //苗字、名前が入力されてなく、苗字(ローマ字)と名前(ローマ字)に半角英字以外の文字が入っている場合
            $('.last_nameblank').show();
            $('.last_namecheck').hide();
            $('.first_nameblank').show();
            $('.first_namecheck').hide();
            $('.rome_last_nameblank').hide();
            $('.rome_last_namecheck').show();
            $('.rome_first_nameblank').hide();
            $('.rome_first_namecheck').show();
            return false;
        } else if (!$("input[name='rome_last_name']").val().match(/^[a-zA-Z]+$/) && $("input[name='last_name']").val() == '' && $("input[name='first_name']").val() == '') {
            //苗字、名前が入力されてなく、苗字(ローマ字)に半角英字以外の文字が入っている場合
            $('.last_nameblank').show();
            $('.last_namecheck').hide();
            $('.first_nameblank').show();
            $('.first_namecheck').hide();
            $('.rome_last_nameblank').hide();
            $('.rome_last_namecheck').show();
            $('.rome_first_nameblank').hide();
            $('.rome_first_namecheck').hide();
            return false;
        } else if (!$("input[name='rome_first_name']").val().match(/^[a-zA-Z]+$/) && $("input[name='last_name']").val() == '' && $("input[name='first_name']").val() == '') {
            //苗字、名前が入力されてなく、名前(ローマ字)に半角英字以外の文字が入っている場合
            $('.last_nameblank').show();
            $('.last_namecheck').hide();
            $('.first_nameblank').show();
            $('.first_namecheck').hide();
            $('.rome_last_nameblank').hide();
            $('.rome_last_namecheck').hide();
            $('.rome_first_nameblank').hide();
            $('.rome_first_namecheck').show();
            return false;
        } else if ($("input[name='last_name']").val() == '' && $("input[name='first_name']").val() == '') {
            //苗字、名前が入力されていない場合
            $('.last_nameblank').show();
            $('.last_namecheck').hide();
            $('.first_nameblank').show();
            $('.first_namecheck').hide();
            $('.rome_last_nameblank').hide();
            $('.rome_last_namecheck').hide();
            $('.rome_first_nameblank').hide();
            $('.rome_first_namecheck').hide();
            return false;
        } else if ($("input[name='last_name']").val() == '' && !$("input[name='first_name']").val().match(/^[^　\x20-\x7e]+$/) && !$("input[name='rome_last_name']").val().match(/^[a-zA-Z]+$/) && !$("input[name='rome_first_name']").val().match(/^[a-zA-Z]+$/) ) {
            //苗字が入力されてなく、名前に全角文字以外の文字が入っていて、苗字[ローマ字]と名前[ローマ字]に半角英字以外の文字が入っている場合
            $('.last_nameblank').show();
            $('.last_namecheck').hide();
            $('.first_nameblank').hide();
            $('.first_namecheck').show();
            $('.rome_last_nameblank').hide();
            $('.rome_last_namecheck').show();
            $('.rome_first_nameblank').hide();
            $('.rome_first_namecheck').show();
            return false;
        } else if ($("input[name='last_name']").val() == '' && !$("input[name='first_name']").val().match(/^[^　\x20-\x7e]+$/) && !$("input[name='rome_last_name']").val().match(/^[a-zA-Z]+$/)) {
            //苗字が入力されてなく、名前に全角文字以外の文字が入っていて、苗字[ローマ字]に半角英字以外の文字が入っている場合
            $('.last_nameblank').show();
            $('.last_namecheck').hide();
            $('.first_nameblank').hide();
            $('.first_namecheck').show();
            $('.rome_last_nameblank').hide();
            $('.rome_last_namecheck').show();
            $('.rome_first_nameblank').hide();
            $('.rome_first_namecheck').hide();
            return false;
        } else if ($("input[name='last_name']").val() == '' && !$("input[name='first_name']").val().match(/^[^　\x20-\x7e]+$/) && !$("input[name='rome_first_name']").val().match(/^[a-zA-Z]+$/)) {
            //苗字が入力されてなく、名前に全角文字以外の文字が入っていて、名前[ローマ字]に半角英字以外の文字が入っている場合
            $('.last_nameblank').show();
            $('.last_namecheck').hide();
            $('.first_nameblank').hide();
            $('.first_namecheck').show();
            $('.rome_last_nameblank').hide();
            $('.rome_last_namecheck').hide();
            $('.rome_first_nameblank').hide();
            $('.rome_first_namecheck').show();
            return false;
        } else if (!$("input[name='last_name']").val().match(/^[^　\x20-\x7e]+$/)) {
            //苗字に全角文字以外の文字が入っている場合(空白不可)
            $('.last_nameblank').hide();
            $('.last_namecheck').show();
            $('.first_nameblank').hide();
            $('.first_namecheck').hide();
            $('.rome_last_nameblank').hide();
            $('.rome_last_namecheck').hide();
            $('.rome_first_nameblank').hide();
            $('.rome_first_namecheck').hide();
            return false;
        } else if (!$("input[name='first_name']").val().match(/^[^　\x20-\x7e]+$/)) {
            //名前に全角文字以外の文字が入っている場合(空白不可)
            $('.last_nameblank').hide();
            $('.last_namecheck').hide();
            $('.first_nameblank').hide();
            $('.first_namecheck').show();
            $('.rome_last_nameblank').hide();
            $('.rome_last_namecheck').hide();
            $('.rome_first_nameblank').hide();
            $('.rome_first_namecheck').hide();
            return false;
        } else if (!$("input[name='rome_last_name']").val().match(/^[a-zA-Z]+$/)) {
            //苗字(ローマ字)に半角英字以外の文字が入っている場合
            $('.last_nameblank').hide();
            $('.last_namecheck').hide();
            $('.first_nameblank').hide();
            $('.first_namecheck').hide();
            $('.rome_last_nameblank').hide();
            $('.rome_last_namecheck').show();
            $('.rome_first_nameblank').hide();
            $('.rome_first_namecheck').hide();
            return false;
        } else if (!$("input[name='rome_first_name']").val().match(/^[a-zA-Z]+$/)) {
            //名前(ローマ字)に半角英字以外の文字が入っている場合
            $('.last_nameblank').hide();
            $('.last_namecheck').hide();
            $('.first_nameblank').hide();
            $('.first_namecheck').hide();
            $('.rome_last_nameblank').hide();
            $('.rome_last_namecheck').hide();
            $('.rome_first_nameblank').hide();
            $('.rome_first_namecheck').show();
            return false;
        } else if ($("input[name='last_name']").val() == '') {
            //苗字が入力されていない場合
            $('.last_nameblank').show();
            $('.last_namecheck').hide();
            $('.first_nameblank').hide();
            $('.first_namecheck').hide();
            $('.rome_last_nameblank').hide();
            $('.rome_last_namecheck').hide();
            $('.rome_first_nameblank').hide();
            $('.rome_first_namecheck').hide();
            return false;
        } else if ($("input[name='first_name']").val() == '') {
            //名前が入力されていない場合
            $('.last_nameblank').hide();
            $('.last_namecheck').hide();
            $('.first_nameblank').show();
            $('.first_namecheck').hide();
            $('.rome_last_nameblank').hide();
            $('.rome_last_namecheck').hide();
            $('.rome_first_nameblank').hide();
            $('.rome_first_namecheck').hide();
            return false;
        } else　if ($("input[name='rome_last_name']").val() == '') {
            //苗字(ローマ字)が入力されていない場合
            $('.last_nameblank').hide();
            $('.last_namecheck').hide();
            $('.first_nameblank').hide();
            $('.first_namecheck').hide();
            $('.rome_last_nameblank').show();
            $('.rome_last_namecheck').hide();
            $('.rome_first_nameblank').hide();
            $('.rome_first_namecheck').hide();
            return false;
        } else if ($("input[name='rome_first_name']").val() == '') {
            //名前(ローマ字)が入力されていない場合
            $('.last_nameblank').hide();
            $('.last_namecheck').hide();
            $('.first_nameblank').hide();
            $('.first_namecheck').hide();
            $('.rome_last_nameblank').hide();
            $('.rome_last_namecheck').hide();
            $('.rome_first_nameblank').show();
            $('.rome_first_namecheck').hide();
            return false;
        } else {
            $("form").submit();
        }
    });
});