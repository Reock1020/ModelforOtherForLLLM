from arch.llm import LLM

llm = LLM()
def generate_message(setting, **params_data):
  message = ""

  for param in setting["params"]:
    # パラメータに対応するデータが引数に与えられてない
    if not param["name"] in params_data["params_data"]: 
      continue
    message += "###  " + param["description"] + "  \n"

    for data in params_data["params_data"][param["name"]]:
      message += f"- {data}\n"

  return message

def call_llm(docstring, log, **params_data):
    setting = docstring

    message = generate_message(setting, **params_data)

    log.append(
      {"role": "user", "content": message}
    )

    print("# 目的  \n {}".format(setting["short_description"]))
    print("## 入力  \n", message)

    while True:
      result = llm.call(
        prompt=setting["prompt"],
        context=log,
        format=setting["output_format"]
      )

      if result["success"]:
        break

      print("Failed call")

    log.append(
      {"role": "assistant", "content": result["text"]}
    )

    print("## 出力  \n", result["text"])

    return result["output"], log