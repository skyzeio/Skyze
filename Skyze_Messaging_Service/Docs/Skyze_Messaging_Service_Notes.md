# Skyze Messaging Service Notes

## Adding a new message
### Messaging code
1. **Add the message type**
  2. in `Skzye_Messaging_Serivce/Messages/SkyzeMessageTypes.py` add the message type to the `SkyzeMessageType` enum
  3. use all caps and _ to separate words
  4. one message type per line
5. **Create the Message object**
  6. in the folder `Skzye_Messaging_Serivce/Messages/` select a message module that is similar to the one you want to create and save it as the new message type
  7. Rename the class name
  8. Change the message type in the Constructor
  9. Change the data it carries
10. **Route the message**
  11. in the `SkyzeMessageBusService.py` module
    12. add the message routing to the `__route_message` function
    13. import the message
14. **Receive the message**
  15. in the services classes that are interested in receiving the message
    16. import the message
    17. add the message to the `receiveMessage` function which routes the message to the appropriate internal function
18. **Send the message**
  19. in the services classes that are interested in sending the message
    20. import the message
    21. add the sender to the appropriate functions using `self._sendMessage(message)`

### Testing the message
#### Unit Testing

#### Integration Testing
