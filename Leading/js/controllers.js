		function gettime(){
			$.ajax({
				url:"/time",
			timeout:10000,
			success:function(data){
				$('#time').html(data)
			},
			err:function(){
				
			}
			});
		}
		function get_mid1_data(){
			$.ajax({
				url:"/mid1",
			success:function(data){
				$(".num h1").eq(0).text(data.confirm);
				$('.num h1').eq(1).text(data.suspect);
				$('.num h1').eq(2).text(data.heal);
				$('.num h1').eq(3).text(data.dead);
			},
			err:function(){
				
			}
			})
		}
		function get_mid2_data() {
			$.ajax({
				url:"/mid2",
				success:function(data){
					ec_center_opention.series[0].data=data.data
					ec_center.setOption(ec_center_opention)
				}
			})
		}

		function get_left1_data() {
			$.ajax({
				url:"/left1",
				success:function(data){
					ec_left1_Option.xAxis[0].data=data.day
					ec_left1_Option.series[0].data=data.confirm
					ec_left1_Option.series[1].data=data.suspect
					ec_left1_Option.series[2].data=data.heal
					ec_left1_Option.series[3].data=data.dead					
					ec_left1.setOption(ec_left1_Option)
				}
			})
		}
		
		function get_left2_data() {
			$.ajax({
				url:"/left2",
				success:function(data){
					ec_left2_Option.xAxis[0].data=data.day
					ec_left2_Option.series[0].data=data.confirm_add
					ec_left2_Option.series[1].data=data.suspect_add				
					ec_left2.setOption(ec_left2_Option)
				}
			})
		}
		
		function get_right1_data() {
			$.ajax({
				url:"/right1",
				success:function(data){
					ec_right1_option.xAxis[0].data=data.city
					ec_right1_option.series[0].data=data.confirm
					ec_right1.setOption(ec_right1_option)
				}
			})
		}
		
		function get_right2_data() {
			$.ajax({
				url:"/right2",
				success:function(data){
					ec_right2_option.series[0].data=data.kws
					ec_right2.setOption(ec_right2_option)
				}
			})
		}
		
		get_mid1_data()
		get_mid2_data()
		get_left1_data()
		get_left2_data()
		get_right1_data()
		get_right2_data()
		gettime()
		//setInterval(get_mid2_data)
		//setInterval(gettime)
		//setInterval(get_mid1_data,1000)
