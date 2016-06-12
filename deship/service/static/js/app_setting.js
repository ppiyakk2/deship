// 사용자 ID 획득
$(function()
{
	var id = $.cookie('user_id');
	decodeURIComponent(id);
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

// 사용자 설정 화면으로 전환
function toRule()
{
	window.location.href="/rule/"+thisSN+"/page";
}

// 미구현 알람
function  notYet()
{
	alert("해당 장치(혹은 기능)는 아직 이용할 수 없습니다.");
}

// 장치 상세정보 조회
$(function(){
	var URLis = "/device/";
	URLis += thisSN;
	$.ajax({
		type:"GET",
		url:URLis,
		dataType:"json",
		success:function(data){
			device = data["device"];
			$("#SN").html(device.SN);
			$("#h3_name").html(device.device_name);
			$("#type").html(device.device_type);
			$("#date").html(device.productive_date);
			if(device.device_name == "성수성수"){
				$("#devPic").attr("src","/static/imgs/wahsing_machine_pic.png");
			}
			var tableID = $("#table_").attr("id")+thisSN;
			$("#table_").attr("id",tableID);
		}
	});
});

// 장치 상태 정보 획득
function updateStatus(thisSN){
	var URLis="/device/";
	URLis += thisSN +"/status";
	$.ajax({
		type:"GET",
		url:URLis,
		dataType:"json",
		success:function(data){
			var status = data["device_status"];
			var stat;
			var amount = status.amount;
			if(status.power == 1){
				stat = "전원 켜짐";
			}
			else if(status.power == 0){
				stat = "전원 꺼짐";
			}
			$("#status").html(stat);
			$("#amount").html(amount);
		}
	});
}


function checkAlarm(thisSN)
{
	var URLis="/device/";
	URLis += thisSN +"/alarm";
	$.ajax({
		type:"GET",
		url:URLis,
		dataType:"json",
		success:function(data){
			var status = data["alarm"];
			if(status)
				alert("세탁기에 세제가 부족합니다.")
		}
	});
}

// 장치 상태 1초 단위 갱신
$(function(){
	setInterval("updateStatus('MSIP-CCM-HUW-H1512')",1000);
	setInterval("checkAlarm('MSIP-CCM-HUW-H1512')",1000);
});
// 하단 버튼 중앙 정렬
/*$( document ).ready(function() {
    	$(window).resize();
}); 
$(window).resize(function(){	
	$('#navbar_bottom').css({position:'fixed'}).css({
 		left: ($(window).width() - $('#navbar_bottom').outerWidth())/2
     });
});*/