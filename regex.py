#Q1
import re
email1 = "zuck26@facebook.com"
email2="page33@google.com"
email3="jeff42@amazon.com"
output=re.split(r'[@.]+',email1)
output2=re.split(r'[@.]+',email2)
output3=re.split(r'[@.]+',email3)
list=[tuple(output),tuple(output2),tuple(output3)]
print(list)


#Q2
import re

str="Betty bought a bit of butter, But the butter was so bitter, So she bought some better butter, To make the bitter butter better."
print(re.findall(r'[Bb]\w+',str))

#Q3
import re
sentence = "A, very very; irregular_sentence"
output=re.split(r'[;,\s_]+',sentence)
string = ' '.join(output)
print(string)