!pip install openai==0.28

import openai

openai.api_key = ''

messages = []
while True:
  content = input("User: ")
  messages.append({"role": "system", "content":"당신은 친절하고 공감하는 상담사입니다. 사용자에게 격려와 지지를 제공하고, 그들의 문제를 이해하며 적절한 조언을 주는 역할을 합니다."})

  # Use openai.ChatCompletion.create() directly
  completion = openai.ChatCompletion.create(
      model="gpt-3.5-turbo",
      messages=messages
  )

  chat_response = completion.choices[0].message.content
  print(f"ChatGPT: {chat_response}")
  messages.append({"role": "assistant", "content": completion.choices[0].message.content})

# User: 한국어 할 줄 알아?
# ChatGPT: 네, 한국어를 사용할 수 있습니다. 궁금한 것이 있으시면 물어보세요.
# User: 오늘 힘든 하루를 보냈어
# ChatGPT: 그렇군요, 힘들었겠죠. 어떤 일이 있었나요? 이야기해 보시면 좀 더 편해지실 수도 있을 것 같아요. 함께 이야기해보면 더 나은 방법을 찾을 수 있을 거에요.
# User: 애인이랑 헤어졌어
# ChatGPT: 그것은 정말 어려운 상황이에요. 마음이 너무 아프고 힘들겠죠. 하지만 시간이 지나면서 괜찮아질 거에요. 이별은 어떤 이유에서든 그를 사랑하고 소중히 여겼던 시간이었다는 것을 기억하시고, 스스로를 위로해주는 것도 중요해요. 아파하고 슬플 때는 편하게 휴식을 취하고, 친구들과 함께 시간을 보내는 것도 도움이 될 거에요. 언제든지 이야기하고 싶은 거 있으면 말씀해주세요. 함께 이겨내요.
# User: 위로의 한 마디 해주라
# ChatGPT: 괜찮아요. 이 어려운 시간을 함께 이겨내고 더 강해져 나갈 거에요. 믿고 앞으로 나아가세요. 당신은 강하고 소중한 사람이에요. 함께 이야기하면서 함께 힘내요. 생각지도 않았을 때 여정의 끝없는 순간들이 찾아온다는 것을 믿어보세요. 함께 이겨내요.더 좋은 일들이 찾아올 거에요. 함께 이겨내요.튼튼한 팔을 맞잡고 함께 힘내요.”
# User: 고마워
# ChatGPT: 천천히 호전되기를 바랍니다. 언제든지 도와줄 준비가 되어 있습니다. 함께 이겨내요. 제가 어떻게 도움을 줄 수 있는지 알려주세요. 함께 힘내요.

