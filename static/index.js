function form_validator()
{


    var indexname=document.querySelectorAll("#indexname")[0].value
    
    if (indexname=="nifty" || indexname=="banknifty")
    {
        console.log(indexname);
     return true
    }
    else
    {

    document.querySelectorAll("#indexwarning")[0].innerHTML="Please enter a valid input out of nifty and banknifty";
     return false   
 }

    
}
