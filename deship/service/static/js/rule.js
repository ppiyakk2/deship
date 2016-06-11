// 사용자 ID 획득
var userID;
$(function(){
	userID = "SampleUser";
	$("#navbar_top_username").html(userID);
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
	window.location.href = "http://211.198.65.241:38080/setting";
}

// 사용자 로그아웃
function logout()
{
	window.location.replace("http://211.198.65.241:38080/");
}

// 장치 추가
function addDevice()
{
	window.location.replace("http://211.198.65.241:38080/add_device");
}

// 메인 화면으로 전환
function toMain()
{
	window.location.replace("http://211.198.65.241:38080/main");
}

// 사용자 설정 옵션 값 획득
var autoCharge;
var autoAlert;
var item_name;
var item_Selected;
function itemSelect(id){
	item_name = $("#"+id+">div>p.item_name").html();
	item_Selected = $("#"+id).attr("value");
	$("#selected_item").html("&nbsp; "+item_name);
}
// 사용자 설정 저장, 서버 전송
function saveRule()
{
	autoCharge = $("#autoChargeVal").val();
	autoAlert = $("#autoAlertVal").val();
	var URLis;
	$.ajax({
		type:"POST",
		url:URLis,
		dataType:"json",
		data:{
			"auto_charge" : autoCharge,
			"auto_alert" : autoAlert,
			"item" : item_Selected
		},
		statusCode:{
			200:function(){
				window.location.replace("http://211.198.65.241:38080/setting");
			}
		}
	});
	//window.location.href="http://211.198.65.241:38080/setting";
}

