 function AddToCart(product_id){

    if (window.XMLHttpRequest){
      // code for IE7+, Firefox, Chrome, Opera, Safari
      xmlhttp=new XMLHttpRequest();
    } else {  // code for IE6, IE5
      xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");
    }

    xmlhttp.onreadystatechange=function() {
      if (this.readyState==4 && this.status==200) {
      var data = JSON.parse(this.responseText);
      console.log(data);
      if (data.status == 'OK'){
        var a = document.getElementById('addtocart_'+product_id)
        a.style.backgroundColor = 'red';
        alert('Tovar savatchaga qo\'shildi !')
      }
      else{
        document.getElementById('addtocart_'+product_id).disabled=false;
        alert('Tovar savatchaga qo\'shilgan !')

      }                   
      }
    }

    var url = "{% url 'shop:cart' %}";
    var url = url+"?data="+product_id;

    xmlhttp.open("GET",url,true);
    xmlhttp.send();
  }

   function DeleteItem(product_id){

    if (window.XMLHttpRequest){
      // code for IE7+, Firefox, Chrome, Opera, Safari
      xmlhttp=new XMLHttpRequest();
    } else {  // code for IE6, IE5
      xmlhttp=new ActiveXObject("Microsoft.XMLHTTP");
    }

    xmlhttp.onreadystatechange=function() {
      if (this.readyState==4 && this.status==200) {
      var data = JSON.parse(this.responseText);
      console.log(data);
      if(data.ok == 200){
       var d =  document.getElementById('product_row_'+product_id).style = 'display:none;';
       document.getElementById('cart_total').innerHTML = 'Jami summa : '+data.cart_total_price;
       console.log(d)
      }
                 
      }
    }

    var url = "{% url 'shop:cart_delete_item' %}";
    var url = url+"?data="+product_id;

    xmlhttp.open("GET",url,true);
    xmlhttp.send();
  }

