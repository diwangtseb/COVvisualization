var ec_right1=echarts.init(document.getElementById("right1"),"dark");


var ec_right1_option={
	//标题样式
	title:{
		text:"非湖北地区城市确诊top5",
		textStyle:{
			color:"white",
		},
		left:"left"
	},
	color:["#3398DB"],
	tooltip:{
		trigger:'axis',
		axisPointer:{
			type:'shadow'
		}
	},
	xAxis:[{
		type:'category',
		data:[]
	}],
	yAxis:{
		type:'value'
	},
	series:[{
		data:[],
		type:'bar',
		barMaxWidth:"50%"
	}]
};
ec_right1.setOption(ec_right1_option)