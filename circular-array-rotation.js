function main() {
    var n_temp = readLine().split(' ');
    var n = parseInt(n_temp[0]);
    var k = parseInt(n_temp[1]);
    var q = parseInt(n_temp[2]);
    a = readLine().split(' ');
    a = a.map(Number);
    
    k = k%n;
    for(var a0 = 0; a0 < q; a0++){
        var m = parseInt(readLine());
        var index = m-k;
        if (index < 0) index += n;
        console.log(a[index]);
    }

}