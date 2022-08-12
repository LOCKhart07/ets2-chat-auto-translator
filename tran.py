from googletrans import Translator
translator = Translator()
# print(translator.translate('[21:01:39] VΛBIƧ (1763): aga bıraz onune kırdım ama', dest = 'en').text)

# import re
# tmpID = r" \(([0-9+])*\)\: "

# stri = '[20:55:12] WOLFSEUS_fastik (1948): токните меня але'
# spliStri = re.search(tmpID, stri)
# # print(spliStri)


# print(stri.split(spliStri.group())[1])

import re
tmpID = r"^.+\(\d+\): "

stri = '[20:55:12] WOLFSEUS_fastik (1948): токните меня але'
spliStri = re.search(tmpID, stri)
prequel = spliStri.group()
sequel = stri.split(spliStri.group())
translated = str(prequel) + str(translator.translate(sequel[1],dest = 'en').text)
print(translated)

# Translated(src=tr, dest=en, text=[21:01:39] VΛBIƧ (1763): but I broke it a little bit, pronunciation=[21:01:39] VΛBIƧ (1763): but I broke it a little bit, extra_data="{'translat...")