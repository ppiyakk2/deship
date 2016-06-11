// 사용자 ID 획득
$(function()
{
	var id = $.cookie('user_id');
	decodeURIComponent(id);
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

// 장치 추가 시 입력한 SN에 해당하는 장치 정보 조회
var device;
function getDeviceInfo()
{	//400 : 이미 등록, 404 : 장치 없음
	var SN = $("#register_userid").val();
	var URLis="/device/";
	URLis += SN;
	$.ajax({
		type:"GET",
		url:URLis,
		dataType:"json",
		succcess:function(data){
		},
		statusCode:{
			200:function(data){
				device = data["device"];
				$("#SN").html(device.SN);
				$("#name").html(device.device_name);
				$("#type").html(device.device_type);
				$("#date").html(device.productive_date);
				if(device.device_name == "TS19VD1"){
					$("#device_picture").attr("src","/static/imgs/wahsing_machine_pic.png");
				}
			},
			400:function(){
				$("#SN").html("--");
				$("#name").html("--");
				$("#type").html("--");
				$("#date").html("---- -- --");
				$("#device_picture").attr("src","/static/imgs/no_img.png");
				alert("이미 등록된 장치입니다.");
				},
			404:function(){
				$("#SN").html("--");
				$("#name").html("--");
				$("#type").html("--");
				$("#date").html("---- -- --");	
				$("#device_picture").attr("src","/static/imgs/no_img.png");
				alert("존재하지 않는 장치입니다.");	
				}
		}
	});
}

// 장치 추가, 장치 정보를 서버로 전송
function addDevice_R()
{
	var SN = $("#register_userid").val();
	var URLis="/device";
	$.ajax({
		type:"POST",
		url:URLis,
		dataType:"json",
		data:{
			"SN":device.SN
		},
		statusCode:{
			200:function(){
				alert("장치가 추가되었습니다.");
				window.location.replace("/main");
			}
		}
	});
}