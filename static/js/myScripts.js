    function pConvert(){
var p=1*document.getElementById("pounds").value;
var k=p*0.453592; 
k=Math.round(k*1000)/1000;
document.getElementById("kilograms").value=k;
                    }
    

    function kConvert(){
var k=1*document.getElementById("kilograms").value;
var p=k*2.20462; 
p=Math.round(p*1000)/1000;
document.getElementById("pounds").value=p;
                    }

// enter conversion ratio and entered value and id to write to.
function convertAnyThing(r, v, t){
var inValue=1*v;
var outValue=inValue*r; 
outValue=Math.round(outValue*1000)/1000;
document.getElementById(t).value=outValue;
}
                 