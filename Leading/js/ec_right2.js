var ec_right2 = echarts.init(document.getElementById('right2'),"dark");
var ddd=[{"name":"肺炎",'value':"123"},{"name":"新肺炎",'value':"456"}]


var ec_right2_option={
	title:{
		text:"今日疫情热搜",
		textStyle:{
			color:"white",
		},
		left:"left"
	},
	tooltip:{
		show:false
	},	
    series: [{
        type: 'wordCloud',
		gridSize:1,
		sizeRange:[12,55],
		ratationRange:[-45,0,45,90],
		data:[],
		textStyle: {
		    normal: {
		        // Color can be a callback function or a color string
		        color: function () {
		            // Random color
		            return 'rgb(' + [
		                Math.round(Math.random() * 255),
		                Math.round(Math.random() * 255),
		                Math.round(Math.random() * 255)
		            ].join(',') + ')';
		        }
		    } 
		},
        right: null,
        bottom: null
    }]
};

ec_right2.setOption(ec_right2_option)