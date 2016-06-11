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

// 상세보기
function toDetail(thisID)
{
	if(thisID == "MSIP-CCM-HUW-H1512")
	{
		window.location.href= "/setting/"+thisID;
	}
	else
	{
		alert("해당 장치(혹은 기능)는 아직 이용할 수 없습니다.");
	}
}

// 장치 유형 구분
function typeAcog(type){
	var content="";
	if(type == "세탁기")
	{
		content+= "<img id=\"icon_washing_machine\" class=\"dev_icon\" src=\"/static/imgs/washing_machine.png\"/>"+
    				"<p>상태 : <span class=\"dev_status\">--</span></p>"+
    				"<p>세제 잔여량 : <span class=\"dev_rem\"></span>%</p></button>";
	}
	else
	{
		content+= "<img id=\"icon_switch\" class=\"dev_icon\" src=\"/static/imgs/switch.png\"/>"+
    				"<p>상태 : <span class=\"dev_status\">--</span></p>"+
    				"</button>";
	}
	return content;
}


// 사용자 장치 목록 조회
var device_list;
var loaded = false;
$(function(){
	var URLis="/device";
	
	$.ajax({
		type:"GET",
		url:URLis,
		dataType:"json",
		success:function(data){
			device_list = data["devices"];
			var content="";
			$.each(device_list, function(index, entry){
				content += "<button id=\""+entry.SN+"\" class=\"component_device_btn\" onclick=\"toDetail(id)\">"+
    				"<h5>"+entry.device_name+"</h5>";
    				content += typeAcog(entry.device_type);
			});
			content+="<button id=\"switch1\" class=\"component_device_btn\" onclick=\"toDetail(id)\">"+
	    				"<h5>스위치 1</h5>"+
	    				"<img id=\"icon_switch\" class=\"dev_icon\" src=\"/static/imgs/switch.png\"/>"+
	    				"<p>상태 : <span>켜짐</span></p>"+
	    			"</button>"+
	    			"<button id=\"door_lock\" class=\"component_device_btn\" onclick=\"toDetail(id)\">"+
	    				"<h5>도어락 1</h5>"+
	    				"<img id=\"icon_doorlock\" class=\"dev_icon\" src=\"/static/imgs/doorlock.png\"/>"+
	    				"<p>상태 : <span>잠김</span></p>"+
	    				"<p>배터리 잔여량 : <span></span>%</p>"+
	    			"</button>"+
	    			"<button id=\"switch2\" class=\"component_device_btn\" onclick=\"toDetail(id)\">"+
	    				"<h5>스위치 2</h5>"+
	    				"<img id=\"icon_switch\" class=\"dev_icon\" src=\"/static/imgs/switch.png\"/>"+
	    				"<p>상태 : <span>꺼짐</span></p>"+
	    			"</button>";
	    			
			$("#div_devicelist").html(content);
			loaded = true;
		}
	});
});

function each_Update()
{
	$.each(device_list, function(index, entry){
		updateStatus(entry.SN);
	});
}
// 장치 상태 실시간 갱신
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
			$("#"+thisSN+">p>span.dev_status").html(stat);
			$("#"+thisSN+">p>span.dev_rem").html(amount);
		}
	});
}

$(function(){
	setInterval("each_Update()",1000);
});
