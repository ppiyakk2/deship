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

// 장치 추가 시 입력한 SN에 해당하는 장치 정보 조회
function getDeviceInfo()
{
	
}

// 장치 추가, 장치 정보를 서버로 전송
function regDevice()
{
	
}