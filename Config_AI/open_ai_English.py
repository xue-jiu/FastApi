import openai


class English_Open_AI():
    def __init__(self, prompt):
        self.response = self.get_response(prompt)
    
    def get_response(self, prompt):
        # 设置你的 API 密钥
        # 调用 OpenAI 的 API
        response = "hello,fastapi"
        return response
