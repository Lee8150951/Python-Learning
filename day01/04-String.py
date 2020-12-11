# 字符串
message = "hello world"
# .title每个单词首字母大写
print(message.title())
# .upper所有字母大写，.lower所有字母小写
print(message.upper())
print(message.lower())
# 通过f"{}{}"进行字符串拼接，使用形式类似于vue.js中的{{}}
first_name = "Jacob"
last_name = "Lee"
full_name = f"{first_name} {last_name}"
print(full_name)