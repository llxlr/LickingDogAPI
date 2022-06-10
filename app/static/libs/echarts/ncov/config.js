$.ajax({
    type: 'GET',
	url: '/v1/ncov/?name=china',
	dataType: 'json',
	success: function(res) {
		let data = res.data;
		let dom = document.getElementById("cnmap");
        let myChart = echarts.init(dom, null, {renderer: 'svg'});
		document.getElementById("cn1").innerHTML=data["currentConfirmed"];
        document.getElementById("cn2").innerHTML=data["overseas"];
        document.getElementById("cn3").innerHTML=data["dead"];
        document.getElementById("cn4").innerHTML=data["cured"];
        const cnoption = {
            bottom: '10px',
            tooltip: {
                show: true,
                trigger: 'item'
            },
            dataRange: {
                x: 'center',
                orient: 'horizontal',
                min: 0,
                max: 20000,
                text: ['高', '低'], // 文本，默认为数值文本
                splitNumber: 0,
                splitList: [
                    {start: 1000, end: 99999},
                    {start: 100, end: 1000},
                    {start: 50, end: 100}, {start: 10, end: 50},
                    {start: 1, end: 10},
                    {start: 0, end: 0},
                ],
                inRange: {
                    color: ['#fff', '#fff5c9', '#FDEBCF', '#F59E83', '#F59E83', '#CB2A2F', '#e6ac53', '#70161D']
                }
            },
            series: [{
                label: {
                    normal: {
                        fontFamily: 'Microsoft YaHei',
                        fontSize: 9,
                        show: true,
                    },
                    emphasis: {
                        show: false
                    }
                },
                name: '现存确诊',
                type: 'map',
                mapType: 'china',
                zoom: 1,
                itemStyle: {
                    normal: {
                        borderWidth: .5,//区域边框宽度
                        borderColor: '#B6B6B6',//区域边框颜色
                        areaColor: "#ffefd5",//区域颜色
                    },
                },
                data: data["details"],
                },
            ],
            animation: false,
        };
        myChart.setOption(cnoption, true);
	},
});

$.ajax({
    type: 'GET',
	url: '/v1/ncov/?name=world',
	dataType: 'json',
	success: function(res) {
        let data = res.data;
        let worldmapdom = document.getElementById("worldmap");
        let worldChart = echarts.init(worldmapdom, null, {renderer: 'svg'});
        document.getElementById("wd1").innerHTML=data["currentConfirmed"];
        document.getElementById("wd2").innerHTML=data["Confirmed"];
        document.getElementById("wd3").innerHTML=data["dead"];
        const worldoption = {
            bottom: '10px',
            tooltip: {
                show: true,
                trigger: 'item',
                formatter: function (val) {
                    return val.data.provinceName + '<br>' + '现存确诊: ' + val.data.value
                }
            },
            dataRange: {
                x: 'center',
                orient: 'horizontal',
                min: 0,
                max: 20000,
                text: ['高', '低'], // 文本，默认为数值文本
                splitNumber: 0,
                splitList: [
                    {start: 10000, end: 999999},
                    {start: 1000, end: 10000},
                    {start: 99, end: 999},
                    {start: 10, end: 99},
                    {start: 0, end: 9},
                ],
                inRange: {
                    color: ['#FAEBD2', '#D56355', '#BB3937','#CB2A2F', '#772526']
                }
            },
            series: [{
                label: {
                    normal: {
                        fontFamily: 'Microsoft YaHei',
                        fontSize: 9,
                        show: false
                    },
                    emphasis: {
                        show: false
                    }
                },
                name: '现存确诊',
                type: 'map',
                mapType: 'world',
                zoom: 0.8,
                itemStyle: {
                    normal: {label: {show: true, color: '#333'}, borderWidth: 0},
                },
                data: data["details"],
                },
            ],
            animation: false,
        };
        worldChart.setOption(worldoption, true);
        worldChart.resize();
    }
});


cnmap = document.getElementById("cnmap");
worldmap = document.getElementById("worldmap");
cninfo = document.getElementById("cninfo");
worldinfo = document.getElementById("worldinfo");
btncn = document.getElementById('btn-cn');
btnworld = document.getElementById('btn-world');

cnmap.style.display = 'block';
worldmap.style.display = 'none';
cninfo.style.display = 'flex';
worldinfo.style.display = 'none';
btncn.className = 'button btn-active';
btnworld.className = 'button';


function showcn(e) {
    cnmap.style.display = 'block';
    worldmap.style.display = 'none';
    cninfo.style.display = 'flex';
    worldinfo.style.display = 'none';
    btncn.className = 'button btn-active';
    btnworld.className = 'button';
}

function showworld(e) {
    worldmap.style.display = 'block';
    cnmap.style.display = 'none';
    cninfo.style.display = 'none';
    worldinfo.style.display = 'flex';
    btncn.className = 'button';
    btnworld.className = 'button btn-active';
}