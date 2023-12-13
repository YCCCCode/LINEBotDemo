"""
    openai助手模塊
    https://platform.openai.com/docs/guides/speech-to-text api範例
"""
import openai
import configparser

# 設置API密鑰
config = configparser.ConfigParser()
config.read("./config.ini")
openai.api_key = "配置OpenAi的金鑰"


class Get_openAI:
    @staticmethod
    def post(text):
        print("進入openai")
        conversation = [
            {
                "role": "system",
                "content": "1.角色：心理諮商師2.提供：人際焦慮、情緒管理、壓力、和其他心理健康問題的指導3.方法：認知行為療法、冥想技巧 目標：管理憂鬱症狀4.風格：簡潔且口語，可以加上語助詞5.字數限制：70字以內",
            },
            {"role": "user", "content": text},
        ]
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=conversation,
                max_tokens=150,
                temperature=0.2,
            )
            print(response)
            data = response["choices"][0]["message"]["content"]
            print(data)
            return data
        except Exception as e:
            print(e)
            return e
