$(document).on('change', ':file', function() {
    var input = $(this),
    numFiles = input.get(0).files ? input.get(0).files.length : 1,
    label = input.val().replace(/\\/g, '/').replace(/.*\//, '');
    input.parent().parent().next(':text').val(label);
});

$(function(){
    tr_default("#tbl1");
    tr_default("#tbl2");
    tr_default("#tbl3");
    tr_default("#tbl4");
    $("#tbl1 tr").click(function(){
        tr_default("#tbl1");
        tr_click($(this));
    });
    $("#tbl2 tr").click(function(){
        tr_default("#tbl2");
        tr_click($(this));
    });
    $("#tbl3 tr").click(function(){
        tr_default("#tbl3");
        tr_click($(this));
    });
    $("#tbl4 tr").click(function(){
        tr_default("#tbl4");
        tr_click($(this));
    });
});

(function($){
    
    $('#btn2').on('click', function(){

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

function tr_default(tblID){
    var vTR = tblID + " tr";
    $(vTR).css("background-color","#ffffff");
    $(vTR).mouseover(function(){
      $(this).css("background-color","#CCFFCC") .css("cursor","pointer")
    });
    $(vTR).mouseout(function(){
      $(this).css("background-color","#ffffff") .css("cursor","normal")
    });
}
 
function tr_click(trID){
    trID.css("background-color","#b4eeff");
    trID.mouseover(function(){
      $(this).css("background-color","#CCFFCC") .css("cursor","pointer")
    });
    trID.mouseout(function(){
      $(this).css("background-color","#b4eeff") .css("cursor","normal")
    });
}
$(function(){
    $("#invite").submit(function(){
	    if($("input[name='mailaddress']").val() == ""){
            $('.email-error').show();
		    return false;
	    }else{
            $('form').submit()
        }
    });
});