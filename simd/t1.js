function add(){
	let sum=0;
	for (let i = 0;i<10000;i++)
		sum+=Math.random()*10000;
	return sum;
}

add()
