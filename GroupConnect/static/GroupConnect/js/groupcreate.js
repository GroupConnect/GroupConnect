
/* アイコン選択 */
$(function() {
  $('.image_box .disabled_checkbox').click(function() {
    return false;
  });

  // 画像がクリックされた時の処理です。
  $('.image_box label').click(function() {
    var $this = $(this);
    var $imageList = $('.image_list');


    $imageList.find('img.thumbnail.checked').removeClass('checked');
    $imageList.find('input.disabled_checkbox').prop("checked", false);

    $this.find('img.thumbnail').addClass('checked');
    $this.find('input.disabled_checkbox').prop("checked", true);


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
var number = 0;
function add(){
  number ++;
  var mail = document.getElementById('mail').value;
  var div_element = document.createElement("div");
  div_element.id='item' + number;
  div_element.className="range"
  div_element.innerHTML = '<p class="d-inline mail-address">'+ mail +'</p><button onclick="del()" type="button" class="btn mail-delete">削除</button>';
  var parent_object = document.getElementById('mail-range')
  parent_object.appendChild(div_element);
}

function del(){
  var div_element = document.getElementById('item' + number);
  document.getElementById('mail-range').removeChild(div_element);
}