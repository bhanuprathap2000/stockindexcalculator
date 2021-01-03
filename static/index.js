function form_validator()
{

    


    var indexname=document.querySelectorAll("#indexname")[0].value;
    var spotvalue=Number(document.querySelectorAll("#spot")[0].value);
    var expiry=Number(document.querySelectorAll("#expiry")[0].value);
    console.log(indexname);
    console.log(spotvalue);
    console.log(typeof(spotvalue));
    console.log(expiry);
    console.log(typeof(expiry));
    
    if (indexname=="nifty" || indexname=="banknifty")
    { 
        document.querySelectorAll("#indexwarning")[0].innerHTML="";

        if(spotvalue>0 && spotvalue!=="")
        {
            document.querySelectorAll("#spotwarning")[0].innerHTML="";
         if(expiry>0 && spotvalue!=="")
         {    document.querySelectorAll("#expirywarning")[0].innerHTML="";
             return true;

         }
         else{
            document.querySelectorAll("#expirywarning")[0].innerHTML="Please enter a valid input greater than zero.";
            return false;

         }


        }
        else{
            document.querySelectorAll("#spotwarning")[0].innerHTML="Please enter a valid input greater than zero.";
            return false;
        }
        
     
    }
    else
    {

    document.querySelectorAll("#indexwarning")[0].innerHTML="Please enter a valid input out of nifty and banknifty";
    document.querySelectorAll("#spotwarning")[0].innerHTML="";
    document.querySelectorAll("#expirywarning")[0].innerHTML="";
     return false   
 }

    
}

