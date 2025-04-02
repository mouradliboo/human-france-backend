from rest_framework.exceptions import APIException

class AgentNotWorkingException(APIException):
    status_code = 400
    default_detail = "The agent is not in work status."
    default_code = 'agent_not_working'
    
    def __init__(self, detail=None):
        if detail is None:
            detail = self.default_detail
        self.detail = {"error": detail}

