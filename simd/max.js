var m1 = [[0.1, 0.2, 0.3], [0.4, 0.5, 0.6], [0.7, 0.8, 0.9]]
var m2 = [[1, 1.1, 1.2], [1.3, 1.4, 1.5], [1.6, 1.7, 1.8]]

function matrixMul(a,b){
	var c=new Array(a.length);
	for(var i=0;i<a.length;i++)
	{
		c[i]=new Array(b[0].length);
		for(var j=0;j<b[0].length;j++)
		{
			c[i][j]=0;
			for(var k=0;k<b.length;k++)
			{
				c[i][j] = Math.max(c[i][j], a[i][k]*b[k][j]);
			}
		}
	}
	return c;
}

for(var i = 0; i < 10000; i++)
{
	matrixMul(m1, m2);
}
