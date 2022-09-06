import stripe

# Set key globally
stripe.api_key = "sk_test_51LdEfjSBknKnDeIZ28LWRgyhOwLFDK7v816NBHKjAXxkqlQWv9mxWgn1pzL1OEQZz56S70WOn1CKcvrrbyYlsVBN001pdcp2FC"


# Retriveing payment methods

methods = stripe.PaymentMethod.retrieve(
    "pm_1LdHhBSBknKnDeIZMTUtU9LT"
)

#print(methods)



# Create payment intent

#payment_intent = stripe.PaymentIntent.create(
#    amount=1000,
#    currency='usd',
#)

# payment_int = stripe.PaymentIntent.confirm(
#     'pi_3Lee74SBknKnDeIZ01F6MUOE',
#     payment_method='pm_card_visa)',
# )

# print(payment_int)

# print('\n\n')

# print(payment_int.status)


# Getting invoices from the customers

invoice = stripe.Invoice.list(limit=1).data[0]

lines = invoice.lines.list(limit=5) #to access nested service methods

print(lines)

