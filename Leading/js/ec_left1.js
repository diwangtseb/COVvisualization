var ec_left1=echarts.init(document.getElementById("left1"),"dark");


var ec_left1_Option={
	title:{
		text:"全国累计趋势",
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
		 data: ['累计确诊', '现有疑似', '累计治愈', '累计死亡'],
		 left:'right',
	},
	//圆形位置
	grid:{
		left:'4%',
		right:'6%',
		bottom:'4%',
		top:'30',
		containLable:true
	},
	xAxis: [{
	        type: 'category',
	        data: []
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
	            name: '累计确诊',
	            type: 'line',
	            smooth: true,
	            data: []
	        },
	        {
	            name: '现有疑似',
	            type: 'line',
	            smooth: true,
	            data: []
	        },
	        {
	            name: '累计治愈',
	            type: 'line',
	            smooth: true,
	            data: []
	        },
	        {
	            name: '累计死亡',
	            type: 'line',
	            smooth: true,
	            data: []
	        }
	    ]
}

ec_left1.setOption(ec_left1_Option)