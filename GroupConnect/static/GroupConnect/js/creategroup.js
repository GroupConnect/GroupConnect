/* アイコン選択 */
$(function() {
    // 画像がクリックされた時の処理です。
    $('.thumbnail').click(function() {
      var $imageList = $('.image_list');
  
      // 現在の選択を解除します。
      $imageList.find('.thumbnail.checked').removeClass('checked');
  
      // チェックを入れた状態にします。
      $(this).addClass('checked');
    });
});

$(function(){
    tr_default("#tbl1");
    tr_default("#tbl2");
    $("#tbl1 tr").click(function(){
      tr_default("#tbl1");
      tr_click($(this));
    });
    $("#tbl2 tr").click(function(){
      tr_default("#tbl2");
      tr_click($(this));
    });
});
 
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