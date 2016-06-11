// 사용자 ID 획득
$(function()
{
	var id = $.cookie('user_id');
	var name = $.cookie('user_name');
	decodeURIComponent(id);
	decodeURIComponent(name);
	$('#navbar_top_username').html(name);
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

// 사용자 설정 화면으로 전환
function toRule()
{
	window.location.href="http://211.198.65.241:38080/rule";
}

// 미구현 알람
function  notYet()
{
	alert("해당 장치(혹은 기능)는 아직 이용할 수 없습니다.");
}
// 하단 버튼 중앙 정렬
/*$( document ).ready(function() {
    	$(window).resize();
}); 
$(window).resize(function(){	
	$('#navbar_bottom').css({position:'fixed'}).css({
 		left: ($(window).width() - $('#navbar_bottom').outerWidth())/2
     });
});*/