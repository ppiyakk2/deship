////////////////////////////////////////////////////////////

// 회원 등록 - 정보 전송
function register()
{
			var id = $("#register_userid").val();
			var username = $("#register_username").val();
			var password = $("#register_password").val();
			var phone = $("#register_phone").val();
			var address = $("#register_address_L").val();
			address += " ";
			address += $("#register_address").val();
			
			$.ajax({
				type : 'POST',
				url : "/users/signup",
				dataType : 'json',
				data :
				{
						"ID" : id,
						"user_name" : username,
						"passwd" : password,
						"phone" : phone,
						"address" : address
				},
				success: function(result){
					location.reload();
				},
				statusCode:{
					200:function(){
						alert("등록이 완료되었습니다.");
						window.location.replace("http://211.198.65.241:38080/");
					},
					400:function(){
						alert("이미 존재하는 ID입니다.");
					},
					403: function() {
						alert("없는 아이디이거나, 패스워드가 틀렸습니다.");
					},
					404: function() {
						alert("Not Found.");
					}
				}
			});
			//window.location.replace("http://211.198.65.241:38080/");
}

// 로그인 정보 전송 함수
function signin()
{
	/////////// 서버와 연동 필요 //////////////////////
	var id = $("#login_id").val();
	var pw = $("#login_password").val();

	$.ajax({
		type:"POST",
		url:"/users/signin",
		data:{"ID": id, "passwd": pw},
		statusCode:{
					200:function(){
						window.location.replace("http://211.198.65.241:38080/main");
					},
					400: function() {
						alert("사용자 계정이나 암호가 일치하지 않습니다.");
					}
				}
	});
	
	/**/
}