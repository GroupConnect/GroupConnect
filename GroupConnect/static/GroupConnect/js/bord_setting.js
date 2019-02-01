$(function(){
    tr_default("#tbl1");
    $("#tbl1 tr").click(function(){
        tr_default("#tbl1");
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