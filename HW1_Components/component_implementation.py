from component_interface import MessageHandler


class SimpleMessageHandler(MessageHandler):
    """Concrete implementation of the MessageHandler interface."""
    
    def process_message(self, message: str) -> str:
        """
        Process a message by converting it to uppercase and adding a prefix.
        
        Args:
            message: The message to process
            
        Returns:
            The processed message with prefix and uppercase conversion
        """
        return f"PROCESSED: {message.upper()}"