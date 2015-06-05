import webapp2

form =""""
  <form action="https://books.zoho.com/api/v3/creditnotes?authtoken=2348335af716e16930d15a86b353cc59&organization_id=52487858" method="post" id="creditnote">
   				    <lable>customer_id</lable>
					<input type="text" name="customer_id" value="">
					</br>
					<lable>vat_treatment</lable>
					<input type="text" name="vat_treatment" value="">
					</br>
					<lable>pricebook_id</lable>
					<input type="text" name="pricebook_id" value="">
					</br>
					<lable>contact_persons</lable>
					<input type="text" name="contact_persons" value="">
					</br>
					<lable>salesorder_number</lable>
					<input type="text" name="salesorder_number" value="">
					</br>
					<lable>reference_number</lable>
					<input type="text" name="reference_number" value="">
					</br>
					<lable>template_id</lable>
					<input type="text" name="template_id" value="">
					</br>
					<lable>date</lable>
					<input type="text" name="date" value="">
					</br>
					<lable>is_update_customer</lable>
					<input type="text" name="is_update_customer" value="">
					</br>
					<lable>shipment_date</lable>
					<input type="text" name="shipment_date" value="">
					</br>
					<lable>discount</lable>
					<input type="text" name="discount" value="">
					</br>
					<lable>exchange_rate</lable>
					<input type="text" name="exchange_rate" value="">
					</br>
					<lable>salesperson_name</lable>
					<input type="text" name="salesperson_name" value="">
					</br>
					<lable>custom_fields</lable>
					<input type="text" name="custom_fields" value="">
					</br>
					<input type="submit" >
        </form>
        
<script type="text/javascript">
      var form = document.getElementById("creditnote");
      form.onsubmit = function (e) 
      {
              e.preventDefault();
              var data = {};
              for (var i = 0, ii = form.length; i < ii; ++i) 
              {
                      var input = form[i];
                      if (input.name) 
                      {
                              data[input.name] = input.value;
                              
                      }
              }
              // construct an HTTP request
              var xhr = new XMLHttpRequest();
              xhr.open(form.method, form.action, true);
              xhr.setRequestHeader("Content-type","application/x-www-form-urlencoded");
              var dataToServer = JSON.stringify(data);

              xhr.send("JSONString="+dataToServer);
              alert (dataToServer);
      };
    </script>
 """
class MainPage(webapp2.RequestHandler):
    
    def get(self):
        self.response.out.write(form)
        
    def post(self):
        self.response.write(" thank you")
        
app = webapp2.WSGIApplication([('/', MainPage)], debug=True)
