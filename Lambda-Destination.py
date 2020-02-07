def lambda_handler(event, context):
    #this will print the payload from the source function
    print(event)
    return "Thanks"
