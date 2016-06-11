// 사용자 ID 획득
$(function()
{
	var id = $.cookie('user_id');
	var name = $.cookie('user_name');
	decodeURIComponent(id);
	decodeURIComponent(name);
	$('#navbar_top_username').html(name);
});

// 장치 ID 획득
var thisSN;
$(document).ready(function(){
	thisSN = $("#device_id").html();
});

// 상단 네비게이션 바 드롭다운 제어
function toDropdown()
{
	if($("#navbar_top_menu_dropdown").css("display") == "block" )
	{
		$("#navbar_top_menu_dropdown").css("display","none");
	}
	else
	{
		$("#navbar_top_menu_dropdown").css("display","block");
	}
}

// 장치 관리 페이지로 전환
function toSettings()
{
	window.location.href = "/setting";
}

// 사용자 로그아웃
function logout()
{
	window.location.replace("/");
}

// 장치 추가
function addDevice()
{
	window.location.replace("/add_device");
}

// 메인 화면으로 전환
function toMain()
{
	window.location.replace("/main");
}

// 소모품 목록 획득
/*
 * 
 * 
 * 			소모품 목록을 서버에서 받아와 설정 화면에 표시
 * 
 * 
 * 
 *
$(function(){
	var item;
	var URLis = "/item/";
	URLis += thisSN;
	$.ajax({
		type:"GET",
		dataType:"json",
		url:URLis,
		success:function(data){
			// json 데이터 획득
			item = data["itemlist"];
			var content="";
			$.each(item ,function(index, entry){
				content += "<button id=\"btn_"+entry.item_id+"\" class=\"btn_item\" value=\""+entry.item_id+"\" onclick=\"itemSelect(id)\">"
    						+"<img id=\"img_"+entry.item_id+"\" class=\"img_item\" src=\"/static/imgs/"+entry.item_id+".png\"/>"
    						+"<div class=\"divp_item\">"
    							+"<p class=\"item_name\">"+entry.item_name+"</p>"
    							+"<p class=\"item_price\">"+" 원</p>"
    						+"</div>"
    					+"</button>";
			});
			$("#div_itemlist").html(content);
		}
	});
});
* 
* 
* 
* 
* */

// 사용자 설정값 로드
$(function(){
	var URLis = "/rule/"+thisSN;
	$.ajax({
		type:"GET",
		url:URLis,
		dataType:"json",
		success:function(data){
			var rule = data["rule"];
			$("#autoChargeVal").val(rule.criteria).attr("selected","selected");
			$("#autoAlertVal").val(rule.alarm_critera).attr("selected","selected");
			itemSelect(rule.item_id);
		}
	});
});

// 사용자 설정 옵션 값 획득
var autoCharge;
var autoAlert;
var item_name;
var item_Selected;
function itemSelect(id){
	item_name = $("#"+id+">div>p.item_name").html();
	item_Selected = $("#"+id).attr("value");
	$("#selected_item").html("&nbsp; "+item_name+"&nbsp;");
}
// 사용자 설정 저장, 서버 전송
function saveRule()
{
	autoCharge = $("#autoChargeVal").val();
	autoAlert = $("#autoAlertVal").val();
	var URLis = "/rule/"+thisSN;
	$.ajax({
		type:"POST",
		url:URLis,
		dataType:"json",
		data:{
			"criteria" : autoCharge,
			"alarm_critera" : autoAlert,
			"item_id" : item_Selected
		},
		statusCode:{
			200:function(){
				//window.location.replace("/setting/"+thisSN);
			}
		}
	});
	//window.location.href="/setting";
}

