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

// 미구현 알람
function toRule(thisID)
{
	if(thisID == "washing_machine")
	{
		window.location.href= "http://211.198.65.241:38080/rule";
	}
	else
	{
		alert("해당 장치(혹은 기능)는 아직 이용할 수 없습니다.");
	}
}
