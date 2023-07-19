document.addEventListener("DOMContentLoaded", ()=>{

    
  var credentials =[{
    username:"dev",
    password:'123',
    email:'dev234@gmail.com'
  },{
    username:"flatter",
    password:"@123",
    email:'flatter254@gmail.com'
  }];  
  

    
  document.querySelector("#signupform").onsubmit = function (){

    var newusername= document.querySelector ("#newusername-value").value;
    var newpassword=  document.querySelector ("#newpassword-value").value;
    var email= document.querySelector ("#email-value").value;
 
     console.log(newusername,newpassword ,email);
 
     var result=credentials.push({
       username:newusername,
       password:newpassword,
       email:email
     })
     
     alert( "Signup successful. You can now login with your new account.");
 
     document.querySelector ("#newusername-value").value ="";
     document.querySelector ("#newpassword-value").value= '';
     document.querySelector ("#email-value").value ="";
     
     return false ;
   }

  document.querySelector("form").onsubmit = function (){
  
     var username = document.querySelector("#username-value").value;
      var password = document.querySelector("#password-value").value;


      var matchcredentials =credentials.find((user) =>{
          return user.username === username && user.password === password;
      });
      
      if(matchcredentials){
      
        alert (`welcome ${matchcredentials.username}`);
      }else{
        alert('Invalid Username or Password')
      }

      username = document.querySelector("#username-value").value = "";
      password = document.querySelector("#password-value").value ="";


    return false;
  }

  
  

});
