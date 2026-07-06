def shutdown():
    choice = input ("Do you want to shutdown (Yes/No)?")

    if choice == "Yes":
        print("Shuttingdown")
    
    elif choice == "No":
        print("Abort shutdown")

    else:
        print("Sorry")
shutdown()