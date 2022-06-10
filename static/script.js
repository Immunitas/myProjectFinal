localStorage.setItem("myProject", "Ziva")

function Timer() {
    var dt=new Date()
    document.getElementById("horloge").innerHTML=dt.getHours()+":"+dt.getMinutes()+":"+dt.getSeconds();
    setTimeout("Timer()",900);
      console.log("Exécution de Timer()");
    
}
Timer();

 