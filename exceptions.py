# Custom exceptions generated by the app


class NotCorrectMessage(Exception):
    """Invalid bot message that could not be parsed"""
    pass


class NotCorrectExpenseIDToDelete(Exception):
    """Invalid expense id in /del<id> command"""
