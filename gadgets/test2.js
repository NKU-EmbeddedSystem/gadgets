car = {};

function init(car) {
    for (var i = 0; i < 0x123; i++) {
        car[(i).toString() + "car"] ^= 0x2345;
    }
}

function run(a, i) {
    // console.log(a[Math.ceil(Math.random() * 0x123455)]); 会被编译器优化
    console.log(a[(0x1234).toString() + "car"]);
}

init(car);

for (var i = 0; i < 0x1234; i++)
    run(car);
