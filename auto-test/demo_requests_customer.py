import stripe

# Set key globally
stripe.api_key = "sk_test_51LdEfjSBknKnDeIZ28LWRgyhOwLFDK7v816NBHKjAXxkqlQWv9mxWgn1pzL1OEQZz56S70WOn1CKcvrrbyYlsVBN001pdcp2FC"


# Create a customer

#customer = stripe.Customer.create(
#    email='jobs.korn@example.com',
#    name='Jobs Korn',
#    tax_exempt='reverse',
#    payment_method='pm_card_visa',
#    invoice_settings={
#        'default_payment_method': 'pm_card_visa',
#    },
#    preferred_locales=['en', 'es'],
#)

#customer_id = 'cus_MMAXOBWsfvWknd'


# Updating customer details (email address)

#cus = stripe.Customer.modify(
#    customer_id,
#    email='jobsk@example.com'
#)

#cus = stripe.Customer.retrieve(customer_id)

#customers = stripe.Customer.list(
#    email='jenny.rosen@example.com'
#)

#print([cus.id for cus in customers.data])


# Delete a customer

#customer = stripe.Customer.delete(
#    'cus_MMAXOBWsfvWknd'
#)



