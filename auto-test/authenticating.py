import stripe

# Set key globally
stripe.api_key = "sk_test_51LdEfjSBknKnDeIZ28LWRgyhOwLFDK7v816NBHKjAXxkqlQWv9mxWgn1pzL1OEQZz56S70WOn1CKcvrrbyYlsVBN001pdcp2FC"


#stripe.Customer.create(
#  email="jenny.rosen@example.com",
#  payment_method="pm_card_visa",
#  invoice_settings={"default_payment_method": "pm_card_visa"},
#)

# print(stripe.Customer.retrieve('cus_MLzMVchaDReF7X'))

account_id = 'acct_1LdEfjSBknKnDeIZ'


#print(stripe.Customer.list(stripe_account=account_id))

#print('/n/n')

customer_list = stripe.Customer.list(stripe_account=account_id)

for customer in customer_list:
  for objects in customer:
    if objects=='name':
      print(objects + ': ' + customer['name'])

print(customer_list)
print('\n\n')

