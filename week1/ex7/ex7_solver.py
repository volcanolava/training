from textwrap import wrap

colors = "D36CD041B8BCBE54FC45CA094806018009F87AFE7066B596E44DF51F7166336960C067F373DBFFB029A1000AC7FAC61E3E108689107EF26DD4F6A72098F70117BDA275E10FA8207F892B1DFF1D7B86CBE070292BFF0A96167EA258D234A31B1C70AFC3B8C3C126C02291090A3264C93E6857AE82CE82DA2CAC1791941BB2230D75B819A060ADBD25AD39B92145F77CD34F5084D4335A2FD046A636A51F3E0067E4FAAB249CFB05A36CB0BF4BCB33571A8AF664D740A922838D3B1E40CC3FA6B0DE90993B6117A50E98897CF4D864D53BAF173FF56FD140B8B9AC87BFD5DF7EF14C5A4E29B9FC863FE4C1831685C4DA7FD652533344C58568EF1342A705E4AAFD88F26BD542B22D48F972EA495335900065FF63D542BEDB8C057DDCE6A707D47FEE86127FEF6A8547A81341F771D342BABB2E791183E562D2EDA31D7FEE66679B18711C9F208B007ADC4BC3C419ECA061D3BCAB2021AD2D95B97BE347C929530983E1685E58A22EA10832E862C433ABAC472E84C87A09C353BF2DA00972EB4C56C912ABAD464E1DBA46BF1690B364DD55B4BEEC80B73609314CDC3CAB2144F56EE6454F0367C478F01136C242AACE90F85CDE3E6819920A69731958DF4DC13CA3C588F864D245AE1790F1FB4DE146BA279E9E96ADC0FC3FDAE263EB0DD965E54D712F9B0783E10BC13B9D0C8485F17EF060DEF9AA239BFA047E79858D4B9D6A0577E249BE30A704809D4EC73F9EA82884188BAD63DD3BC2B8281AC145F0EBF0F2048CF072D2FCAD269EFD0786ABAC22DA1119A5118DEB15C845A313203CB4FFF4A0CE0F93187E9F55CF31A01819F7DFDF40983A1FB31B9B0C79DB5AC728324E53F9D9FB50AE4DC01B96F979DF53B9C3B63DA9669528B336B62291FF000CDA57EE725B81FEF314CF63CF3CA70F19FDC6E75A00CD979AD6BD3FD937BEB40DA13A40FEE722C6F87D10C9DC63E0F6A72098F701B02149B4E6F1AB9ACE5AC737B2CD8FF673893AB32B8A941A7BDD76EE4D773C9E137FE765602842B390D5D864E44C703193010C8E1290C624D7DEDA69F575DD01BD2095027AEF4B59DE4DB3D3910E80EF66CEF8A928940B71723F6084F67B0787EF13D536A1CF85FF61D0484915579C289505809B51CB2D9C1415087A4C3E048E1583F772D9FBBA2E9A0772DAE404A43B9E2AAA1236FB5DD23EA6241F129C917E21A3239D052FE55FC130A8A94F980FCDA3F5B03CBC24480678D84CBC2631CBB0C644E456D147B6289FB76DE749B83031EA7EE07549CE39B120829076FB18A5A18EFDB6F12151F05CD3393A5111A293EAD47057968F2F4CD858C0E49A1472F9EF2231AAF0B525D5E571DE4EC9E4950E86E5EF2D0B9CD46C3C59F355C43C5D2580F665D74E464EAC3AC27BFB75DD07CA3AA61487F059D2333DC088740279D545C1DE8F0880DFE9299C79F43CFB8D0567D352B821989CD7B68065CC75C9129E1E86AA60D743AA1A920571D5E0357D149B097DF85F813FB11185F55F6A76BC2832BE31A6BC6DEC58CF3536226B1B01986C9521A1092DE753BB34A1A756724CB080E9BD42B42D8B07046AB0D5DE455D8C9619EA2CC02599007C9D5EC02E395269D52D9E6B4CD04CBEB8D013C1D9579A6CAFE5385CB4D064DA3DB824880A6A746AE92EA44F266CDA56D2D3A53B7C20006F04CF4C9C8F968BEB77E454CFEAA01A7CFFF5A04DE3E75931EC6FDF58C82F97A1F601AD42D8494ED6E8780A6ADE4EB8C3145710BCF9D3470A441A69006CD343BB2E9AFE094EB78A013419DC7E1C82F56AD5434452001188264B2E5CBFFB84FB6FE341BD2F9B9BD16F539A508CDC952098FF01C165FE995EBD056A3CC4582CA042AE17930067D63A45E88900C8427055A32F9C0C87A254D930ACAD10745AD600DCBC40C4229AFF6FEBE85E728C731E68EA0825B13199BD7FDC56C637A5A6F5CC1C4D1350D247B31B99944BC8040FE2501E9A66D13FCB38A8233EF06BDD3BB5B8256E4E46A357E34BC43137F1A1F4618DEC06822B3D94DE78E44DBEE899128AE9F383F163C6C7335EF462C84BA515968E4D59E321F6230C35701882EE505ADDFBD89E16B0A1C8DA14327BF874D95D7324A30F86ECED68E08580371090FC67E9E4A10DA2A49D55699F2F6AD2F486F966D3DD2BC29D37C01D39F533D16F22A2128CEC69D243AE1721EBF19DBF77E0119C1085A052D0329D181ACF855F9D27A89C2CA21585A066C636B0101A07115CEAFFC13EB828990708EB13CFEB60AACE6BBD7128C4399D1487E610D636A620808A5D54BD4CD84CB22A2BB43288DF37928FCE4AC82BC04CB3DE99FD6EDFE99CC54CF436884410DC5ECCD7010505E4EE86A8251AB001BB9CC967C438B2177E8CE082F9E496C5280C61E96CE14EC63B97A58E27574C6FB6A8B85C710170EA09C830A4101405625A9AAF3E75750765E149B6E0A103717C7A97EB7F8941931D8AED6FD9D94BD2EC197C166182540A00960A25E44CC02C301F0BBDCE9A2E7BE38C2799F77174AF24DB04EAF5801C83BBDB861292FA1EDC4EAC2890FD07F6F9134ED3A733A0108BA668C53FAF208E8F18337B4CA335930F77E4EEF9CFC1E5C23FE69BA0CC31BD2A9A1530EF57CB373BF089ECE8C0D54ED64AB6BAFBA47AE9ABDAE86000C5523E3ED541A8B3B77C31386CC2719B1EA5756460E44FC0345B1A8EEE5D66237EB5DFF5954FD155AF279BBB81E151CB2B356D69A05867F85BCA37B81D9192F175F930F5E8EE8955EB64D144A3AD73487B4D0C07F11DB37379047DED617738A4177882510D17C621B0FF98FC78DC50BC2A55057FEF60CE333E9C06860464EB42703696067C7B723A2E96FF1B9F2381F95ECE4A6718910976DAE1B03F1B9C0735F75BC73DACAFE896E896F77F1A9C37A91488ED5FCDD1C11357A770CE0CFF1EA61D8EFC1DCF43B31F8E0674758754AD31C638AA0882A56BCB3BB5151FAC867FB237C131A8A0C9E472D44EE2E414C0F54B82CE49BF2EA0170FEC8819342193C6689784DA66D343BED9A1FC72E153CAC2C7C1C993D06CD446BCB2D21D9B8889E361A40191B9F777E761C1CB450110C155F4876A880809"

name = input("Enter your name: ")
quest = input("Enter your quest: ")

key = 0x55

# Process name


def _process_buffer(_key, _buffer, _left_factor, _right_factor):
    for _i in range(len(_buffer)):
        _key = (ord(_buffer[_i]) + _key) & 0x7f
        _key = (_key << _left_factor | _key >> _right_factor) & 0x7f

    return _key


key = _process_buffer(key, name, 3, 4)
key = _process_buffer(key, quest, 4, 3)

# Key final process

for i in range(4):
    key = (key + 0x55) & 0x7f
    key = (key << 3 | key >> 4) & 0x7f

# 'Choose' color and calculate factor

start_ind = ((key << 4) + key) * 2
encoded_color = wrap(colors[start_ind:start_ind+32], 2)

factor = ((((key << 3) - key) + 0x33) ^ 0xffffffcc) & 0xff

#  Decode needed color
decoded_color = ""
for i in range(len(encoded_color)):
    _current_decoded_char = int(encoded_color[i], 16) - ((factor + i) * 0x6f)
    decoded_color += chr(_current_decoded_char & 0xff)

print(f"Your favorite color should be: {decoded_color}")

