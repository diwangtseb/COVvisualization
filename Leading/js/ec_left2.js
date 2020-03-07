var ec_left2=echarts.init(document.getElementById("left2"),"dark")


var ec_left2_Option={
	title:{
		text:"确诊以及疑似新增趋势",
		textStyle:{
			//color:"white"
		},
		left:'left',
	},
	tooltip:{
		trigger:'axis',
		//指示器
		axisPointer:{
			type:'line',
			LineStyle:{
				color:'#7171C6'
			}
		},
	},
	legend:{
		 data: ['确诊新增', '疑似新增'],
		 left:'right',
	},
	//圆形位置
	grid:{
		left:'4%',
		right:'6%',
		bottom:'4%',
		top:'50',
		containLable:true
	},
	xAxis: [{
	        type: 'category',
	        data: ['01.20','01.21','01.22']
	}],
	yAxis: [{
		type: 'value',
		//y轴字体设置
		axisLabel:{
			show:true,
			color:'white',
			fontSize:12,
			formatter:function(value){
				if(value>=1000){
					value=value/1000+'k';
				}
				return value
			}
		},
		//y轴设置显示
		axisLine:{
			show:true
		},
		//与x轴平行的线样式
		splitLine:{
			show:true,
			LineStyle:{
				color:'#172738',
				width:1,
				type:'solid',
			}
		}
	}],
	 series: [
	        {
	            name: '确诊新增',
	            type: 'line',
	            smooth: true,
	            data: [120, 132, 101]
	        },
	        {
	            name: '疑似新增',
	            type: 'line',
	            smooth: true,
	            data: [1, 2, 3]
	        }
	    ]
}

ec_left2.setOption(ec_left2_Option)