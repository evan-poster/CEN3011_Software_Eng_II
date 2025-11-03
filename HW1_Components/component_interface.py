from abc import ABC, abstractmethod


class MessageHandler(ABC):
    """Abstract base class defining the interface for message handling components."""
    
    @abstractmethod
    def process_message(self, message: str) -> str:
        """
        Process a message and return the result.
        
        Args:
            message: The message to process
            
        Returns:
            The processed message
        """
        pass