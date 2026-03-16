function processPayment(){

let name=document.getElementById("name").value;
let card=document.getElementById("card").value;
let amount=document.getElementById("amount").value;

if(name=="" || card=="" || amount=="")
{
alert("Please fill all fields");
return;
}

let txn="TXN"+Math.floor(Math.random()*100000);

alert("Payment Successful\nTransaction ID: "+txn);

}