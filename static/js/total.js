function total()
{
    var test = parseInt(document.getElementById("test").innerHTML);
    var AF = parseInt(document.getElementById("AF").value);
    console.log(test,AF)

    var total = test + AF

    document.getElementById('p-total').style.display='block'
    document.getElementById('total').innerHTML = total
}