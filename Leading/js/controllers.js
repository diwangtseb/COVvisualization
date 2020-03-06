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
		get_mid1_data()
		get_mid2_data()
		gettime()
		//setInterval(get_mid2_data)
		//setInterval(gettime)
		//setInterval(get_mid1_data,1000)
