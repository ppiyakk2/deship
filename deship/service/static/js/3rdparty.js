// 샘플 데이터 - 요청 목록
var sample_reqList = {"request_list":[{
	"SN":"1224",
	"device_name":"좋은 세탁기",
	"user_name":"김태경",
	"reqtime":"2016-06-12 16:01",
	"address":"경희대학교 우정원 2570호",
	"item":"퍼실 컬러 드럼전용 2.7L",
	"amount":1,
	"msg":"세제 자동구매",
	"status":"ongoing",
	"reg_date":"2016-05-29"
}, {
	"SN":"1225",
	"device_name":"안좋은 세탁기",
	"user_name":"김태경",
	"reqtime":"2016-06-12 15:55",
	"address":"경희대학교 우정원 2570호",
	"item":"아토세이프 드럼전용 2.5L",
	"amount":1,
	"msg":"세제 자동구매",
	"status":"complete",
	"reg_date":"2016-05-29"
}]
};

// 샘플 데이터 - 요청 상세정보
var sample_request = {
	"request":{
	"SN":"1224",
	"device_name":"좋은 세탁기",
	"user_name":"김태경",
	"reqtime":"2016-06-12 16:01",
	"address":"경희대학교 우정원 2570호",
	"item":"퍼실 컬러 드럼전용 2.7L",
	"amount":1,
	"msg":"세제 자동구매",
	"status":"ongoing",
	"reg_date":"2016-05-29"}
};

//샘플 데이터 - 소모품 목록
var sample_itemlist = {
	"item_list" : [{
		"item_id" : "item1",
		"item_name":"퍼실 컬러 드럼전용 2.7L",
		"item_price":"19800",
		"amount":57
	},{
		"item_id" : "item2",
		"item_name":"아토세이프 드럼전용 2.5L",
		"item_price":"22800",
		"amount":33
	},
]};

// 요청 목록 조회
function update_reqList(){
	var content_ongoing="<tr><th>요청 내용</th><th>주소</th><th>요청 시간</th><th>상세정보</th></tr>";
	var content_complete="<tr><th>요청 내용</th><th>주소</th><th>요청 시간</th><th>상세정보</th></tr>";
	var URLis="/transaction";
	$.ajax({
		type:"GET",
		url:URLis,
		dataType:"json",
		success:function(data){
			var reqlist = data["transactiondata"];
			$.each(reqlist, function(index, entry){
				if(!entry.request_done){
					content_ongoing = add_ongoing(entry, content_ongoing);
				}
				else{
					content_complete = add_complete(entry, content_complete);
				}
			});
			$("#table_request_ongoing").html(content_ongoing);
			$("#table_request_complete").html(content_complete);
		}
	});

};

// 진행중인 요청 목록에 추가
function add_ongoing(entry, content){
	content += "<tr>"+
    				"<td class=\"req_msg\">세제 구매</td>"+
    				"<td class=\"req_address\">"+entry.address +"</td>"+
    				"<td class=\"req_reqtime\">"+ entry.request_tx +"</td>"+
    				"<td>"+
    					"<button id=\"btn_"+entry.device_id+"\" value=\""+entry.device_id+"\" class=\"btn_ang\""+
						"data-toggle=\"modal\" data-target=\"#modal_detail\" onclick=\"detailOf('"+entry.tx_id+"', '진행중')\">보기</button>"+
					"</td></tr>";
	return content;
}
// 완료된 요청 목록에 추가
function add_complete(entry, content){
	content += "<tr>"+
    				"<td class=\"req_msg\">세제 구매</td>"+
    				"<td class=\"req_address\">"+entry.address+"</td>"+
    				"<td class=\"req_reqtime\">"+entry.request_tx+"</td>"+
    				"<td>"+
    					"<button id=\"btn_"+entry.device_id+"\" value=\""+entry.device_id+"\" class=\"btn_ang\""+
						"data-toggle=\"modal\" data-target=\"#modal_detail\" onclick=\"detailOf('"+entry.tx_id+"', '완료')\">보기</button>"+
					"</td></tr>";
	return content;
}


// 완료 요청
function done(tx_id){
	var URLis = '/transaction/' + tx_id + "/done";
	$.ajax({
		type:"GET",
		url:URLis,
		dataType:"json",
		success:function(data){
		}
	});
}

// 요청 상세정보 획득
function detailOf(value, r){
	var URLis="/transaction/"+value;
	$.ajax({
		type:"GET",
		url:URLis,
		dataType:"json",
		success:function(data){
			var reqinfo = data["transaction"];
			$("#img_device").attr("src","/static/imgs/wahsing_machine_pic.png");
			$("#req_SN").html(reqinfo.device_sn);
			$("#req_user_name").html(reqinfo.user_name);
			$("#req_device_name").html(reqinfo.device_name);
			$("#req_msg").html("세제 구매");
			$("#req_item").html(reqinfo.item_name+"/1");
			$("#req_address").html(reqinfo.address);
			$("#req_reqtime").html(reqinfo.request_time);
			$("#req_status").html(r);
			$("#done_button").html("<button type='button' class='btn_ang' data-dismiss='modal' onclick=done('"+reqinfo.tx_id+"')\>완료</button>");
		}
	});
}

// 소모품 목록 조회
$(function(){
	var URLis="/consumable";
	var content = "";
	$.ajax({
		type:"GET",
		url:URLis,
		dataType:"json",
		success:function(data){
			var itemlist = data["consumable"];
			$.each(itemlist, function(index, entry){
				content += "<div class=\"div_item\">"+
	    			"<img src=\"/consumable/"+entry.item_id+"/image\" class=\"img_items\"/>"+
	    			"<span>"+
	    				"<h5 class=\"item_name\">"+entry.name+"</h5>"+
	    				"<h6>판매가 <span class=\"item_price\">"+entry.price+"</span> 원</h6>"+
	    			"</span></div>";
			});
			$("#container_item>div").html(content);
		}
	});
	
	// 샘플코드
	/*var itemlist = sample_itemlist["item_list"];
	$.each(itemlist, function(index, entry){
		content += "<div class=\"div_item\">"+
			"<img src=\"/static/imgs/"+entry.item_id+".png\" class=\"img_items\"/>"+
			"<span>"+
				"<h5 class=\"item_name\">"+entry.item_name+"</h5>"+
				"<h6>판매가 <span class=\"item_price\">"+entry.item_price+"</span> 원</h6>"+
				"<p>보유 수량 : <span class=\"item_amount\">"+entry.amount+"</span> 개</p>"+
			"</span></div>";
	});
	$("#container_item>div").html(content);*/
});

// 1초 주기로 요청 목록을 갱신
$(function(){
	setInterval("update_reqList()", 1000);
});